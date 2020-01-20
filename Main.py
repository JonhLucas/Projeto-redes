import random
import socket
import threading
import time

from PyQt5 import QtCore, QtWidgets

from MainWindowGui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """docstring for MainWindow"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_9.setText(_translate("MainWindow", "Qual é a palavra?"))
        self.label.setText(_translate("MainWindow", "Ativar nova sala:"))
        self.criar.setText(_translate("MainWindow", "Criar"))
        self.label_2.setText(_translate("MainWindow", "Escolher uma sala:"))
        self.Entrar.setText(_translate("MainWindow", "entrar"))
        self.label_8.setText(_translate("MainWindow", "Resultado:"))
        self.resultado.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Digite uma letra"))
        self.pushButton_3.setText(_translate("MainWindow", "Palpite"))
        self.label_10.setText(_translate("MainWindow", "Letras utilizadas:"))
        self.Palpites.setText(_translate("MainWindow", "[]"))
        self.label_11.setText(_translate("MainWindow", "Status:"))
        self.label_7.setText(_translate("MainWindow", "Palavra"))
        self.label_5.setText(_translate("MainWindow", "Tema:"))
        self.Tema.setText(_translate("MainWindow", "Variavel"))
        self.Frutas.setText(_translate("MainWindow", "Frutas"))
        self.Cores.setText(_translate("MainWindow", "Cores"))
        self.Animais.setText(_translate("MainWindow", "Animais"))
        self.Paises.setText(_translate("MainWindow", "Países"))
        self.label_4.setText(_translate("MainWindow", "Escolha uma categoria"))
        self.label_3.setText(_translate("MainWindow", "Aguarde"))
        self.label_12.setText(_translate("MainWindow", "FIM DO JOGO"))
        self.label_13.setText(_translate("MainWindow", "Bem vindo ao"))

        self.progressBar.setValue(0)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setMaxLength(1)

        def transition():
            def end_waiting():
                time.sleep(1)
                MainWindow.Aguarde.hide()

            task_2 = threading.Thread(target=end_waiting)
            task_2.daemon = True
            task_2.start()

        def progress():
            def addition():
                complete = int(0)
                while complete < 100:
                    complete += 1
                    MainWindow.progressBar.setValue(complete)

            add = threading.Thread(target=addition)
            add.daemon = True
            add.start()

        def choose_category(choice):
            global category
            category = choice
            MainWindow.Aguarde.show()
            MainWindow.Tema.setText(choice)

        def send_letter():
            global character
            character = MainWindow.lineEdit_3.text()
            MainWindow.lineEdit_3.setEnabled(False)
            MainWindow.lineEdit_3.clear()
            print(character)


        # conexões
        self.criar.clicked.connect(progress)
        self.criar.clicked.connect(transition)
        self.Entrar.clicked.connect(progress)
        self.Frutas.clicked.connect(lambda: choose_category("Frutas"))
        self.Cores.clicked.connect(lambda: choose_category("Cores"))
        self.Animais.clicked.connect(lambda: choose_category("Animais"))
        self.Paises.clicked.connect(lambda: choose_category("Países"))
        self.pushButton_3.clicked.connect(send_letter)

    def list_room(self, ip_address):
        try:
            i_port = 20000
            i_address = (ip_address, i_port)
            i_client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            i_client.connect(i_address)
            rooms = i_client.recv(4096).decode().split('#')
            available = rooms[0].split("*")
            occupied = rooms[1].split("*")
            i = 0
            while i < len(available) - 1:
                self.comboBox.addItem(available[i])
                i += 1
            i = 0
            while i < len(occupied) - 1:
                self.comboBox_2.addItem(occupied[i])
                i += 1
        except socket.error:
            print('erro na conexao')
        return i_client


def main(mw, room_socket):
    def create_room(porta):
        def create_socket():
            global character
            print("escolhido", porta)
            p = porta.split('#')
            port = int(p[0])
            room_socket.send(porta.encode())
            time.sleep(1)
            try:
                address = ("localhost", port)
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(address)
            except socket.error:
                print("Erro na conexao")
            playing = True
            keeper = 0  # condição para leitura de dados
            guesses = []
            print("Cliente ativo, fazendo requisição\n")
            while playing:
                print('inicio de jogo')
                control = client.recv(2)
                control = control.decode()
                if (control == 's'):
                    print("-> Jogador 1, informe a categoria de palavras deseja\n")
                    while category == "inicial":
                        time.sleep(1)
                    client.send(category.encode())
                    print("esperando conexão de outros jogadores")
                    mw.Aguarde.hide()
                else:
                    mw.Aguarde.hide()
                    mw.tela_escolha.hide()
                # messagem inicial
                messenge_inicial = client.recv(4096).decode().split('#')
                mw.label_7.setText(messenge_inicial[0])
                mw.Tema.setText(messenge_inicial[1])
                while playing:
                    if keeper:
                        #envio da letra
                        mw.lineEdit_3.setEnabled(True)
                        print('leitura liberada')
                        while character == '':
                            time.sleep(1)
                        print("caracter digitado:", character)
                        client.send(character.encode())
                        character = ''
                        #Retorno do servidor
                        response = client.recv(4096).decode().split("#")
                        palavra = response[1].split(":")
                        status = response[0].split(":")
                        #avaliação da próxima rodada
                        if 'Errado' in status[0]:
                            keeper = 0
                            mw.lineEdit_3.setEnabled(False)
                        elif 'vitoria' in status[0]:
                            playing = False
                            print('Voce venceu!')
                            mw.palpite.hide()
                            mw.resultado.setText("Vitoria")
                        mw.label_7.setText(status[1])
                        mw.Palpites.setText(palavra[1])
                    else:
                        print('espere sua vez')
                        response = client.recv(4096).decode()
                        if 'Sua vez' in response:
                            keeper = 1
                        elif 'vitoria' in response:
                            playing = False
                            client.close()
                        elif 'derrota' in response:
                            print("voce perdeu")
                            playing = False
                            client.close()
                            mw.palpite.hide()
                            mw.resultado.setText("Derrota!")
                        if 'update' in response:
                            # response não pode ser alterado
                            # duas mensagens estão sendo recebidas ao mesmo tempo, update e sua vez
                            palavra = response.split("#")
                            status = palavra[0].split(":")
                            p = palavra[1].split(":")
                            mw.label_7.setText(status[1])
                            mw.Palpites.setText(p[1][0:(p[1].find(']') + 1)])
                            
        tarefa_principal = threading.Thread(target=create_socket, args=())
        tarefa_principal.start()

    mw.criar.clicked.connect(lambda: create_room(mw.comboBox.currentText()+"#criar"))  # lambda: choose_category("Frutas"
    mw.Entrar.clicked.connect(lambda: create_room(mw.comboBox_2.currentText()+"#entrar"))


response = "Valor inicial"
category = "inicial"
character = ""
if __name__ == "__main__":
    import sys

    ip = "localhost"
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    c: socket.socket = ui.list_room(ip)
    ui.show()
    main(ui, c)
    sys.exit(app.exec_())
