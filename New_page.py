from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QStatusBar

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "Teste"
		self.top = 100
		self.left = 100
		self.width = 800
		self.height= 500

		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
