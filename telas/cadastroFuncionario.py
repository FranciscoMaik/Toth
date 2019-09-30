# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import socket
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fundo_func(object):
    def setupUi(self, fundo_func):
        fundo_func.setObjectName("fundo_func")
        fundo_func.resize(1180, 857)
        fundo_func.setAutoFillBackground(False)
        fundo_func.setStyleSheet("#fundo_func{\n"
"background-color: qlineargradient(spread:pad, x1:0.095, y1:0.903, x2:0.994, y2:0.0113636, stop:0 rgba(123, 91, 255, 255), stop:0.716418 rgba(22, 47, 168, 255));\n"
"}")
        self.label_4 = QtWidgets.QLabel(fundo_func)
        self.label_4.setGeometry(QtCore.QRect(160, 240, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(fundo_func)
        self.label_8.setGeometry(QtCore.QRect(200, 610, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(fundo_func)
        self.label_5.setGeometry(QtCore.QRect(160, 320, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(fundo_func)
        self.label_11.setGeometry(QtCore.QRect(830, 530, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.frame_3 = QtWidgets.QFrame(fundo_func)
        self.frame_3.setGeometry(QtCore.QRect(110, 470, 971, 271))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.txt_rua_func = QtWidgets.QTextEdit(self.frame_3)
        self.txt_rua_func.setGeometry(QtCore.QRect(200, 70, 371, 41))
        self.txt_rua_func.setObjectName("txt_rua_func")
        self.txt_bairro_func = QtWidgets.QTextEdit(self.frame_3)
        self.txt_bairro_func.setGeometry(QtCore.QRect(200, 130, 371, 41))
        self.txt_bairro_func.setObjectName("txt_bairro_func")
        self.txt_cep_func = QtWidgets.QTextEdit(self.frame_3)
        self.txt_cep_func.setGeometry(QtCore.QRect(200, 190, 371, 41))
        self.txt_cep_func.setObjectName("txt_cep_func")
        self.txt_num_end_func = QtWidgets.QTextEdit(self.frame_3)
        self.txt_num_end_func.setGeometry(QtCore.QRect(820, 60, 111, 41))
        self.txt_num_end_func.setObjectName("txt_num_end_func")
        self.label_6 = QtWidgets.QLabel(fundo_func)
        self.label_6.setGeometry(QtCore.QRect(150, 490, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(fundo_func)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(fundo_func)
        self.label_10.setGeometry(QtCore.QRect(420, 50, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(fundo_func)
        self.label_9.setGeometry(QtCore.QRect(200, 670, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(fundo_func)
        self.label_7.setGeometry(QtCore.QRect(200, 550, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btn_cancel_func = QtWidgets.QPushButton(fundo_func)
        self.btn_cancel_func.setGeometry(QtCore.QRect(190, 760, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cancel_func.setFont(font)
        self.btn_cancel_func.setStyleSheet("#btn_cancel_func{\n"
"background-color:rgb(208, 0, 0);\n"
"color:#ffffff\n"
"}")
        self.btn_cancel_func.setObjectName("btn_cancel_func")
        self.btn_cad_func = QtWidgets.QPushButton(fundo_func)
        self.btn_cad_func.setGeometry(QtCore.QRect(830, 760, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cad_func.setFont(font)
        self.btn_cad_func.setStyleSheet("#btn_cad_func{\n"
"background-color:rgb(0, 197, 0);\n"
"color:#ffffff\n"
"}")
        self.btn_cad_func.setObjectName("btn_cad_func")
        self.label_12 = QtWidgets.QLabel(fundo_func)
        self.label_12.setGeometry(QtCore.QRect(160, 400, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.sb_id_loja_func = QtWidgets.QSpinBox(fundo_func)
        self.sb_id_loja_func.setGeometry(QtCore.QRect(410, 390, 371, 41))
        self.sb_id_loja_func.setStyleSheet("#sb_id_loja_func{\n"
"border-radius:5px;\n"
"}")
        self.sb_id_loja_func.setObjectName("sb_id_loja_func")
        self.btn_voltar_tela_func = QtWidgets.QPushButton(fundo_func)
        self.btn_voltar_tela_func.setGeometry(QtCore.QRect(20, 40, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_voltar_tela_func.setFont(font)
        self.btn_voltar_tela_func.setObjectName("btn_voltar_tela_func")
        self.txt_num_func = QtWidgets.QTextEdit(fundo_func)
        self.txt_num_func.setGeometry(QtCore.QRect(410, 320, 371, 41))
        self.txt_num_func.setObjectName("txt_num_func")
        self.txt_cpf_func = QtWidgets.QTextEdit(fundo_func)
        self.txt_cpf_func.setGeometry(QtCore.QRect(410, 230, 371, 41))
        self.txt_cpf_func.setObjectName("txt_cpf_func")
        self.txt_nome_func = QtWidgets.QTextEdit(fundo_func)
        self.txt_nome_func.setGeometry(QtCore.QRect(410, 150, 371, 41))
        self.txt_nome_func.setStyleSheet("#txt_nome_func{\n"
"border-radius:10px;\n"
"}")
        self.txt_nome_func.setObjectName("txt_nome_func")
        self.frame_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_5.raise_()
        self.label_11.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_7.raise_()
        self.btn_cancel_func.raise_()
        self.btn_cad_func.raise_()
        self.label_12.raise_()
        self.sb_id_loja_func.raise_()
        self.btn_voltar_tela_func.raise_()
        self.txt_num_func.raise_()
        self.txt_cpf_func.raise_()
        self.txt_nome_func.raise_()

        self.retranslateUi(fundo_func)
        QtCore.QMetaObject.connectSlotsByName(fundo_func)

    def retranslateUi(self, fundo_func):
        _translate = QtCore.QCoreApplication.translate
        fundo_func.setWindowTitle(_translate("fundo_func", "Dialog"))
        self.label_4.setText(_translate("fundo_func", "CPF"))
        self.label_8.setText(_translate("fundo_func", "Bairro"))
        self.label_5.setText(_translate("fundo_func", "Número de Telefone"))
        self.label_11.setText(_translate("fundo_func", "Número"))
        self.label_6.setText(_translate("fundo_func", "Endereço"))
        self.label_3.setText(_translate("fundo_func", "Nome"))
        self.label_10.setText(_translate("fundo_func", "Cadastro de Funcionário"))
        self.label_9.setText(_translate("fundo_func", "CEP"))
        self.label_7.setText(_translate("fundo_func", "Rua"))
        self.btn_cancel_func.setText(_translate("fundo_func", "Limpar"))
        self.btn_cad_func.setText(_translate("fundo_func", "Cadastrar"))
        self.label_12.setText(_translate("fundo_func", "Loja"))
        self.btn_voltar_tela_func.setText(_translate("fundo_func", "Voltar"))

        self.funcionalidades()

    def funcionalidades(self):
        # click de botões
        self.btn_cad_func.clicked.connect(self.conectarServer)
        self.btn_cancel_func.clicked.connect(self.limpar)

    def limpar(self):
        self.txt_nome_func.setText("")
        self.txt_cpf_func.setText("")
        self.txt_num_func.setText("")
        self.txt_rua_func.setText("")
        self.txt_bairro_func.setText("")
        self.txt_cep_func.setText("")
        self.txt_num_end_func.setText("")

    def conectarServer(self):
        nome_fun = self.txt_nome_func.toPlainText()
        cpf_fun = self.txt_cpf_func.toPlainText()
        num_tel = self.txt_num_func.toPlainText()

        #endereço
        rua = self.txt_rua_func.toPlainText()
        bairro = self.txt_bairro_func.toPlainText()
        cep = self.txt_cep_func.toPlainText()
        num_rua = self.txt_num_end_func.toPlainText()

        ip = '127.0.0.1'
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        a = "Funcionario"
        mensagem_total = a + "," + nome_fun + "," + cpf_fun + "," + num_tel + "," + rua + "," + bairro + "," + cep + "," + num_rua
        client_socket.send((mensagem_total.encode()))
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Funcionário", mensagem_recebida)
        client_socket.close()

        self.txt_nome_func.setText("")
        self.txt_cpf_func.setText("")
        self.txt_num_func.setText("")
        self.txt_rua_func.setText("")
        self.txt_bairro_func.setText("")
        self.txt_cep_func.setText("")
        self.txt_num_end_func.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fundo_func = QtWidgets.QDialog()
    ui = Ui_fundo_func()
    ui.setupUi(fundo_func)
    fundo_func.show()
    sys.exit(app.exec_())
