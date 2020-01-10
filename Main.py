import random
import socket
import threading
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal

from principal import Ui_MainWindow


class Sinais(QtCore.QObject):
    sinal = pyqtSignal()

    def __init__(self):
        QtCore.QObject.__init__(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """docstring for MainWindow"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(_translate("MainWindow", "Criar nova sala:"))
        self.criar.setText(_translate("MainWindow", "Criar"))
        self.label_2.setText(_translate("MainWindow", "Digite o código da sala que deseja entrar"))
        self.Entrar.setText(_translate("MainWindow", "entrar"))
        self.label_8.setText(_translate("MainWindow", "Resultado:"))
        self.resultado.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Digite uma letra"))
        self.pushButton_3.setText(_translate("MainWindow", "Palpite"))
        self.label_10.setText(_translate("MainWindow", "Letras utilizadas:"))
        self.Palpites.setText(_translate("MainWindow", "[]"))
        self.label_11.setText(_translate("MainWindow", "Palavra:"))
        self.label_7.setText(_translate("MainWindow", "Palavra"))
        self.label_5.setText(_translate("MainWindow", "Tema:"))
        self.Tema.setText(_translate("MainWindow", "Variavel"))
        self.Frutas.setText(_translate("MainWindow", "Frutas"))
        self.Cores.setText(_translate("MainWindow", "Cores"))
        self.Animais.setText(_translate("MainWindow", "Animais"))
        self.Paises.setText(_translate("MainWindow", "Países"))
        self.label_4.setText(_translate("MainWindow", "Escolha uma categoria"))
        self.label_3.setText(_translate("MainWindow", "Aguarde"))

        self.progressBar.setValue(0)

        def transition():
            def end_waiting():
                time.sleep(1)
                MainWindow.Aguarde.hide()

            tarefa = threading.Thread(target=end_waiting)
            tarefa.daemon = True
            tarefa.start()

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
        '''def change_background():
            MainWindow.widget.setStyleSheet("background-color: #{};".format(random.randint(100000, 999999)))

        sinal = Sinais()
        sinal.sinal.connect(change_background)

        def change_color():
            while True:
                time.sleep(1)
                sinal.sinal.emit()

        task = threading.Thread(target=change_color)
        task.daemon = True
        task.start()'''
        # conexões
        self.criar.clicked.connect(progress)
        self.criar.clicked.connect(transition)
        self.Frutas.clicked.connect(lambda: choose_category("Frutas"))
        self.Cores.clicked.connect(lambda: choose_category("Cores"))
        self.Animais.clicked.connect(lambda: choose_category("Animais"))
        self.Paises.clicked.connect(lambda: choose_category("Países"))


def main(mw):
    def create_room():
        def create_socket():
            try:
                port = int(mw.lineEdit.text())
                print("Endereço solicitado:", port)
            except:
                port = 20002
                print('Endereço invalido. Encaminhando para:', port)

            address = ("localhost", port)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(address)
            playing = True
            keeper = 0  # condição para leitura de dados
            guesses = []
            print("Cliente ativo, fazendo requisição\n")
            # try:
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
                        print('leitura liberada')
                        letter = input('Uma letra: ')
                        letter = letter.encode()
                        client.send(letter)
                        response = client.recv(4096).decode().split("#")
                        palavra = response[1].split(":")
                        status = response[0].split(":")
                        if 'Errado' in status[0]:
                            keeper = 0
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
                            #duas mensagens estão sendo recebidas ao mesmo tempo, update e sua vez
                            palavra = response.split("#")
                            status = palavra[0].split(":")
                            p = palavra[1].split(":")
                            mw.label_7.setText(status[1])
                            mw.Palpites.setText(p[1][0:(p[1].find(']') + 1)])

        tarefa_principal = threading.Thread(target=create_socket)
        tarefa_principal.start()

    mw.criar.clicked.connect(create_room)


response = "Valor inicial"
category = "inicial"
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    main(ui)
    sys.exit(app.exec_())
