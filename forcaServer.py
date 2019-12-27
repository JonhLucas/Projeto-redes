import socket
import random

words_Server = {"Frutas":['uva','maçã','laranja','banana','pera','mamão','abacate'],
                "Animais":['macaco','gato','cachorro','galinha','cobra','tartaruga'],
                "Cores":['azul','verde','vermelho','preto','amarelo','rosa','marrom'],
                "Países":['brasil','italia','alemanha','inglaterra','venezuela','espanha']}

address = ("localhost",20002)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(1)

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
    
def change_word(category):
    words = words_Server[category]
    return (words[random.randrange(0,len(words))])
        
winner = 0

print("Servidor escutando...Aguardando Usuarios")

#try:
while True:
    conec, client = server.accept()
    
    catg = conec.recv(1024)
    catg = catg.decode()
    word = change_word(catg)
    print(word)
    word_clients = []

    for i in range(len(word)):
            word_clients.append('_')
    
    print(word_clients)
    
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
            print("Errou!")
            
        conec.send((','.join(word)).encode())            
#except:
#    server.close()