# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import globalServer

class Ui_fundo_func(object):
    def setupUi(self, fundo_func):
        fundo_func.setObjectName("fundo_func")
        fundo_func.resize(1180, 857)
        fundo_func.setAutoFillBackground(False)
        fundo_func.setStyleSheet("")
        self.label_4 = QtWidgets.QLabel(fundo_func)
        self.label_4.setGeometry(QtCore.QRect(160, 250, 51, 21))
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
        self.label_3.setGeometry(QtCore.QRect(160, 110, 61, 31))
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
        self.btn_cancel_func.setGeometry(QtCore.QRect(110, 770, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cancel_func.setFont(font)
        self.btn_cancel_func.setStyleSheet("")
        self.btn_cancel_func.setObjectName("btn_cancel_func")
        self.btn_cad_func = QtWidgets.QPushButton(fundo_func)
        self.btn_cad_func.setGeometry(QtCore.QRect(680, 770, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cad_func.setFont(font)
        self.btn_cad_func.setStyleSheet("")
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
        self.txt_cpf_func.setGeometry(QtCore.QRect(410, 240, 371, 41))
        self.txt_cpf_func.setObjectName("txt_cpf_func")
        self.txt_nome_func = QtWidgets.QTextEdit(fundo_func)
        self.txt_nome_func.setGeometry(QtCore.QRect(410, 110, 371, 41))
        self.txt_nome_func.setStyleSheet("#txt_nome_func{\n"
"border-radius:10px;\n"
"}")
        self.txt_nome_func.setObjectName("txt_nome_func")
        self.btn_buscar_funcionario = QtWidgets.QPushButton(fundo_func)
        self.btn_buscar_funcionario.setGeometry(QtCore.QRect(300, 770, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_buscar_funcionario.setFont(font)
        self.btn_buscar_funcionario.setStyleSheet("")
        self.btn_buscar_funcionario.setObjectName("btn_buscar_funcionario")
        self.btn_editar_funcionario = QtWidgets.QPushButton(fundo_func)
        self.btn_editar_funcionario.setGeometry(QtCore.QRect(500, 770, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_editar_funcionario.setFont(font)
        self.btn_editar_funcionario.setStyleSheet("")
        self.btn_editar_funcionario.setObjectName("btn_editar_funcionario")
        self.txt_senha_fun = QtWidgets.QTextEdit(fundo_func)
        self.txt_senha_fun.setGeometry(QtCore.QRect(410, 180, 371, 41))
        self.txt_senha_fun.setStyleSheet("#txt_nome_func{\n"
"border-radius:10px;\n"
"}")
        self.txt_senha_fun.setObjectName("txt_senha_fun")
        self.label_13 = QtWidgets.QLabel(fundo_func)
        self.label_13.setGeometry(QtCore.QRect(160, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.btn_excluir_funcionario = QtWidgets.QPushButton(fundo_func)
        self.btn_excluir_funcionario.setGeometry(QtCore.QRect(870, 770, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_excluir_funcionario.setFont(font)
        self.btn_excluir_funcionario.setStyleSheet("")
        self.btn_excluir_funcionario.setObjectName("btn_excluir_funcionario")
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
        self.btn_buscar_funcionario.raise_()
        self.btn_editar_funcionario.raise_()
        self.txt_senha_fun.raise_()
        self.label_13.raise_()
        self.btn_excluir_funcionario.raise_()

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
        self.btn_cancel_func.setText(_translate("fundo_func", "Cancelar"))
        self.btn_cad_func.setText(_translate("fundo_func", "Cadastrar"))
        self.label_12.setText(_translate("fundo_func", "Loja"))
        self.btn_voltar_tela_func.setText(_translate("fundo_func", "Voltar"))
        self.btn_buscar_funcionario.setText(_translate("fundo_func", "Buscar"))
        self.btn_editar_funcionario.setText(_translate("fundo_func", "Alterar"))
        self.label_13.setText(_translate("fundo_func", "Senha"))
        self.btn_excluir_funcionario.setText(_translate("fundo_func", "Excluir"))

        self.funcionalidades()

    def funcionalidades(self):
        self.btn_cad_func.clicked.connect(self.cadastrarFuncionario)
        self.btn_cancel_func.clicked.connect(self.cancelarFuncionario)
        self.btn_buscar_funcionario.clicked.connect(self.buscarFuncionario)
        self.btn_editar_funcionario.clicked.connect(self.alterarValores)
        self.btn_excluir_funcionario.clicked.connect(self.excluirFuncionario)

    def cadastrarFuncionario(self):
        nome = self.txt_nome_func.toPlainText()
        senha = self.txt_senha_fun.toPlainText()
        cpfentrada = self.txt_cpf_func.toPlainText()
        num = self.txt_num_func.toPlainText()
        loja = str(self.sb_id_loja_func.value())
        rua = self.txt_rua_func.toPlainText()
        bairro = self.txt_bairro_func.toPlainText()
        cep = self.txt_cep_func.toPlainText()
        numero_rua = self.txt_num_end_func.toPlainText()

        if globalServer.ip == "":
            QtWidgets.QMessageBox.about(None,"Funcionário","O servidor não está conectado! Por favor vá a página de conexão e se conecte ao servidor!")
        else:
            try:
                soma = 0
                dgit = 0
                index = 0
                validade = True
                a = cpfentrada
                cpf = list()
                for x in a:
                    if x != '.' and x != '-':
                        b = int(x)
                        cpf.append(b)

                for x in range(10, 1, -1):
                    soma += x * cpf[index]
                    index += 1

                dgit = (soma * 10) % 11

                if dgit == 10:
                    dgit = 0

                if dgit != cpf[9]:
                    validade = False
                    exit(1)

                index = 0
                soma = 0
                for x in range(11, 1, -1):
                    soma += x * cpf[index]
                    index += 1

                dgit = (soma * 10) % 11

                if dgit == 10:
                    dgit1 = 0

                if dgit != cpf[10]:
                    validade = False
                    exit(1)



            except:
                QtWidgets.QMessageBox.about(None, "Funcionário", "CPF Inválido")

            if(cep.isdecimal() == False):
                QtWidgets.QMessageBox.about(None,'Cadastro de Funcionário', 'CEP Inválido, por favor colocar somente números!')
            if(num.isdecimal() == False):
                QtWidgets.QMessageBox.about(None, 'Cadastro de Funcionário',
                                            'Número de Telefone Inválido, por favor colocar somente números!')

            if(validade == True and cep.isdecimal() == True and num.isdecimal() == True):
                ip = globalServer.ip
                port = 7000
                addr = ((ip, port))
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(addr)

                a = "Funcionario," + nome + "," + rua + "," + num + "," + bairro + "," + cep + "," + senha + "," + cpfentrada + "," + loja + "," + numero_rua

                client_socket.send(a.encode())
                mensagem_recebida = client_socket.recv(1024).decode()
                QtWidgets.QMessageBox.about(None, "Funcionário", mensagem_recebida)
                client_socket.close()

                self.cancelarFuncionario()
            else:
                QtWidgets.QMessageBox.about(None, 'Cadastro de Funcionário',
                                            'Algum campo está vazio ou inválido, por favor preencha todos os campos!')

    def cancelarFuncionario(self):
        self.txt_num_end_func.setText("")
        self.txt_cep_func.setText("")
        self.txt_bairro_func.setText("")
        self.txt_rua_func.setText("")
        self.txt_num_func.setText("")
        self.txt_cpf_func.setText("")
        self.txt_senha_fun.setText("")
        self.txt_nome_func.setText("")
        self.sb_id_loja_func.setValue(0)

    def buscarFuncionario(self):
        cpfentrada = self.txt_cpf_func.toPlainText()
        if globalServer.ip == "":
            QtWidgets.QMessageBox.about(None, "Funcionário",
                                        "O servidor não está conectado! Por favor vá a página de conexão e se conecte ao servidor!")
        else:
            try:
                soma = 0
                dgit = 0
                index = 0
                validade = True
                a = cpfentrada
                cpf = list()
                for x in a:
                    if x != '.' and x != '-':
                        b = int(x)
                        cpf.append(b)

                for x in range(10, 1, -1):
                    soma += x * cpf[index]
                    index += 1

                dgit = (soma * 10) % 11

                if dgit == 10:
                    dgit = 0

                if dgit != cpf[9]:
                    validade = False
                    exit(1)

                index = 0
                soma = 0
                for x in range(11, 1, -1):
                    soma += x * cpf[index]
                    index += 1

                dgit = (soma * 10) % 11

                if dgit == 10:
                    dgit1 = 0

                if dgit != cpf[10]:
                    validade = False
                    exit(1)

            except:
                if(cpfentrada != ''):
                    QtWidgets.QMessageBox.about(None, "Funcionário", "CPF Inválido")

            if cpfentrada == '':
                QtWidgets.QMessageBox.about(None, "Funcionário", "Por favor, preencher o campo CPF para buscá-lo!")

            if (cpfentrada != '' and validade == True):
                ip = globalServer.ip
                port = 7000
                addr = ((ip, port))
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(addr)

                a = "buscarFuncionario," + cpfentrada

                client_socket.send(a.encode())
                mensagem_recebida = client_socket.recv(1024).decode()

                rec = mensagem_recebida.split(",")
                print(mensagem_recebida)
                if rec[0] == "existe":
                    self.txt_num_end_func.setText("111")
                    self.txt_cep_func.setText("2415")
                    self.txt_bairro_func.setText("centro")
                    self.txt_rua_func.setText("tals")
                    self.txt_num_func.setText("89988020693")
                    self.txt_cpf_func.setText("06121129344")
                    self.txt_senha_fun.setText("estaeasenha")
                    self.txt_nome_func.setText("maik")
                    self.sb_id_loja_func.setValue(32)

                elif rec[0] == "noexiste":
                    QtWidgets.QMessageBox.about(None, "Funcionário", "Não foi possivel encontrar o funcionário!")
                client_socket.close()


    def alterarValores(self):
        nome = self.txt_nome_func.toPlainText()
        senha = self.txt_senha_fun.toPlainText()
        cpf = self.txt_cpf_func.toPlainText()
        num = self.txt_num_func.toPlainText()
        loja = str(self.sb_id_loja_func.value())
        rua = self.txt_rua_func.toPlainText()
        bairro = self.txt_bairro_func.toPlainText()
        cep = self.txt_cep_func.toPlainText()
        numero_rua = self.txt_num_end_func.toPlainText()

        ip = globalServer.ip
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        a = "alterarDadosFuncionario," + nome + "," + rua + "," + num + "," + bairro + "," + cep + "," + senha + "," + cpf + "," + loja + "," + numero_rua

        client_socket.send(a.encode())
        mensagem_recebida = client_socket.recv(1024).decode()
        QtWidgets.QMessageBox.about(None, "Funcionário", mensagem_recebida)
        client_socket.close()

        self.cancelarFuncionario()

    def excluirFuncionario(self):
        cpfentrada = self.txt_cpf_func.toPlainText()

        try:
            soma = 0
            dgit = 0
            index = 0
            validade = True
            a = cpfentrada
            cpf = list()
            for x in a:
                if x != '.' and x != '-':
                    b = int(x)
                    cpf.append(b)

            for x in range(10, 1, -1):
                soma += x * cpf[index]
                index += 1

            dgit = (soma * 10) % 11

            if dgit == 10:
                dgit = 0

            if dgit != cpf[9]:
                validade = False
                exit(1)

            index = 0
            soma = 0
            for x in range(11, 1, -1):
                soma += x * cpf[index]
                index += 1

            dgit = (soma * 10) % 11

            if dgit == 10:
                dgit1 = 0

            if dgit != cpf[10]:
                validade = False
                exit(1)

        except:
            if (cpfentrada != ''):
                QtWidgets.QMessageBox.about(None, "Funcionário", "CPF Inválido")

        if cpfentrada == '':
            QtWidgets.QMessageBox.about(None, "Funcionário", "Por favor, preencher o campo CPF para exclui-lo!")

        if(cpfentrada != '' and validade == True):
            ip = globalServer.ip
            port = 7000
            addr = ((ip, port))
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)

            a = "excluirFuncionario,"

            client_socket.send(a.encode())
            mensagem_recebida = client_socket.recv(1024).decode()
            QtWidgets.QMessageBox.about(None, "Funcionário", mensagem_recebida)
            client_socket.close()

            self.cancelarFuncionario()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fundo_func = QtWidgets.QDialog()
    ui = Ui_fundo_func()
    ui.setupUi(fundo_func)
    fundo_func.showMaximized()
    sys.exit(app.exec_())

