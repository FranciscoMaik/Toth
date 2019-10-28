# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroLoja.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket

class Ui_ui_loja(object):
    def setupUi(self, ui_loja):
        ui_loja.setObjectName("ui_loja")
        ui_loja.resize(1180, 857)
        ui_loja.setAutoFillBackground(False)
        ui_loja.setStyleSheet("")
        self.label_8 = QtWidgets.QLabel(ui_loja)
        self.label_8.setGeometry(QtCore.QRect(190, 380, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(ui_loja)
        self.label_11.setGeometry(QtCore.QRect(820, 300, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.frame_3 = QtWidgets.QFrame(ui_loja)
        self.frame_3.setGeometry(QtCore.QRect(100, 250, 971, 271))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.txt_rua_loja = QtWidgets.QTextEdit(self.frame_3)
        self.txt_rua_loja.setGeometry(QtCore.QRect(200, 60, 371, 41))
        self.txt_rua_loja.setObjectName("txt_rua_loja")
        self.txt_bairro_loja = QtWidgets.QTextEdit(self.frame_3)
        self.txt_bairro_loja.setGeometry(QtCore.QRect(200, 120, 371, 41))
        self.txt_bairro_loja.setObjectName("txt_bairro_loja")
        self.txt_cep_loja = QtWidgets.QTextEdit(self.frame_3)
        self.txt_cep_loja.setGeometry(QtCore.QRect(200, 180, 371, 41))
        self.txt_cep_loja.setObjectName("txt_cep_loja")
        self.txt_num_loja = QtWidgets.QTextEdit(self.frame_3)
        self.txt_num_loja.setGeometry(QtCore.QRect(830, 50, 81, 41))
        self.txt_num_loja.setObjectName("txt_num_loja")
        self.label_6 = QtWidgets.QLabel(ui_loja)
        self.label_6.setGeometry(QtCore.QRect(140, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(ui_loja)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(ui_loja)
        self.label_10.setGeometry(QtCore.QRect(420, 50, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(ui_loja)
        self.label_9.setGeometry(QtCore.QRect(190, 440, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(ui_loja)
        self.label_7.setGeometry(QtCore.QRect(190, 320, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btn_cad_loja = QtWidgets.QPushButton(ui_loja)
        self.btn_cad_loja.setGeometry(QtCore.QRect(630, 580, 121, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cad_loja.setFont(font)
        self.btn_cad_loja.setStyleSheet("")
        self.btn_cad_loja.setObjectName("btn_cad_loja")
        self.btn_cancel_loja = QtWidgets.QPushButton(ui_loja)
        self.btn_cancel_loja.setGeometry(QtCore.QRect(100, 580, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cancel_loja.setFont(font)
        self.btn_cancel_loja.setStyleSheet("")
        self.btn_cancel_loja.setObjectName("btn_cancel_loja")
        self.btn_voltar_loja = QtWidgets.QPushButton(ui_loja)
        self.btn_voltar_loja.setGeometry(QtCore.QRect(20, 30, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_voltar_loja.setFont(font)
        self.btn_voltar_loja.setObjectName("btn_voltar_loja")
        self.txt_nome_loja = QtWidgets.QTextEdit(ui_loja)
        self.txt_nome_loja.setGeometry(QtCore.QRect(350, 140, 371, 41))
        self.txt_nome_loja.setObjectName("txt_nome_loja")
        self.btn_buscar_loja = QtWidgets.QPushButton(ui_loja)
        self.btn_buscar_loja.setGeometry(QtCore.QRect(270, 580, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_buscar_loja.setFont(font)
        self.btn_buscar_loja.setStyleSheet("")
        self.btn_buscar_loja.setObjectName("btn_buscar_loja")
        self.btn_alterar_loja = QtWidgets.QPushButton(ui_loja)
        self.btn_alterar_loja.setGeometry(QtCore.QRect(460, 580, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_alterar_loja.setFont(font)
        self.btn_alterar_loja.setStyleSheet("")
        self.btn_alterar_loja.setObjectName("btn_alterar_loja")
        self.btn_exluir__loja = QtWidgets.QPushButton(ui_loja)
        self.btn_exluir__loja.setGeometry(QtCore.QRect(820, 580, 121, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_exluir__loja.setFont(font)
        self.btn_exluir__loja.setStyleSheet("")
        self.btn_exluir__loja.setObjectName("btn_exluir__loja")
        self.frame_3.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_7.raise_()
        self.btn_cad_loja.raise_()
        self.btn_cancel_loja.raise_()
        self.btn_voltar_loja.raise_()
        self.txt_nome_loja.raise_()
        self.btn_buscar_loja.raise_()
        self.btn_alterar_loja.raise_()
        self.btn_exluir__loja.raise_()

        self.retranslateUi(ui_loja)
        QtCore.QMetaObject.connectSlotsByName(ui_loja)

    def retranslateUi(self, ui_loja):
        _translate = QtCore.QCoreApplication.translate
        ui_loja.setWindowTitle(_translate("ui_loja", "Dialog"))
        self.label_8.setText(_translate("ui_loja", "Bairro"))
        self.label_11.setText(_translate("ui_loja", "Número"))
        self.label_6.setText(_translate("ui_loja", "Endereço"))
        self.label_3.setText(_translate("ui_loja", "Nome da Filial"))
        self.label_10.setText(_translate("ui_loja", "Cadastro de Loja"))
        self.label_9.setText(_translate("ui_loja", "CEP"))
        self.label_7.setText(_translate("ui_loja", "Rua"))
        self.btn_cad_loja.setText(_translate("ui_loja", "Cadastrar"))
        self.btn_cancel_loja.setText(_translate("ui_loja", "Cancelar"))
        self.btn_voltar_loja.setText(_translate("ui_loja", "Voltar"))
        self.btn_buscar_loja.setText(_translate("ui_loja", "Buscar"))
        self.btn_alterar_loja.setText(_translate("ui_loja", "Alterar"))
        self.btn_exluir__loja.setText(_translate("ui_loja", "Excluir"))

        self.funcionalidades()

    def funcionalidades(self):
            self.btn_cancel_loja.clicked.connect(self.limparCampos)
            self.btn_cad_loja.clicked.connect(self.cadastrarLoja)
            self.btn_buscar_loja.clicked.connect(self.buscarLoja)
            self.btn_alterar_loja.clicked.connect(self.alterarValores)
            self.btn_exluir__loja.clicked.connect(self.excluirLoja)

    def cadastrarLoja(self):
        nome = self.txt_nome_loja.toPlainText()
        rua = self.txt_rua_loja.toPlainText()
        num = self.txt_num_loja.toPlainText()
        bairro = self.txt_bairro_loja.toPlainText()
        cep = self.txt_cep_loja.toPlainText()

        ip = "127.0.0.1"
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        a = "Loja," + nome + "," + rua + "," + num + "," + bairro + "," + cep

        client_socket.send(a.encode())
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Loja", mensagem_recebida)
        client_socket.close()

        self.limparCampos()

    def limparCampos(self):
        self.txt_nome_loja.setText("")
        self.txt_bairro_loja.setText("")
        self.txt_cep_loja.setText("")
        self.txt_num_loja.setText("")
        self.txt_rua_loja.setText("")

    def buscarLoja(self):
        nome = self.txt_nome_loja.toPlainText()
        rua = self.txt_rua_loja.toPlainText()
        num = self.txt_num_loja.toPlainText()
        bairro = self.txt_bairro_loja.toPlainText()
        cep = self.txt_cep_loja.toPlainText()

        ip = "127.0.0.1"
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        a = "buscarLoja,"

        client_socket.send(a.encode())
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Loja", mensagem_recebida)

        # recebimento das mensagens e setar os campos
        mensagem_recebida = mensagem_recebida.split()

        self.txt_nome_loja.setText("Nome")
        self.txt_bairro_loja.setText("Bairro")
        self.txt_cep_loja.setText("Cep")
        self.txt_num_loja.setText("Num")
        self.txt_rua_loja.setText("Rua")

        client_socket.close()

    def alterarValores(self):
        ip = "127.0.0.1"
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        nome = self.txt_nome_loja.toPlainText()
        rua = self.txt_rua_loja.toPlainText()
        num = self.txt_num_loja.toPlainText()
        bairro = self.txt_bairro_loja.toPlainText()
        cep = self.txt_cep_loja.toPlainText()

        a = "valoresLojaAlterado," + nome + "," + rua + "," + num + "," + bairro + "," + cep

        client_socket.send(a.encode())
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Loja", mensagem_recebida)
        client_socket.close()

        self.limparCampos()

    def excluirLoja(self):
        nome = self.txt_nome_loja.toPlainText()
        rua = self.txt_rua_loja.toPlainText()
        num = self.txt_num_loja.toPlainText()
        bairro = self.txt_bairro_loja.toPlainText()
        cep = self.txt_cep_loja.toPlainText()

        ip = "127.0.0.1"
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        a = "excluirLoja,"

        client_socket.send(a.encode())
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Loja", mensagem_recebida)
        client_socket.close()

        self.limparCampos()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_loja = QtWidgets.QDialog()
    ui = Ui_ui_loja()
    ui.setupUi(ui_loja)
    ui_loja.show()
    sys.exit(app.exec_())

