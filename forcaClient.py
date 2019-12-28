import socket

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
        #message = client.recv(1024)
        #print(message.decode())   
        
    while True:
        if keeper:
        	print('leitura liberada')
        	letter = input('Uma letra: ')
	        letter = letter.encode()
	        client.send(letter)
	        response = client.recv(4096)
	        if response.decode() == 'Errou':
	        	keeper = 0
	        print(response.decode())
        else:
        	print('espere sua vez')
        	response = client.recv(4096)
	        if response.decode() == 'Sua vez':
	        	keeper = 1
	        print(response.decode())
        
#except:
#    client.close()
	        
	        