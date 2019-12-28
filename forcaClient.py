import socket
import time

address = ("localhost", 20002)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

print("Cliente ativo, fazendo requisição\n")

#try:    
while True:
    
    control = client.recv(2)
    control = control.decode()
    keeper = 0 #condição para leitura de dados
    if(control == 's'):
        print("-> Jogador 1, informe a categoria de palavras deseja\n")
        category = input()
        client.send(category.encode())
        print("esperando 10 segundo para conexão de outros jogadores")
        time.sleep(10)
        #message = client.recv(1024)
        #print(message.decode())   
        
    while True:
        if keeper:
        	print('leitura liberada')
        	letter = input('Uma letra: ')
	        letter = letter.encode()
	        client.send(letter)
	        response = client.recv(4096)
	        if 'Errado ' in response.decode()  :
	        	keeper = 0
	        palavra = response.decode()
	        print(palavra[7:])
        else:
        	print('espere sua vez')
        	response = client.recv(4096)
	        if 'Sua vez' in response.decode():
	        	keeper = 1
	        print(response.decode())
        
#except:
#    client.close()
	        
	        