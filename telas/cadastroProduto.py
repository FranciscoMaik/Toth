# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroProduto.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import socket
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_cad_prod(object):
    def setupUi(self, tela_cad_prod):
        tela_cad_prod.setObjectName("tela_cad_prod")
        tela_cad_prod.resize(1180, 857)
        tela_cad_prod.setAutoFillBackground(False)
        tela_cad_prod.setStyleSheet("#tela_cad_prod{\n"
"background-color: qlineargradient(spread:pad, x1:0.095, y1:0.903, x2:0.994, y2:0.0113636, stop:0 rgba(123, 91, 255, 255), stop:0.716418 rgba(22, 47, 168, 255));\n"
"}")
        self.frame_3 = QtWidgets.QFrame(tela_cad_prod)
        self.frame_3.setGeometry(QtCore.QRect(150, 50, 901, 581))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(60, 270, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.sb_quant_prod = QtWidgets.QSpinBox(self.frame_3)
        self.sb_quant_prod.setGeometry(QtCore.QRect(310, 190, 371, 31))
        self.sb_quant_prod.setMaximum(100000)
        self.sb_quant_prod.setObjectName("sb_quant_prod")
        self.dsp_preco_prod = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dsp_preco_prod.setGeometry(QtCore.QRect(310, 260, 371, 31))
        self.dsp_preco_prod.setMaximum(99999.99)
        self.dsp_preco_prod.setObjectName("dsp_preco_prod")
        self.btn_cad_prod = QtWidgets.QPushButton(self.frame_3)
        self.btn_cad_prod.setGeometry(QtCore.QRect(550, 430, 98, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cad_prod.setFont(font)
        self.btn_cad_prod.setStyleSheet("#btn_cad_prod{\n"
"background-color:rgb(0, 197, 0);\n"
"color:#ffffff\n"
"}")
        self.btn_cad_prod.setObjectName("btn_cad_prod")
        self.btn_cancel_prod = QtWidgets.QPushButton(self.frame_3)
        self.btn_cancel_prod.setGeometry(QtCore.QRect(280, 430, 89, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cancel_prod.setFont(font)
        self.btn_cancel_prod.setStyleSheet("#btn_cancel_prod{\n"
"background-color:rgb(208, 0, 0);\n"
"color:#ffffff\n"
"}")
        self.btn_cancel_prod.setObjectName("btn_cancel_prod")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(60, 350, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sb_id_loja_prod = QtWidgets.QSpinBox(self.frame_3)
        self.sb_id_loja_prod.setGeometry(QtCore.QRect(310, 350, 371, 31))
        self.sb_id_loja_prod.setMaximum(1000)
        self.sb_id_loja_prod.setObjectName("sb_id_loja_prod")
        self.txt_nome_prod_prod = QtWidgets.QTextEdit(self.frame_3)
        self.txt_nome_prod_prod.setGeometry(QtCore.QRect(310, 100, 371, 31))
        self.txt_nome_prod_prod.setObjectName("txt_nome_prod_prod")
        self.label_3 = QtWidgets.QLabel(tela_cad_prod)
        self.label_3.setGeometry(QtCore.QRect(210, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(tela_cad_prod)
        self.label_10.setGeometry(QtCore.QRect(470, 50, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.btn_voltar_prod = QtWidgets.QPushButton(tela_cad_prod)
        self.btn_voltar_prod.setGeometry(QtCore.QRect(30, 30, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_voltar_prod.setFont(font)
        self.btn_voltar_prod.setObjectName("btn_voltar_prod")

        self.retranslateUi(tela_cad_prod)
        QtCore.QMetaObject.connectSlotsByName(tela_cad_prod)


    def retranslateUi(self, tela_cad_prod):
        _translate = QtCore.QCoreApplication.translate
        tela_cad_prod.setWindowTitle(_translate("tela_cad_prod", "Dialog"))
        self.label_4.setText(_translate("tela_cad_prod", "Quantidade"))
        self.label_5.setText(_translate("tela_cad_prod", "Preço"))
        self.btn_cad_prod.setText(_translate("tela_cad_prod", "Cadastrar"))
        self.btn_cancel_prod.setText(_translate("tela_cad_prod", "Limpar"))
        self.label_6.setText(_translate("tela_cad_prod", "Loja"))
        self.label_3.setText(_translate("tela_cad_prod", "Nome"))
        self.label_10.setText(_translate("tela_cad_prod", "Cadastro de Produto"))
        self.btn_voltar_prod.setText(_translate("tela_cad_prod", "Voltar"))

        self.funcionalidades()

    def funcionalidades(self):
        #click de botões
        self.btn_cad_prod.clicked.connect(self.conectarServer)
        self.btn_cancel_prod.clicked.connect(self.limpar)

    def limpar(self):
        self.txt_nome_prod_prod.setText("")
        self.sb_quant_prod.setValue(0)
        self.dsp_preco_prod.setValue(0.00)

    def conectarServer(self):
        nome = self.txt_nome_prod_prod.toPlainText()
        quantidade = self.sb_quant_prod.text()
        valor = self.dsp_preco_prod.text()
        ip = '127.0.0.1'
        port = 7000
        addr = ((ip,port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        a = "Produto"
        mensagem_total = a + "," + nome + "," + quantidade + "," + valor
        client_socket.send((mensagem_total.encode()))
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Produto", mensagem_recebida)
        client_socket.close()

        self.txt_nome_prod_prod.setText("")
        self.sb_quant_prod.setValue(0)
        self.dsp_preco_prod.setValue(0.00)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_cad_prod = QtWidgets.QDialog()
    ui = Ui_tela_cad_prod()
    ui.setupUi(tela_cad_prod)
    tela_cad_prod.show()
    sys.exit(app.exec_())
