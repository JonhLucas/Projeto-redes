import socket

address = ("localhost",20002)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

print("Cliente ativo, fazendo requisição\n")
try:    
    while True:
        
        category = input("Informe a palavra desejada:")
        client.send(category.encode())
        message = client.recv(1024)
        print(message.decode())   
        
        while True:
            letter = input('Uma letra: ')
            letter = letter.encode()
            client.send(letter)
             
except:
    client.close()