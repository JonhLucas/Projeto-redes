import socket
import random
import threading
import time



def submission_Client():
    global cont_plays
    global ready
    global submission
    while cont_plays < 2:
        print(cont_plays)
        time.sleep(10)
    ready = True
    submission = False
#Função responsavel por chegar se a letra está contida na palavra

def check_tentative(letter):
    
    have = False
    faul_letter = 0
    
    for i in range(len(word)):
        if(word[i] == letter):
            word_clients[i] = letter
            have = True
        if(word_clients[i] == '_'):
            faul_letter = faul_letter + 1
    
    return (have,faul_letter)

#função responsavel por escolher uma palavra entre todas disponiveis para a categoria escolhida

def change_word(category):
    words = words_Server[category]
    return (words[random.randrange(0,len(words))])

#função responsavel por gerenciar cada cliente threading

def manager_Client(conec,word, number_player):
    global contador
    global cont_plays
    global victory
    first_time = True
    conec.send(str(word_clients).encode())
    while not victory:
        #Validacao do jogador
        if ready and number_player == contador:
            if first_time:
                conec.send("Sua vez".encode())
                first_time = False
            letter = conec.recv(2)
            letter = letter.decode()
            
            print("Letra escolhida:",letter)
            
            right,fault_qtd = check_tentative(letter)
            
            if(fault_qtd == 0):
                print("End Game!")
                conec.send('vitoria'.encode() + str(word_clients).encode())
                #conec.close()
                victory = True
                break
            elif(right):
                print("Acerto!")
                conec.send('Acertou'.encode() + str(word_clients).encode())
            else:
                print("Errou! Passando a vez...\n")
                contador = 1 + contador%cont_plays
                print("Agora a vez é de ", contador)
                conec.send('Errado '.encode() + str(word_clients).encode())
                first_time = True
            print(word_clients)
        elif ready and not victory:
            time.sleep(1)
            conec.send("update ".encode() + str(word_clients).encode())
            #print("envio", number_player)

    time.sleep(1)
    conec.send('derrota'.encode())
    conec.close()



#escopo principal

words_Server = {"Frutas":['uva','maçã','laranja','banana','pera','mamão','abacate','abacaxi','melão','cereja','tangerina'],
                "Animais":['macaco','gato','cachorro','galinha','cobra','tartaruga','cabra','boi','vaca','escorpião','sapo'],
                "Cores":['azul','verde','vermelho','preto','amarelo','rosa','marrom','roxo','branco','cinza','lilas','violeta'],
                "Países":['brasil','italia','alemanha','inglaterra','venezuela','espanha','islandia','Noruega','Portugal','Belgica']}

#criando conexão tcp

address = ("localhost", 20002)
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
contador = 1
victory = False
submission = True
ready = False
#trava = threading.allocate_lock()

print("-----------------CATEGORIAS-----------------")
for i in words_Server:
    print("{a} - {cat}".format(a=cont_categories,cat=i))
    cont_categories = cont_categories + 1
print("--------------------------------------------")
try:
    #submission
    while submission:
        
        conec, client = server.accept()
        if(first_iteration):
            conec.send('s'.encode())
            
        cont_plays = cont_plays + 1
        print("Jogador {a} entrou no jogo...".format(a=cont_plays))
        
        if(first_iteration):
            
            catg = conec.recv(1024)
            catg = catg.decode()
            word = change_word(catg)
        
            print(word)
            word_clients = []

            for i in range(len(word)):
                    word_clients.append('_')
                    
            print(word_clients)
            new_client = threading.Thread(target=manager_Client,args=(conec,word,cont_plays))
            new_client.start()
            
            first_iteration = False
            time_submission = threading.Thread(target=submission_Client, args=())
            time_submission.start()

        else:
            conec.send('n'.encode())
            new_client = threading.Thread(target=manager_Client,args=(conec,word,cont_plays))
            new_client.start()
            #conec.send((','.join(word)).encode())
        
except:
    server.close()