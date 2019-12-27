import socket
import random
import threading

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

def manager_Client(conec,word):
    
    while True:
        letter = conec.recv(2)
        letter = letter.decode()
        
        print(letter)
        
        right,fault_qtd = check_tentative(letter)
        
        if(fault_qtd == 0):
            print("End Game!")
            break
        elif(right):
            print("Acerto!")
        else:
            print("Errou! Passando a vez...\n")
            break
        
        print(word_clients)   


#escopo principal

words_Server = {"Frutas":['uva','maçã','laranja','banana','pera','mamão','abacate','abacaxi','melão','cereja','tangerina'],
                "Animais":['macaco','gato','cachorro','galinha','cobra','tartaruga','cabra','boi','vaca','escorpião','sapo'],
                "Cores":['azul','verde','vermelho','preto','amarelo','rosa','marrom','roxo','branco','cinza','lilas','violeta'],
                "Países":['brasil','italia','alemanha','inglaterra','venezuela','espanha','islandia','Noruega','Portugal','Belgica']}

#criando conexão tcp

address = ("localhost",20002)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

print("\n--------------------------------")
print("|------JOGO DA FORCA-----------|")
print("--------------------------------")

print("\n-> Aguardando jogadores....\n")

first_iteration = True
winner = 0
cont_plays = 1
cont_categories = 1

print("-----------------CATEGORIAS-----------------")
for i in words_Server:
    print("{a} - {cat}".format(a=cont_categories,cat=i))
    cont_categories = cont_categories + 1
print("--------------------------------------------")
try:
    while True:
        
        conec, client = server.accept()
        if(first_iteration):
            conec.send('s'.encode())
            
        print("Jogador {a} entrou no jogo...".format(a=cont_plays))
        cont_plays = cont_plays + 1
        
        if(first_iteration):
            
            catg = conec.recv(1024)
            catg = catg.decode()
            word = change_word(catg)
        
            print(word)
            word_clients = []

            for i in range(len(word)):
                    word_clients.append('_')
                    
            print(word_clients)
            new_client = threading.Thread(target=manager_Client,args=(conec,word))
            new_client.start()
            
            first_iteration = False
        else:
            conec.send('n'.encode())
            new_client = threading.Thread(target=manager_Client,args=(conec,word))
            new_client.start()
            #conec.send((','.join(word)).encode())
        
except:
    server.close()