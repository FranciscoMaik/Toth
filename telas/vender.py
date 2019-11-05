# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vender.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
#import qrcode
import globalServer
import  socket


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 810)
        Form.setStyleSheet("")
        self.ln_id_prod_venda = QtWidgets.QLineEdit(Form)
        self.ln_id_prod_venda.setGeometry(QtCore.QRect(160, 100, 113, 27))
        self.ln_id_prod_venda.setObjectName("ln_id_prod_venda")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sb_quan_prod_venda = QtWidgets.QSpinBox(Form)
        self.sb_quan_prod_venda.setGeometry(QtCore.QRect(170, 250, 48, 27))
        self.sb_quan_prod_venda.setObjectName("sb_quan_prod_venda")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 216, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ln_nome_prod_venda = QtWidgets.QLineEdit(Form)
        self.ln_nome_prod_venda.setGeometry(QtCore.QRect(360, 100, 311, 27))
        self.ln_nome_prod_venda.setObjectName("ln_nome_prod_venda")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(360, 70, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sb_loja_venda = QtWidgets.QSpinBox(Form)
        self.sb_loja_venda.setGeometry(QtCore.QRect(780, 100, 101, 27))
        self.sb_loja_venda.setObjectName("sb_loja_venda")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(780, 70, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_voltar_vender = QtWidgets.QPushButton(Form)
        self.btn_voltar_vender.setGeometry(QtCore.QRect(50, 740, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_voltar_vender.setFont(font)
        self.btn_voltar_vender.setStyleSheet("#btn_voltar_vender{\n"
"background-color: rgb(255, 0, 18);\n"
"}")
        self.btn_voltar_vender.setObjectName("btn_voltar_vender")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(150, 40, 871, 311))
        self.frame.setStyleSheet("#frame{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_vender = QtWidgets.QPushButton(self.frame)
        self.btn_vender.setGeometry(QtCore.QRect(630, 210, 99, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_vender.setFont(font)
        self.btn_vender.setStyleSheet("#btn_vender{\n"
"background-color: rgb(0, 255, 0);\n"
"}")
        self.btn_vender.setObjectName("btn_vender")
        self.qr_code = QtWidgets.QLabel(Form)
        self.qr_code.setGeometry(QtCore.QRect(450, 380, 221, 201))
        self.qr_code.setText("")
        self.qr_code.setObjectName("qr_code")
        self.frame.raise_()
        self.ln_id_prod_venda.raise_()
        self.label.raise_()
        self.sb_quan_prod_venda.raise_()
        self.label_2.raise_()
        self.ln_nome_prod_venda.raise_()
        self.label_3.raise_()
        self.sb_loja_venda.raise_()
        self.label_4.raise_()
        self.btn_voltar_vender.raise_()
        self.qr_code.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ID Produto"))
        self.label_2.setText(_translate("Form", "Quantidade"))
        self.label_3.setText(_translate("Form", "Nome do Produto"))
        self.label_4.setText(_translate("Form", "Loja"))
        self.btn_voltar_vender.setText(_translate("Form", "Voltar"))
        self.btn_vender.setText(_translate("Form", "Vender"))

        self.funcionalidades()

    def funcionalidades(self):
        self.btn_vender.clicked.connect(self.venderProdutos)

    def venderProdutos(self):
        idProduto = self.ln_id_prod_venda.text()
        nomeProduto = self.ln_nome_prod_venda.text()
        idLoja = str(self.sb_loja_venda.value())
        quantidade = str(self.sb_quan_prod_venda.value())

        if(idProduto == '' or idProduto.isdecimal() == False):
            QtWidgets.QMessageBox.about(None, 'Venda','Por favor informar um ID_Produto númerico!')
        if(nomeProduto == ''):
            QtWidgets.QMessageBox.about(None, 'Venda','Por favor informar o Nome do Produto!')
        if(idLoja == '0'):
            QtWidgets.QMessageBox.about(None, 'Venda','Por favor informar um ID_Loja válido!')
        if quantidade == '0':
            QtWidgets.QMessageBox.about(None, 'Venda','Por favor informar uma Quantidade do Produto superior a 0!')


        if(idProduto != '' and idProduto.isdecimal() == True and nomeProduto != '' and idLoja != '0' and quantidade != '0'):
            ip = globalServe.ip
            port = 7000
            addr = ((ip, port))
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)

            #qr = qrcode.make('Id do Produto: ' + idProduto + '\nNome do Produto: ' + nomeProduto + '\nId da Loja: ' + idLoja + '\nQuantidade do Produto: ' + quantidade)
            #qr.save("qrvenda.png")

            pixmap = QPixmap("qrvenda.png")
            pixmap = pixmap.scaled(int(pixmap.width()*0.7), int(pixmap.height()*0.7))
            self.qr_code.setPixmap(pixmap)
            self.qr_code.resize(pixmap.width(), pixmap.height())

            a = "Vender," + idProduto + "," + nomeProduto + "," + idLoja + "," + quantidade

            client_socket.send(a.encode())
            mensagem_recebida = client_socket.recv(1024).decode()
            QtWidgets.QMessageBox.about(None, "Venda", mensagem_recebida)
            client_socket.close()

            self.ln_id_prod_venda.setText('')
            self.ln_nome_prod_venda.setText('')
            self.sb_loja_venda.setValue(0)
            self.sb_quan_prod_venda.setValue(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showMaximized()
    sys.exit(app.exec_())

