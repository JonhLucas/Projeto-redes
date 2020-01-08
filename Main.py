from principal import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from Client import Client
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

		def CriarSala():
			print('Sala criada!')

		self.criar.clicked.connect(CriarSala)
		
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


		def transicao():
			def apagarAguarde():
				time.sleep(1)
				MainWindow.Aguarde.hide()

			tarefa = threading.Thread(target = apagarAguarde)
			tarefa.daemon = True
			tarefa.start()

		def b():
			MainWindow.widget.setStyleSheet("background-color: #{};".format(random.randint(100000,999999))) 
		
		def escolherCategoria(choose):
			global category
			category = choose
			MainWindow.Aguarde.show()
			MainWindow.Tema.setText(choose)
			#transicao()

		sinal = Sinais()
		sinal.sinal.connect(b)
		def changeColor():
			while True:
				time.sleep(1)
				sinal.sinal.emit()

		tarefa = threading.Thread(target=changeColor)
		tarefa.daemon = True
		tarefa.start()
		#conexões
		self.criar.clicked.connect(transicao)
		self.Frutas.clicked.connect(lambda: escolherCategoria("Frutas"))
		self.Cores.clicked.connect(lambda: escolherCategoria("Cores"))
		self.Animais.clicked.connect(lambda: escolherCategoria("Animais"))
		self.Paises.clicked.connect(lambda: escolherCategoria("Países"))


def main(ui):

	def a():

		def create_socket():
			address = ("localhost", 20002)
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect(address)
			playing = True
			keeper = 0 #condição para leitura de dados
			print("Cliente ativo, fazendo requisição\n")
			#try:    
			while playing:
			    print('inicio de jogo')
			    control = client.recv(2)
			    control = control.decode()
			    if(control == 's'):
			        print("-> Jogador 1, informe a categoria de palavras deseja\n")
			        while category == "inicial":
			        	time.sleep(1)
			        client.send(category.encode())
			        print("esperando conexão de outros jogadores")
			        ui.Aguarde.hide()
			    else:
			    	ui.Aguarde.hide()
			    	ui.tela_escolha.hide()

			    messenge_inicial = client.recv(4096).decode()
			    print(messenge_inicial)
			    nova = messenge_inicial.find(']')
			    ui.label_7.setText(messenge_inicial[0:nova+1])
			    ui.Tema.setText(messenge_inicial[nova+1:]) 
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
				        	ui.palpite.hide()
				        	ui.resultado.setText("Vitoria")
				        palavra = response.decode()
				        print(palavra)
				        ui.label_7.setText(palavra[7:])
			        else:
			        	print('espere sua vez')
			        	response = client.recv(4096)
			        	palavra = response.decode()
				        if 'Sua vez' in response.decode():
				        	keeper = 1
				        elif 'vitoria' in response.decode():
				        	playing = False
				        	client.close()
				        elif 'update' in response.decode():
				        	print("atualização:", response.decode())
				        	ui.label_7.setText(palavra[7:])
				        else:
				        	print("voce perdeu")
				        	playing = False
				        	client.close()
				        	ui.palpite.hide()
				        	ui.resultado.setText("Derrota!")
				        print(response.decode())


		tarefa_principal = threading.Thread(target=create_socket)
		tarefa_principal.daemon = True
		tarefa_principal.start()

	ui.criar.clicked.connect(a)



response = "Valor inicial"
category = "inicial"
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    main(ui)
    sys.exit(app.exec_())