import socket
import time

address = ("localhost", 20002)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
playing = True

print("Cliente ativo, fazendo requisição\n")

#try:    
while playing:
    print('inicio de jogo')
    control = client.recv(2)
    control = control.decode()
    keeper = 0 #condição para leitura de dados
    if(control == 's'):
        print("-> Jogador 1, informe a categoria de palavras deseja\n")
        category = input()
        client.send(category.encode())
        print("esperando conexão de outros jogadores")
        #time.sleep(10)
        #message = client.recv(1024)
        #print(message.decode())   
        
    while playing:
        if keeper:
        	print('leitura liberada')
        	letter = input('Uma letra: ')
	        letter = letter.encode()
	        client.send(letter)
	        response = client.recv(4096)
	        if 'Errado ' in response.decode():
	        	keeper = 0
	        elif 'vitoria' in response.decode():
	        	playing = False
	        	print('Voce venceu!')
	        palavra = response.decode()
	        print(palavra)
        else:
        	print('espere sua vez')
        	response = client.recv(4096)
	        if 'Sua vez' in response.decode():
	        	keeper = 1
	        elif 'vitoria' in response.decode():
	        	playing = False
	        	client.close()
	        else:
	        	print("voce perdeu")
	        	playing = False
	        	client.close()
	        print(response.decode())





#except:
#    client.close()
	        
	        