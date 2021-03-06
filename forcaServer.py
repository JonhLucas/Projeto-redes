import socket
import random
import threading
import time


def submission_client():
    global cont_plays
    global ready
    global submission
    while cont_plays < 2:
        print(cont_plays)
        time.sleep(10)
    ready = True
    submission = False
    print("O jogo pode começar")


# Função responsavel por chegar se a letra está contida na palavra

def check_tentative(letter):
    have = False
    faul_letter = 0

    for i in range(len(word)):
        if word[i] == letter:
            word_clients[i] = letter
            have = True
        if word_clients[i] == '_':
            faul_letter = faul_letter + 1

    return have, faul_letter


# função responsavel por escolher uma palavra entre todas disponiveis para a categoria escolhida

def change_word(category):
    words = words_Server[category]
    return (words[random.randrange(0, len(words))])


# função responsavel por gerenciar cada cliente threading

def manager_client(conec, word, number_player, catg):
    global counter
    global cont_plays
    global victory
    global submission
    global guesses
    first_time = True
    # messagem inicial
    conec.send(str(word_clients).encode() + "#".encode() + catg.encode())
    while not victory:
        # Validacao do jogador
        if ready and number_player == counter:
            if first_time:
                conec.send(
                    "Sua vez:".encode() + str(word_clients).encode() + "#palpite:".encode() + str(guesses).encode())
                first_time = False
            letter = conec.recv(2)
            letter = letter.decode()

            print("Letra escolhida:", letter)
            guesses.append(letter)
            print(str(guesses))

            right, fault_qtd = check_tentative(letter)

            if (fault_qtd == 0):
                print("End Game!")
                conec.send(
                    'vitoria:'.encode() + str(word_clients).encode() + "#palpite:".encode() + str(guesses).encode())
                submission = False  # lembrar de apagar
                # conec.close()
                victory = True
                break
            elif (right):
                print("Acerto!")
                conec.send(
                    'Acertou:'.encode() + str(word_clients).encode() + "#palpite:".encode() + str(guesses).encode())
            else:
                print("Errou! Passando a vez...\n")
                counter = 1 + counter % cont_plays
                print("Agora a vez é de ", counter)
                conec.send(
                    'Errado:'.encode() + str(word_clients).encode() + "#palpite:".encode() + str(guesses).encode())
                first_time = True
            print(word_clients)
        elif ready and not victory:
            time.sleep(1)
            conec.send("update:".encode() + str(word_clients).encode() + "#palpite:".encode() + str(guesses).encode())

    time.sleep(1)
    conec.send('derrota'.encode())
    conec.close()


def manager_room(ipaddress):
    global rooms
    def submit_rooms():
        try:
            print("Divulgação de salas")
            r = ""
            i_port = 20000
            i_address = ("localhost", i_port)
            i_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            i_server.bind(i_address)
            i_server.listen(5)
            while True:
                i_conec, i_client = i_server.accept()
                print("Nova conexao estabelecida:", i_client)
                for e in rooms:
                    if rooms[e] == True:
                        r = r + str(e) + '*'
                r = r + "#"
                for e in rooms:
                    if not rooms[e]:
                        r = r + str(e) + '*'
                i_conec.send(r.encode())
                #print(r)
                r = ""
                devolvido = i_conec.recv(4096).decode()
                print("Devolvido:", devolvido)
                rooms[int(devolvido)] = False
                i_conec.close()
        except socket.error:
            print("Erro na conexao")

    task = threading.Thread(target=submit_rooms, args=())
    task.start()


# escopo principal

words_Server = {"Frutas": ['uva', 'maçã', 'laranja', 'banana', 'pera', 'mamão', 'abacate', 'abacaxi', 'melão', 'cereja',
                           'tangerina'],
                "Animais": ['macaco', 'gato', 'cachorro', 'galinha', 'cobra', 'tartaruga', 'cabra', 'boi', 'vaca',
                            'escorpião', 'sapo'],
                "Cores": ['azul', 'verde', 'vermelho', 'preto', 'amarelo', 'rosa', 'marrom', 'roxo', 'branco', 'cinza',
                          'lilas', 'violeta'],
                "Países": ['brasil', 'italia', 'alemanha', 'inglaterra', 'venezuela', 'espanha', 'islandia', 'Noruega',
                           'Portugal', 'Belgica']}
# Listar salas
ip = "localhost"
rooms = {20001: True, 20002: True, 20003: True, 20004: True, 20005: False}
manager_room(ip)

# criando conexão tcp

port = 20002
address = (ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

print("\n--------------------------------")
print("|------JOGO DA FORCA-----------|")
print("--------------------------------")

print("\n-> Aguardando jogadores....\n")

first_iteration = True
winner = 0
cont_plays = 0
cont_categories = 1
counter = 1
victory = False
submission = True
ready = False
guesses = []
# trava = threading.allocate_lock()

print("-----------------CATEGORIAS-----------------")
for i in words_Server:
    print("{a} - {cat}".format(a=cont_categories, cat=i))
    cont_categories = cont_categories + 1
print("--------------------------------------------")
try:
    # submission
    while submission:

        conec, client = server.accept()
        print("conexao:", client)
        if (first_iteration):
            conec.send('s'.encode())

        cont_plays = cont_plays + 1
        print("Jogador {a} entrou no jogo...".format(a=cont_plays))

        if (first_iteration):

            catg = conec.recv(1024)
            catg = catg.decode()
            word = change_word(catg)

            print(catg, ":", word)
            word_clients = []

            for i in range(len(word)):
                word_clients.append('_')

            print(word_clients)
            new_client = threading.Thread(target=manager_client, args=(conec, word, cont_plays, catg))
            new_client.start()

            first_iteration = False
            time_submission = threading.Thread(target=submission_client, args=())
            time_submission.daemon = True
            time_submission.start()
            #rooms[20002] = False
            #print(rooms[20002], "lembrar de apagar")
        else:
            conec.send('n'.encode())
            new_client = threading.Thread(target=manager_client, args=(conec, word, cont_plays, catg))
            new_client.start()
            # conec.send((','.join(word)).encode())
    print("fechando")
    server.close()
except:
    server.close()
