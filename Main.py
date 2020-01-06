from principal import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
import threading, time, random, socket

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
		self.comboBox.setItemText(0, _translate("MainWindow", "Frutas"))
		self.comboBox.setItemText(1, _translate("MainWindow", "Cores"))
		self.comboBox.setItemText(2, _translate("MainWindow", "Animais"))
		self.comboBox.setItemText(3, _translate("MainWindow", "Países"))
		self.escolha.setText(_translate("MainWindow", "Escolher"))

		class Sinais(QtCore.QObject):
			sinal = pyqtSignal()
			def __init__(self):
				QtCore.QObject.__init__(self)

		sinal = Sinais()


		def b():
			MainWindow.widget.setStyleSheet("background-color: #{};".format(random.randint(100000,999999)))

		sinal.sinal.connect(b)
		
		def changeColor():
			while True:
				time.sleep(1)
				sinal.sinal.emit()

		tarefa = threading.Thread(target=changeColor)
		tarefa.daemon = True
		tarefa.start()


def main(ui):

	def escolherCategoria():
		category = ui.lineEdit_2.text()
		print("Texto:", category)

	def a():
		
		def create_socket():
			def oi():
				print("Hello")

			category = ""
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
			        while category == "":
			        	time.sleep(10)
			        	category = ui.lineEdit_2.text()
			        	print(ui.lineEdit_2.text(), ui.comboBox.currentText())
			        print("Saiu do loop")
			        client.send(category.encode())
			        print("esperando conexão de outros jogadores")
			    else:
			    	ui.tela_escolha  
			        
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


		#print("1----- ",ui.lineEdit_2.text())
		#ui.label_2.setText("olafasdf sadf a")
		tarefa_principal = threading.Thread(target=create_socket)
		tarefa_principal.daemon = True
		tarefa_principal.start()

	ui.criar.clicked.connect(a)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    main(ui)
    sys.exit(app.exec_())