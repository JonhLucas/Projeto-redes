from principal import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
import threading, time, random, socket


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
        self.label_5.setText(_translate("MainWindow", "Tema:"))
        self.label_3.setText(_translate("MainWindow", "Variavel"))
        self.label_7.setText(_translate("MainWindow", "Palavra"))
        self.label_6.setText(_translate("MainWindow", "Digite uma letra"))
        self.pushButton_3.setText(_translate("MainWindow", "Palpite"))
        self.label_4.setText(_translate("MainWindow", "Escolha uma categoria"))
        self.Frutas.setText(_translate("MainWindow", "Frutas"))
        self.Cores.setText(_translate("MainWindow", "Cores"))
        self.Animais.setText(_translate("MainWindow", "Animais"))
        self.Paises.setText(_translate("MainWindow", "Países"))
        self.label_4.setText(_translate("MainWindow", "Escolha uma categoria"))
        self.progressBar.setValue(0)

        def transition():
            def endWaiting():
                time.sleep(1)
                MainWindow.Aguarde.hide()

            tarefa = threading.Thread(target=endWaiting)
            tarefa.daemon = True
            tarefa.start()

        def progress():
            def endWaiting():
                complete = int(0)
                while complete < 100:
                    complete += 1
                    # time.sleep(0.1)
                    MainWindow.progressBar.setValue(complete)

            tarefa = threading.Thread(target=endWaiting)
            tarefa.daemon = True
            tarefa.start()

        def changeBackground():
            MainWindow.widget.setStyleSheet("background-color: #{};".format(random.randint(100000, 999999)))

        def chooseCategory(choice):
            global category
            category = choice
            MainWindow.Aguarde.show()
            MainWindow.Tema.setText(choice)
            # transicao()
            #progress()

        sinal = Sinais()
        sinal.sinal.connect(changeBackground)

        def changeColor():
            while True:
                time.sleep(1)
                sinal.sinal.emit()

        task = threading.Thread(target=changeColor)
        task.daemon = True
        task.start()
        # conexões
        self.criar.clicked.connect(progress)
        self.criar.clicked.connect(transition)
        self.Frutas.clicked.connect(lambda: chooseCategory("Frutas"))
        self.Cores.clicked.connect(lambda: chooseCategory("Cores"))
        self.Animais.clicked.connect(lambda: chooseCategory("Animais"))
        self.Paises.clicked.connect(lambda: chooseCategory("Países"))

def main(ui):
    def createRoom():
        def create_socket():
            try:
                port = int(ui.lineEdit.text())
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
                    ui.Aguarde.hide()
                else:
                    ui.Aguarde.hide()
                    ui.tela_escolha.hide()
                #messagem inicial
                messenge_inicial = client.recv(4096).decode().split('#')
                ui.label_7.setText(messenge_inicial[0])
                ui.Tema.setText(messenge_inicial[1])
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
                            ui.palpite.hide()
                            ui.resultado.setText("Vitoria")
                        print(response[0], response[1])
                        ui.label_7.setText(status[1])
                    else:
                        print('espere sua vez')
                        response = client.recv(4096)
                        palavra = response.decode().split("#")
                        status = palavra[0].split(":")
                        if 'Sua vez' in status[0]:
                            keeper = 1
                        elif 'vitoria' in status[0]:
                            playing = False
                            client.close()
                        elif 'update' in status[0]:
                            #print("atualização:", palavra[0])
                            ui.label_7.setText(status[1])
                        else:
                            print("voce perdeu")
                            playing = False
                            client.close()
                            ui.palpite.hide()
                            ui.resultado.setText("Derrota!")
                        print(response.decode())

        tarefa_principal = threading.Thread(target=create_socket)
        tarefa_principal.start()

    ui.criar.clicked.connect(createRoom)


response = "Valor inicial"
category = "inicial"
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    main(ui)
    sys.exit(app.exec_())
