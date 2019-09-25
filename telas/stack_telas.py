from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QApplication, QTableWidgetItem
from telas.cadastroFuncionario import Ui_fundo_func
from telas.cadastroProduto import Ui_tela_cad_prod
from telas.cadastroLoja import Ui_ui_loja
from telas.home import Ui_ui_home
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200,900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.cadastroFuncionario = Ui_fundo_func()
        self.cadastroFuncionario.setupUi(self.stack0);

        self.cadastroProduto = Ui_tela_cad_prod()
        self.cadastroProduto.setupUi(self.stack1)

        self.cadastroLoja = Ui_ui_loja()
        self.cadastroLoja.setupUi(self.stack2)

        self.home = Ui_ui_home()
        self.home.setupUi(self.stack3)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.home.btn_cadastrar_loja.clicked.connect(self.abrirTelaCadastrarLoja)




    def abrirTelaCadastrarLoja(self):
        self.QtStack.setCurrentIndex(2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec())
