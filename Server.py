import socket
import threading
from Room import Room


def manager_room():
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
                if rooms[e]:
                    r = r + str(e) + '*'
            r = r + "#"
            for e in rooms:
                if not rooms[e]:
                    r = r + str(e) + '*'
            i_conec.send(r.encode())
            r = ""
            answer = i_conec.recv(4096).decode()
            ans = answer.split('#')
            rooms[int(ans[0])] = False
            if 'criar' in ans[1]:
                def create_room():
                    room = Room(int(ans[0]))

                task = threading.Thread(target=create_room, args=())
                task.start()
                print('Sala criada', answer)
            elif 'entrar' in ans[1]:
                print('Entrou na sala:', answer)
            i_conec.close()
    except socket.error:
        print("Erro na conexao")


rooms = {20001: True, 20002: True, 20003: True, 20004: True, 20005: True}
manager_room()
