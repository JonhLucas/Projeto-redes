# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-80, -50, 731, 531))
        self.widget.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 100, 200, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.criar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.criar.setObjectName("criar")
        self.horizontalLayout.addWidget(self.criar)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 170, 501, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.Entrar = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Entrar.setObjectName("Entrar")
        self.horizontalLayout_2.addWidget(self.Entrar)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(-1, -21, 661, 511))
        self.widget_2.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(50, 310, 511, 151))
        self.widget_3.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(40, 50, 311, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.resultado = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.resultado.setObjectName("resultado")
        self.horizontalLayout_3.addWidget(self.resultado)
        self.resultado.raise_()
        self.label_8.raise_()
        self.palpite = QtWidgets.QWidget(self.widget_2)
        self.palpite.setGeometry(QtCore.QRect(50, 50, 511, 411))
        self.palpite.setObjectName("palpite")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.palpite)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 290, 281, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.palpite)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 511, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.Palpites = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Palpites.setObjectName("Palpites")
        self.verticalLayout.addWidget(self.Palpites)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.palpite)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 171, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.Tema = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Tema.setObjectName("Tema")
        self.horizontalLayout_5.addWidget(self.Tema)
        self.tela_escolha = QtWidgets.QWidget(self.widget_2)
        self.tela_escolha.setGeometry(QtCore.QRect(0, 20, 661, 491))
        self.tela_escolha.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.tela_escolha.setObjectName("tela_escolha")
        self.Frutas = QtWidgets.QPushButton(self.tela_escolha)
        self.Frutas.setGeometry(QtCore.QRect(20, 120, 131, 71))
        self.Frutas.setObjectName("Frutas")
        self.Cores = QtWidgets.QPushButton(self.tela_escolha)
        self.Cores.setGeometry(QtCore.QRect(150, 120, 131, 71))
        self.Cores.setObjectName("Cores")
        self.Animais = QtWidgets.QPushButton(self.tela_escolha)
        self.Animais.setGeometry(QtCore.QRect(280, 120, 131, 71))
        self.Animais.setObjectName("Animais")
        self.Paises = QtWidgets.QPushButton(self.tela_escolha)
        self.Paises.setGeometry(QtCore.QRect(410, 120, 131, 71))
        self.Paises.setObjectName("Paises")
        self.label_4 = QtWidgets.QLabel(self.tela_escolha)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 261, 51))
        self.label_4.setObjectName("label_4")
        self.Aguarde = QtWidgets.QWidget(self.centralwidget)
        self.Aguarde.setGeometry(QtCore.QRect(-71, -41, 831, 531))
        self.Aguarde.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.Aguarde.setObjectName("Aguarde")
        self.label_3 = QtWidgets.QLabel(self.Aguarde)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 81, 61))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.Aguarde)
        self.progressBar.setGeometry(QtCore.QRect(120, 200, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget_2.raise_()
        self.Aguarde.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.criar.clicked['bool'].connect(self.widget.hide)
        self.Animais.clicked['bool'].connect(self.tela_escolha.hide)
        self.Frutas.clicked['bool'].connect(self.tela_escolha.hide)
        self.Cores.clicked['bool'].connect(self.tela_escolha.hide)
        self.Paises.clicked['bool'].connect(self.tela_escolha.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
