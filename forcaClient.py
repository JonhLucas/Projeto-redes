import socket

address = ("localhost",20002)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

print("Cliente ativo, fazendo requisição\n")

#try:    
while True:
    
    control = client.recv(2)
    control = control.decode()
    
    if(control == 's'):
        print("-> Jogador 1, informe a categoria de palavras deseja\n")
        category = input()
        client.send(category.encode())
        #message = client.recv(1024)
        #print(message.decode())   
        
    while True:
        letter = input('Uma letra: ')
        letter = letter.encode()
        client.send(letter)
        
#except:
#    client.close()