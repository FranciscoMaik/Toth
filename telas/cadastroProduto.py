# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroProduto.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import globalServer

class Ui_tela_cad_prod(object):
    def setupUi(self, tela_cad_prod):
        tela_cad_prod.setObjectName("tela_cad_prod")
        tela_cad_prod.resize(1180, 857)
        tela_cad_prod.setAutoFillBackground(False)
        tela_cad_prod.setStyleSheet("")
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
        self.btn_cad_prod.setGeometry(QtCore.QRect(480, 440, 111, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cad_prod.setFont(font)
        self.btn_cad_prod.setStyleSheet("")
        self.btn_cad_prod.setObjectName("btn_cad_prod")
        self.btn_cancel_prod = QtWidgets.QPushButton(self.frame_3)
        self.btn_cancel_prod.setGeometry(QtCore.QRect(60, 440, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cancel_prod.setFont(font)
        self.btn_cancel_prod.setStyleSheet("")
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
        self.btn_buscar_prod = QtWidgets.QPushButton(self.frame_3)
        self.btn_buscar_prod.setGeometry(QtCore.QRect(200, 440, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_buscar_prod.setFont(font)
        self.btn_buscar_prod.setStyleSheet("")
        self.btn_buscar_prod.setObjectName("btn_buscar_prod")
        self.btn_alterar_prod = QtWidgets.QPushButton(self.frame_3)
        self.btn_alterar_prod.setGeometry(QtCore.QRect(340, 440, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_alterar_prod.setFont(font)
        self.btn_alterar_prod.setStyleSheet("")
        self.btn_alterar_prod.setObjectName("btn_alterar_prod")
        self.btn_excluir_produto = QtWidgets.QPushButton(self.frame_3)
        self.btn_excluir_produto.setGeometry(QtCore.QRect(640, 440, 111, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_excluir_produto.setFont(font)
        self.btn_excluir_produto.setStyleSheet("")
        self.btn_excluir_produto.setObjectName("btn_excluir_produto")
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
        self.btn_cancel_prod.setText(_translate("tela_cad_prod", "Cancelar"))
        self.label_6.setText(_translate("tela_cad_prod", "Loja"))
        self.btn_buscar_prod.setText(_translate("tela_cad_prod", "Buscar"))
        self.btn_alterar_prod.setText(_translate("tela_cad_prod", "Alterar"))
        self.btn_excluir_produto.setText(_translate("tela_cad_prod", "Excluir"))
        self.label_3.setText(_translate("tela_cad_prod", "Nome"))
        self.label_10.setText(_translate("tela_cad_prod", "Cadastro de Produto"))
        self.btn_voltar_prod.setText(_translate("tela_cad_prod", "Voltar"))

        self.funcionalidades()

    def funcionalidades(self):
        self.btn_cad_prod.clicked.connect(self.cadastrarProduto)
        self.btn_cancel_prod.clicked.connect(self.cancelarProduto)
        self.btn_buscar_prod.clicked.connect(self.buscarProduto)
        self.btn_alterar_prod.clicked.connect(self.alterarValoresProduto)
        self.btn_excluir_produto.clicked.connect(self.excluirProduto)

    def cadastrarProduto(self):
        nome = self.txt_nome_prod_prod.toPlainText()
        quantidade = str(self.sb_quant_prod.value())
        preco = str(self.dsp_preco_prod.value())
        loja = str(self.sb_id_loja_prod.value())
        print(loja,type(loja))

        ip = globalServer.ip
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        if globalServer.conectado == False:
            QtWidgets.QMessageBox.about(None, 'Produto', "Servidor não conectado, por favor vá a página Acesso e para conecá-lo!")
        else:
            if (nome == "" or quantidade == '0' or preco == '0.0' or loja == '0'):
                QtWidgets.QMessageBox.about(None, "Produto", "Algum campo está vazio, por favor preencher para cadastrar o produto!")
            else:
                a = "Produto," + nome + "," + quantidade + "," + preco + "," + loja
                client_socket.send(a.encode())
                mensagem_recebida = client_socket.recv(1024).decode()
                rec = mensagem_recebida.split()
                QtWidgets.QMessageBox.about(None, "Produto",mensagem_recebida)
            client_socket.close()

        self.cancelarProduto()

    def cancelarProduto(self):
        self.txt_nome_prod_prod.setText("")
        self.sb_quant_prod.setValue(0)
        self.sb_id_loja_prod.setValue(0)
        self.dsp_preco_prod.setValue(0.0)

    def buscarProduto(self):
        nome = self.txt_nome_prod_prod.toPlainText()
        loja = str(self.sb_id_loja_prod.value())

        if globalServer.conectado == False:
            QtWidgets.QMessageBox.about(None, 'Produto', "Servidor não conectado, por favor vá a página Acesso e para conecá-lo!")
        else:
            if(nome == '' or loja =='0'):
                QtWidgets.QMessageBox.about(None,'Produto','Por favor preencher o nome e Id da Loja para buscar o Produto')

            elif(nome != '' and loja != '0'):
                ip = globalServer.ip
                port = 7000
                addr = ((ip, port))
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(addr)

                a = "buscarProduto," + nome + "," + loja

                client_socket.send(a.encode())
                mensagem_recebida = client_socket.recv(1024).decode()
                rec = mensagem_recebida.split(',')
                if "prodexiste" == str(rec[0]):
                    #IdentificadorProduto,NomeDoProduto,NomeDaFilial,PrecoUnitario,Quantidade
                    self.txt_nome_prod_prod.setText(rec[2])
                    self.sb_quant_prod.setValue(int(rec[5]))
                    self.dsp_preco_prod.setValue(float(rec[4]))
                elif "prodnoexiste" == str(rec[0]):
                    QtWidgets.QMessageBox.about(None, "Produto", "O produto solicitado não foi encontrado nesta loja")
                elif "lojanoexiste" == str(rec[0]):
                    QtWidgets.QMessageBox.about(None, "Produto", "A loja na qual buscou o produto não existe, por favor pesquise em uma loja existente")
                client_socket.close()

    def alterarValoresProduto(self):
        nome = self.txt_nome_prod_prod.toPlainText()
        quantidade = str(self.sb_quant_prod.value())
        preco = str(self.dsp_preco_prod.value())
        loja = str(self.sb_id_loja_prod.value())

        ip = globalServer.ip
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        a = "alterarValoresdoProduto," + nome + "," + quantidade + "," + preco + "," + loja

        client_socket.send(a.encode())
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Produto", mensagem_recebida)
        client_socket.close()

        self.cancelarProduto()

    def excluirProduto(self):
        nome = self.txt_nome_prod_prod.toPlainText()
        loja = str(self.sb_id_loja_prod.value())

        if globalServer.conectado == False:
            QtWidgets.QMessageBox.about(None, 'Produto', "Servidor não conectado, por favor vá a página Acesso e para conecá-lo!")

        else:
            if (nome == '' or loja == '0'):
                QtWidgets.QMessageBox.about(None, 'Produto',
                                            'Por favor preencher o nome e Id da Loja para excluir o Produto')
            if(nome != '' and loja != '0'):
                ip = globalServer.ip
                port = 7000
                addr = ((ip, port))
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(addr)

                a = "excluirProduto,"+nome + ',' + loja

                client_socket.send(a.encode())
                mensagem_recebida = client_socket.recv(1024).decode()
                QtWidgets.QMessageBox.about(None, "Produto", mensagem_recebida)
                client_socket.close()

                self.cancelarProduto()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_cad_prod = QtWidgets.QDialog()
    ui = Ui_tela_cad_prod()
    ui.setupUi(tela_cad_prod)
    tela_cad_prod.showMaximized()
    sys.exit(app.exec_())

