import socket
import threading
import time
import random


class Room:

    def __init__(self, port):
        self.port = port
        self.ip = "localhost"
        self.first_iteration = True
        self.winner = 0
        self.cont_plays = 0
        self.cont_categories = 1
        self.counter = int(1)
        self.victory = False
        self.submission = True
        self.ready = False
        self.guesses = []
        self.word_clients = []
        self.words_Server = {
            "Frutas": ['uva', 'maçã', 'laranja', 'banana', 'pera', 'mamão', 'abacate', 'abacaxi', 'melão', 'cereja',
                       'tangerina'],
            "Animais": ['macaco', 'gato', 'cachorro', 'galinha', 'cobra', 'tartaruga', 'cabra', 'boi', 'vaca',
                        'escorpião', 'sapo'],
            "Cores": ['azul', 'verde', 'vermelho', 'preto', 'amarelo', 'rosa', 'marrom', 'roxo', 'branco', 'cinza',
                      'lilas', 'violeta'],
            "Países": ['brasil', 'italia', 'alemanha', 'inglaterra', 'venezuela', 'espanha', 'islandia', 'Noruega',
                       'Portugal', 'Belgica']}
        self.word = ""
        print("iniciada")
        self.run()

    def submission_client(self):
        while self.cont_plays < 2:
            print(self.cont_plays)
            time.sleep(10)
        self.ready = True
        self.submission = False
        print("O jogo pode começar")

    # Função responsavel por chegar se a letra está contida na palavra

    def check_tentative(self, letter):
        have = False
        faul_letter = 0

        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.word_clients[i] = letter
                have = True
            if self.word_clients[i] == '_':
                faul_letter = faul_letter + 1

        return have, faul_letter

    # função responsavel por escolher uma palavra entre todas disponiveis para a categoria escolhida

    def change_word(self, category):
        words = self.words_Server[category]
        return words[random.randrange(0, len(words))]

    # função responsavel por gerenciar cada cliente threading

    def manager_client(self, conec, word, number_player, catg):
        first_time = True
        # messagem inicial
        conec.send(str(self.word_clients).encode() + "#".encode() + catg.encode())
        while not self.victory:
            # Validacao do jogador
            if self.ready and number_player == self.counter:
                if first_time:
                    conec.send(
                        "Sua vez:".encode() + str(self.word_clients).encode()
                        + "#palpite:".encode() + str(self.guesses).encode())
                    first_time = False
                letter = conec.recv(2)
                letter = letter.decode()

                print("Letra escolhida:", letter)
                self.guesses.append(letter)
                print(str(self.guesses))

                right, fault_qtd = self.check_tentative(letter)

                if fault_qtd == 0:
                    print("End Game!")
                    conec.send(
                        'vitoria:'.encode() + str(self.word_clients).encode()
                        + "#palpite:".encode() + str(self.guesses).encode())
                    self.submission = False  # lembrar de apagar
                    # conec.close()
                    self.victory = True
                    break
                elif right:
                    print("Acerto!")
                    conec.send(
                        'Acertou:'.encode() + str(self.word_clients).encode()
                        + "#palpite:".encode() + str(self.guesses).encode())
                else:
                    print("Errou! Passando a vez...\n")
                    self.counter = 1 + self.counter % self.cont_plays
                    print("Agora a vez é de ", self.counter)
                    conec.send(
                        'Errado:'.encode() + str(self.word_clients).encode()
                        + "#palpite:".encode() + str(self.guesses).encode())
                    first_time = True
                print(self.word_clients)
            elif self.ready and not self.victory:
                time.sleep(1)
                conec.send("update:".encode() + str(self.word_clients).encode()
                           + "#palpite:".encode() + str(self.guesses).encode())

        time.sleep(1)
        conec.send('derrota'.encode())
        conec.close()

    def run(self):
        print("\n--------------------------------")
        print("|------JOGO DA FORCA-----------|")
        print("--------------------------------")
        print("\n-> Aguardando jogadores....\n")

        print("-----------------CATEGORIAS-----------------")
        for i in self.words_Server:
            print("{a} - {cat}".format(a=self.cont_categories, cat=i))
            self.cont_categories = self.cont_categories + 1
        print("--------------------------------------------")
        address = (self.ip, self.port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(address)
        server.listen(5)
        try:
            # submission
            while self.submission:

                conec, client = server.accept()
                print("conexao:", client)
                if self.first_iteration:
                    conec.send('s'.encode())

                self.cont_plays = self.cont_plays + 1
                print("Jogador {a} entrou no jogo...".format(a=self.cont_plays))

                if self.first_iteration:

                    catg = conec.recv(1024)
                    catg = catg.decode()
                    self.word = self.change_word(catg)

                    print(catg, ":", self.word)

                    for i in range(len(self.word)):
                        self.word_clients.append('_')

                    print(self.word_clients)
                    new_client = threading.Thread(target=self.manager_client,
                                                  args=(conec, self.word, self.cont_plays, catg))
                    new_client.start()

                    self.first_iteration = False
                    time_submission = threading.Thread(target=self.submission_client, args=())
                    time_submission.daemon = True
                    time_submission.start()
                else:
                    conec.send('n'.encode())
                    new_client = threading.Thread(target=self.manager_client,
                                                  args=(conec, self.word, self.cont_plays, catg))
                    new_client.start()
            print("fechando")
            server.close()
        except:
            server.close()
