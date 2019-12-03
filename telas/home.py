# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import socket
import time
import globalServer
import threading
class Ui_ui_home(object):
    def setupUi(self, ui_home):
        ui_home.setObjectName("ui_home")
        ui_home.resize(1180, 814)
        ui_home.setAutoFillBackground(False)
        self.grafico = QtWidgets.QTabWidget(ui_home)
        self.grafico.setEnabled(True)
        self.grafico.setGeometry(QtCore.QRect(0, 0, 1191, 861))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.grafico.setFont(font)
        self.grafico.setMouseTracking(False)
        self.grafico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grafico.setObjectName("grafico")
        self.pagina_inicial = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(14)
        self.pagina_inicial.setFont(font)
        self.pagina_inicial.setStyleSheet("")
        self.pagina_inicial.setObjectName("pagina_inicial")
        self.label = QtWidgets.QLabel(self.pagina_inicial)
        self.label.setGeometry(QtCore.QRect(80, 80, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_cadastrar_loja = QtWidgets.QPushButton(self.pagina_inicial)
        self.btn_cadastrar_loja.setEnabled(True)
        self.btn_cadastrar_loja.setGeometry(QtCore.QRect(80, 140, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.btn_cadastrar_loja.setFont(font)
        self.btn_cadastrar_loja.setMouseTracking(False)
        self.btn_cadastrar_loja.setStyleSheet("")
        self.btn_cadastrar_loja.setObjectName("btn_cadastrar_loja")
        self.btn_cadastrar_funcionario = QtWidgets.QPushButton(self.pagina_inicial)
        self.btn_cadastrar_funcionario.setGeometry(QtCore.QRect(80, 190, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.btn_cadastrar_funcionario.setFont(font)
        self.btn_cadastrar_funcionario.setStyleSheet("")
        self.btn_cadastrar_funcionario.setObjectName("btn_cadastrar_funcionario")
        self.btn_cadastrar_produto = QtWidgets.QPushButton(self.pagina_inicial)
        self.btn_cadastrar_produto.setGeometry(QtCore.QRect(80, 240, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.btn_cadastrar_produto.setFont(font)
        self.btn_cadastrar_produto.setStyleSheet("")
        self.btn_cadastrar_produto.setObjectName("btn_cadastrar_produto")
        self.label_2 = QtWidgets.QLabel(self.pagina_inicial)
        self.label_2.setGeometry(QtCore.QRect(790, 50, 231, 61))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_atualizar_dia = QtWidgets.QPushButton(self.pagina_inicial)
        self.btn_atualizar_dia.setGeometry(QtCore.QRect(810, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.btn_atualizar_dia.setFont(font)
        self.btn_atualizar_dia.setObjectName("btn_atualizar_dia")
        self.btn_atualizar_mes = QtWidgets.QPushButton(self.pagina_inicial)
        self.btn_atualizar_mes.setGeometry(QtCore.QRect(970, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.btn_atualizar_mes.setFont(font)
        self.btn_atualizar_mes.setObjectName("btn_atualizar_mes")
        self.btn_atualizar = QtWidgets.QPushButton(self.pagina_inicial)
        self.btn_atualizar.setGeometry(QtCore.QRect(650, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.btn_atualizar.setFont(font)
        self.btn_atualizar.setObjectName("btn_atualizar")
        self.gridLayoutWidget = QtWidgets.QWidget(self.pagina_inicial)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(660, 310, 471, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_loja_conect = QtWidgets.QLabel(self.pagina_inicial)
        self.lb_loja_conect.setGeometry(QtCore.QRect(1090, 750, 67, 17))
        self.lb_loja_conect.setText("")
        self.lb_loja_conect.setObjectName("lb_loja_conect")
        self.data_inicial = QtWidgets.QDateEdit(self.pagina_inicial)
        self.data_inicial.setGeometry(QtCore.QRect(660, 226, 131, 31))
        self.data_inicial.setObjectName("data_inicial")
        self.date_final = QtWidgets.QDateEdit(self.pagina_inicial)
        self.date_final.setGeometry(QtCore.QRect(830, 226, 131, 31))
        self.date_final.setObjectName("date_final")
        self.label_3 = QtWidgets.QLabel(self.pagina_inicial)
        self.label_3.setGeometry(QtCore.QRect(660, 170, 191, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.grafico.addTab(self.pagina_inicial, "")
        self.buscar_loja = QtWidgets.QWidget()
        self.buscar_loja.setStyleSheet("")
        self.buscar_loja.setObjectName("buscar_loja")
        self.label_25 = QtWidgets.QLabel(self.buscar_loja)
        self.label_25.setGeometry(QtCore.QRect(540, 110, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.buscar_loja)
        self.label_26.setGeometry(QtCore.QRect(350, 200, 161, 27))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.buscar_loja)
        self.label_27.setGeometry(QtCore.QRect(350, 260, 141, 27))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.cb_nome_filial = QtWidgets.QCheckBox(self.buscar_loja)
        self.cb_nome_filial.setGeometry(QtCore.QRect(271, 210, 16, 16))
        self.cb_nome_filial.setText("")
        self.cb_nome_filial.setObjectName("cb_nome_filial")
        self.cb_id_loja = QtWidgets.QCheckBox(self.buscar_loja)
        self.cb_id_loja.setGeometry(QtCore.QRect(271, 271, 16, 16))
        self.cb_id_loja.setText("")
        self.cb_id_loja.setObjectName("cb_id_loja")
        self.txt_nome_filial = QtWidgets.QLineEdit(self.buscar_loja)
        self.txt_nome_filial.setGeometry(QtCore.QRect(540, 200, 311, 33))
        self.txt_nome_filial.setStyleSheet("#txt_nome_filial{\n"
"border-radius: 5px;\n"
"}")
        self.txt_nome_filial.setObjectName("txt_nome_filial")
        self.frame = QtWidgets.QFrame(self.buscar_loja)
        self.frame.setGeometry(QtCore.QRect(229, 90, 741, 301))
        self.frame.setStyleSheet("#frame{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_limpar_tabela_home = QtWidgets.QPushButton(self.frame)
        self.btn_limpar_tabela_home.setGeometry(QtCore.QRect(100, 250,150,31))
        self.btn_buscar_loja = QtWidgets.QPushButton(self.frame)
        self.btn_buscar_loja.setGeometry(QtCore.QRect(620, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.btn_buscar_loja.setFont(font)
        self.btn_buscar_loja.setStyleSheet("#btn_buscar_loja{\n"
"background-color:rgb(138, 226, 52);\n"
"border-radius: 5px;\n"
"}")
        self.btn_buscar_loja.setObjectName("btn_buscar_loja")
        self.btn_limpar_tabela_home.setFont(font)
        self.btn_limpar_tabela_home.setStyleSheet("#btn_limpar_tabela_home{\n"
                                           "background-color:rgb(138, 226, 52);\n"
                                           "border-radius: 5px;\n"
                                           "}")
        self.btn_limpar_tabela_home.setObjectName("btn_limpar_tabela_home")
        self.sb_id_loja = QtWidgets.QSpinBox(self.frame)
        self.sb_id_loja.setGeometry(QtCore.QRect(310, 170, 311, 41))
        self.sb_id_loja.setStyleSheet("#sb_id_loja{\n"
"border-radius: 5px;\n"
"}")
        self.sb_id_loja.setMaximum(1000)
        self.sb_id_loja.setObjectName("sb_id_loja")
        self.label_28 = QtWidgets.QLabel(self.buscar_loja)
        self.label_28.setGeometry(QtCore.QRect(231, 431, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.buscar_loja)
        self.label_29.setGeometry(QtCore.QRect(484, 431, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.tableLojas = QtWidgets.QTableWidget(self.buscar_loja)
        self.tableLojas.setGeometry(QtCore.QRect(230, 490, 741, 192))
        self.tableLojas.setObjectName("tableLojas")
        self.label_28.raise_()
        self.label_29.raise_()
        self.frame.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.cb_nome_filial.raise_()
        self.cb_id_loja.raise_()
        self.txt_nome_filial.raise_()
        self.tableLojas.raise_()
        self.grafico.addTab(self.buscar_loja, "")
        self.ver_estoque = QtWidgets.QWidget()
        self.ver_estoque.setStyleSheet("")
        self.ver_estoque.setObjectName("ver_estoque")
        self.label_19 = QtWidgets.QLabel(self.ver_estoque)
        self.label_19.setGeometry(QtCore.QRect(280, 110, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.cb_nome_prod_estoque = QtWidgets.QCheckBox(self.ver_estoque)
        self.cb_nome_prod_estoque.setGeometry(QtCore.QRect(251, 79, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.cb_nome_prod_estoque.setFont(font)
        self.cb_nome_prod_estoque.setText("")
        self.cb_nome_prod_estoque.setObjectName("cb_nome_prod_estoque")
        self.label_20 = QtWidgets.QLabel(self.ver_estoque)
        self.label_20.setGeometry(QtCore.QRect(280, 70, 191, 24))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.cb_id_loja_estoque = QtWidgets.QCheckBox(self.ver_estoque)
        self.cb_id_loja_estoque.setGeometry(QtCore.QRect(250, 120, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.cb_id_loja_estoque.setFont(font)
        self.cb_id_loja_estoque.setText("")
        self.cb_id_loja_estoque.setObjectName("cb_id_loja_estoque")
        self.frame_2 = QtWidgets.QFrame(self.ver_estoque)
        self.frame_2.setGeometry(QtCore.QRect(170, 40, 931, 171))
        self.frame_2.setStyleSheet("#frame_2{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.txt_nome_produto_estoque = QtWidgets.QLineEdit(self.frame_2)
        self.txt_nome_produto_estoque.setGeometry(QtCore.QRect(310, 30, 431, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.txt_nome_produto_estoque.setFont(font)
        self.txt_nome_produto_estoque.setStyleSheet("#txt_nome_produto_estoque{\n"
"border-radius: 5px;\n"
"}")
        self.txt_nome_produto_estoque.setObjectName("txt_nome_produto_estoque")
        self.sb_id_loja_estoque = QtWidgets.QSpinBox(self.frame_2)
        self.sb_id_loja_estoque.setGeometry(QtCore.QRect(310, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.sb_id_loja_estoque.setFont(font)
        self.sb_id_loja_estoque.setStyleSheet("#sb_id_loja_estoque{\n"
"border-radius: 5px;\n"
"}")
        self.sb_id_loja_estoque.setMaximum(1000)
        self.sb_id_loja_estoque.setObjectName("sb_id_loja_estoque")
        self.btn_ver_estoque = QtWidgets.QPushButton(self.frame_2)
        self.btn_ver_estoque.setGeometry(QtCore.QRect(740, 110, 161, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.btn_ver_estoque.setFont(font)
        self.btn_ver_estoque.setStyleSheet("#btn_ver_estoque{\n"
"background-color:rgb(138, 226, 52);\n"
"border-radius: 5px;\n"
"}")
        self.btn_ver_estoque.setObjectName("btn_ver_estoque")
        self.label_21 = QtWidgets.QLabel(self.ver_estoque)
        self.label_21.setGeometry(QtCore.QRect(171, 251, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.ver_estoque)
        self.label_22.setGeometry(QtCore.QRect(320, 250, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.ver_estoque)
        self.label_23.setGeometry(QtCore.QRect(710, 250, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.ver_estoque)
        self.label_24.setGeometry(QtCore.QRect(910, 250, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.btn_vender_produto = QtWidgets.QPushButton(self.ver_estoque)
        self.btn_vender_produto.setGeometry(QtCore.QRect(960, 660, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_vender_produto.setFont(font)
        self.btn_vender_produto.setObjectName("btn_vender_produto")
        self.tableEstoque = QtWidgets.QTableWidget(self.ver_estoque)
        self.tableEstoque.setGeometry(QtCore.QRect(170, 290, 931, 341))
        self.tableEstoque.setObjectName("tableEstoque")
        self.tableEstoque.horizontalHeader().setCascadingSectionResizes(False)
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.frame_2.raise_()
        self.label_19.raise_()
        self.cb_nome_prod_estoque.raise_()
        self.label_20.raise_()
        self.cb_id_loja_estoque.raise_()
        self.btn_vender_produto.raise_()
        self.tableEstoque.raise_()
        self.grafico.addTab(self.ver_estoque, "")
        self.identificador_loja = QtWidgets.QWidget()
        self.identificador_loja.setStyleSheet("")
        self.identificador_loja.setObjectName("identificador_loja")
        self.label_4 = QtWidgets.QLabel(self.identificador_loja)
        self.label_4.setGeometry(QtCore.QRect(280, 90, 261, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.identificador_loja)
        self.frame_3.setGeometry(QtCore.QRect(210, 80, 771, 301))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.txt_senha_conectada = QtWidgets.QTextEdit(self.frame_3)
        self.txt_senha_conectada.setGeometry(QtCore.QRect(70, 160, 261, 41))
        self.txt_senha_conectada.setStyleSheet("#txt_senha_conectada{\n"
"border-radius: 5px;\n"
"}")
        self.txt_senha_conectada.setObjectName("txt_senha_conectada")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(70, 120, 261, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(70, 40, 261, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(70, 236, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 236, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.txt_cpf_home_login = QtWidgets.QTextEdit(self.frame_3)
        self.txt_cpf_home_login.setGeometry(QtCore.QRect(70, 80, 261, 41))
        self.txt_cpf_home_login.setStyleSheet("#txt_senha_conectada{\n"
"border-radius: 5px;\n"
"}")
        self.txt_cpf_home_login.setObjectName("txt_cpf_home_login")
        self.frame_5 = QtWidgets.QFrame(self.identificador_loja)
        self.frame_5.setGeometry(QtCore.QRect(210, 440, 771, 231))
        self.frame_5.setStyleSheet("#frame_5{\n"
"background-color:rgb(194, 194, 194);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(60, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txt_ip_server = QtWidgets.QTextEdit(self.frame_5)
        self.txt_ip_server.setGeometry(QtCore.QRect(60, 80, 261, 41))
        self.txt_ip_server.setStyleSheet("#txt_senha_conectada{\n"
"border-radius: 5px;\n"
"}")
        self.txt_ip_server.setText("0.0.0.0")
        self.txt_ip_server.setObjectName("txt_ip_server")
        self.btn_conect_server = QtWidgets.QPushButton(self.frame_5)
        self.btn_conect_server.setGeometry(QtCore.QRect(510, 80, 99, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_conect_server.setFont(font)
        self.btn_conect_server.setObjectName("btn_conect_server")
        self.label_6 = QtWidgets.QLabel(self.identificador_loja)
        self.label_6.setGeometry(QtCore.QRect(210, 400, 261, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_3.raise_()
        self.label_4.raise_()
        self.frame_5.raise_()
        self.label_6.raise_()
        self.grafico.addTab(self.identificador_loja, "")

        self.retranslateUi(ui_home)
        self.grafico.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(ui_home)

    def retranslateUi(self, ui_home):
        _translate = QtCore.QCoreApplication.translate
        ui_home.setWindowTitle(_translate("ui_home", "Dialog"))
        self.label.setText(_translate("ui_home", "MENU DE OPÇÕES"))
        self.btn_cadastrar_loja.setText(_translate("ui_home", "Opções da Loja"))
        self.btn_cadastrar_funcionario.setText(_translate("ui_home", "Opções do Funcionário"))
        self.btn_cadastrar_produto.setText(_translate("ui_home", "Opções de Produto"))
        self.label_2.setText(_translate("ui_home", "Gráfico de Compras"))
        self.btn_atualizar_dia.setText(_translate("ui_home", "Do dia"))
        self.btn_atualizar_mes.setText(_translate("ui_home", "Do mês"))
        self.btn_atualizar.setText(_translate("ui_home", "Atualizar"))
        self.label_3.setText(_translate("ui_home", "Período"))
        self.grafico.setTabText(self.grafico.indexOf(self.pagina_inicial), _translate("ui_home", "Página Inicial"))
        self.label_25.setText(_translate("ui_home", "Buscar Loja"))
        self.label_26.setText(_translate("ui_home", "Nome da Filial"))
        self.label_27.setText(_translate("ui_home", "Identificador"))
        self.btn_buscar_loja.setText(_translate("ui_home", "Buscar"))
        self.btn_limpar_tabela_home.setText(_translate("ui_home", "Limpar Tabela"))
        self.label_28.setText(_translate("ui_home", "Id"))
        self.label_29.setText(_translate("ui_home", "Nome"))
        self.grafico.setTabText(self.grafico.indexOf(self.buscar_loja), _translate("ui_home", "Buscar Loja"))
        self.label_19.setText(_translate("ui_home", "Id da Loja"))
        self.label_20.setText(_translate("ui_home", "Nome do Produto"))
        self.btn_ver_estoque.setText(_translate("ui_home", "Ver Estoque"))
        self.label_21.setText(_translate("ui_home", "Id_Produto"))
        self.label_22.setText(_translate("ui_home", "Nome Produto"))
        self.label_23.setText(_translate("ui_home", "Quantidade"))
        self.label_24.setText(_translate("ui_home", "Nome Loja"))
        self.btn_vender_produto.setText(_translate("ui_home", "Vender"))
        self.grafico.setTabText(self.grafico.indexOf(self.ver_estoque), _translate("ui_home", "Ver Estoque"))
        self.label_4.setText(_translate("ui_home", "Funcionario Conetado"))
        self.label_5.setText(_translate("ui_home", "Senha"))
        self.label_8.setText(_translate("ui_home", "CPF"))
        self.pushButton.setText(_translate("ui_home", "LOGIN"))
        self.pushButton_2.setText(_translate("ui_home", "LOGOUT"))
        self.label_7.setText(_translate("ui_home", "Informe o IP do Servidor"))
        self.btn_conect_server.setText(_translate("ui_home", "Conectar"))
        self.label_6.setText(_translate("ui_home", "Conectar ao Servidor"))
        self.grafico.setTabText(self.grafico.indexOf(self.identificador_loja), _translate("ui_home", "Acesso"   ))

        self.funcionalidades()

    def funcionalidades(self):
        """
        Função responsável pela ação do click dos botões e campos de textos.
        :return: Não possuí retorno
        """
        self.btn_conect_server.clicked.connect(self.conectarServer)
        self.txt_nome_filial.setDisabled(True)
        self.sb_id_loja.setDisabled(True)
        self.txt_nome_produto_estoque.setDisabled(True)
        self.sb_id_loja_estoque.setDisabled(True)
        self.cb_id_loja_estoque.clicked.connect(self.estadoDoCheckBox4)
        self.cb_nome_prod_estoque.clicked.connect(self.estadoDoCheckBox3)
        self.cb_nome_filial.clicked.connect(self.estadoDoCheckBox1)
        self.cb_id_loja.clicked.connect(self.estadoDoCheckBox2)
        self.btn_buscar_loja.clicked.connect(self.buscarDadosDasLojas)
        self.btn_ver_estoque.clicked.connect(self.buscarEstoqueProdutos)
        self.pushButton.clicked.connect(self.fazLogin)
        self.pushButton_2.clicked.connect(self.fazLogout)
        self.btn_limpar_tabela_home.clicked.connect(self.loadDadosDasLojasLimpar)


    def loadDadosDasLojasLimpar(self):
        lista = [" "]
        self.loadDadosDasLojas(lista)

    def fazLogout(self):
        if globalServer.Funcionario == False:
            QtWidgets.QMessageBox.about(None,'Home',"Não há nenhum funcionário logado!")
        else:
            nome = globalServer.Funcionario
            globalServer.Funcionario = False
            QtWidgets.QMessageBox.about(None,"Home","Funcionário do CPF "+nome+" desconectado!")
            self.txt_cpf_home_login.setText(" ")
            self.txt_senha_conectada.setText(" ")

    def fazLogin(self):
        #pega os campos de entrada
        cpfentrada = self.txt_cpf_home_login.toPlainText()
        senha = self.txt_senha_conectada.toPlainText()
        message = ''

        if globalServer.Funcionario != False:
            QtWidgets.QMessageBox.about(None,'Home','Há um funcionário conectado!')
        else:
            if globalServer.conectado == False:
                QtWidgets.QMessageBox.about(None,"Home","Servidor não conectado, por favor se conectar ao servidor!")

            else:
                #validação do cpf
                try:
                    soma = 0
                    dgit = 0
                    index = 0
                    if cpfentrada=='' and senha=='':
                        message = 'Informe os campos.'
                        raise ValueError
                    if len(cpfentrada)<11:
                        message = "CPF Inválido"
                        raise ValueError
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
                        message = "CPF Inválido"
                        raise ValueError

                    index = 0
                    soma = 0
                    for x in range(11, 1, -1):
                        soma += x * cpf[index]
                        index += 1

                    dgit = (soma * 10) % 11

                    if dgit == 10:
                        dgit1 = 0

                    if dgit != cpf[10]:
                        message = "CPF Inválido"
                        raise ValueError

                    if senha == '':
                        message += "Por favor, informar a senha!"
                        raise ValueError

                    ip = globalServer.ip
                    port = 7000
                    addr = ((ip, port))
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect(addr)


                    a = "Login," + cpfentrada + "," + senha

                    client_socket.send((a.encode()))
                    mensagem_recebida = client_socket.recv(1024).decode()
                    ver = mensagem_recebida.split(",")
                    if ver[0] == "naoencontrado":
                        QtWidgets.QMessageBox.about(None, "Home", "CPF e Senha não correspondem!")
                    else:
                        globalServer.Funcionario = str(ver[1])
                        QtWidgets.QMessageBox.about(None,"Home","Funcionário Conectado!")
                        self.txt_cpf_home_login.setText("")
                        self.txt_senha_conectada.setText('')

                    client_socket.close()

                except ValueError:

                    QtWidgets.QMessageBox.about(None, "Home", message)
                    self.txt_senha_conectada.setText('')
                    self.txt_cpf_home_login.setText('')


    def buscarEstoqueProdutos(self):
        ip = globalServer.ip
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        nomeProdutoEstoque = None
        idLojaEstoque = "0"
        if globalServer.ip != "":
            QtWidgets.QMessageBox.about(None,'Home','O servidor não está conectado, por favor conectar ao servidor!')
        else:
            if self.cb_nome_prod_estoque.isChecked() == True:
                nomeProdutoEstoque = self.txt_nome_produto_estoque.text()
            else:
                nomeProdutoEstoque = None
            if self.cb_id_loja_estoque.isChecked() == True:
                idLojaEstoque = str(self.sb_id_loja_estoque.value())
            else:
                idLojaEstoque = "0"

            if self.cb_nome_prod_estoque.isChecked() ==  True and nomeProdutoEstoque  == " ":
                QtWidgets.QMessageBox.about(None, "Home", "Caixa de nome selecionada mas está com o campo vazio!")
            else:
                if self.cb_id_loja_estoque.isChecked() == True and idLojaEstoque ==  "0":
                    QtWidgets.QMessageBox.about(None,"Home","Caixa da Identificação da loja selecionada mas o  valor inválido!")
                else:
                    if nomeProdutoEstoque != None and idLojaEstoque == "0":
                        a = "buscarEstoqueHome," + nomeProdutoEstoque + ",vazio"

                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        rec = mensagem_recebida.split(",")[:-1]

                        m = []
                        rec = mensagem_recebida.split(";")[:-1]
                        for i in range(len(rec)):
                            rec2 = rec[i].split(",")[:-1]
                            m.append(rec2)

                        self.loadDadosDoEstoque(m)

                        client_socket.close()

                    elif nomeProdutoEstoque == None and idLojaEstoque != "0":
                        a = "buscarEstoqueHome,vazio," + idLojaEstoque

                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        rec = mensagem_recebida.split(",")[:-1]

                        m = []
                        rec = mensagem_recebida.split(";")[:-1]
                        for i in range(len(rec)):
                            rec2 = rec[i].split(",")[:-1]
                            m.append(rec2)

                        self.loadDadosDoEstoque(m)

                        client_socket.close()

                    elif nomeProdutoEstoque != None and idLojaEstoque != "0":
                        a = "buscarEstoqueHome," + nomeProdutoEstoque + "," + idLojaEstoque

                        client_socket.send((a.encode()))

                        mensagem_recebida = client_socket.recv(1024).decode()

                        rec = mensagem_recebida.split(",")[:-1]

                        m = []
                        rec = mensagem_recebida.split(";")[:-1]
                        for i in range(len(rec)):
                            rec2 = rec[i].split(",")[:-1]
                            m.append(rec2)

                        self.loadDadosDoEstoque(m)

                        client_socket.close()
                    else:
                        a = "buscarEstoqueHome,vazio,vazio"
                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        m = []
                        rec = mensagem_recebida.split(";")[:-1]
                        for i in range(len(rec)):
                            rec2 = rec[i].split(",")[:-1]
                            m.append(rec2)

                        self.loadDadosDoEstoque(m)
                        client_socket.close()

    def loadDadosDoEstoque(self,lista):
        self.tableEstoque.setRowCount(len(lista))
        self.tableEstoque.setColumnCount(len(lista[0]))
        self.tableEstoque.setHorizontalHeaderLabels(
            ["Nome do Produto", "Quantidade", "Id_Produto", "Preço_Uni", "Id_loja"])
        self.tableEstoque.resize(931, 341)


        for i in range(len(lista)):
            for j in range(len(lista[0])):
                self.tableEstoque.setItem(i,j,QTableWidgetItem(lista[i][j]))


    def loadDadosDasLojas(self,lista):
        print(lista)
        self.tableLojas.setRowCount(len(lista))
        self.tableLojas.setColumnCount(len(lista[0]))
        for i in range(len(lista)):
            for j in range(len(lista[0])):
                self.tableLojas.setItem(i,j,QTableWidgetItem(lista[i][j]))



    def buscarDadosDasLojas(self):
        ip = globalServer.ip
        port = 7000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)

        nomeFilialBuscarLoja = None
        identificadorLoja = "0"


        if globalServer.conectado == False:
            QtWidgets.QMessageBox.about(None,"Home","Servidor não conectado, por favor se conectar ao servidor!")

        else:
            if self.cb_nome_filial.isChecked() == True:
                nomeFilialBuscarLoja = self.txt_nome_filial.text()
            else:
                nomeFilialBuscarLoja = None
            if self.cb_id_loja.isChecked() == True:
                identificadorLoja = str(self.sb_id_loja.value())
            else:
                identificadorLoja = "0"

            if self.cb_nome_filial.isChecked() == True and nomeFilialBuscarLoja == "":
                QtWidgets.QMessageBox.about(None, "Home", "Campo texto foi selecionado e esta vazio!")
            else:
                if self.cb_id_loja.isChecked() == True and identificadorLoja == "0":
                    QtWidgets.QMessageBox.about(None, "Home", "Campo  de identificação selecionado mas com valor invalido!")
                else:
                    if nomeFilialBuscarLoja == None and identificadorLoja != "0":
                        print("Caso 1 Nome = null , id = sim")
                        a = "buscarLojaHome," + "vazio," + identificadorLoja

                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        rec = mensagem_recebida.split(",")[:-1]

                        m = [rec]

                        self.loadDadosDasLojas(m)

                        client_socket.close()

                    elif nomeFilialBuscarLoja != None and identificadorLoja == "0":
                        print("Opção dois Nome = Sim, id = não")
                        a = "buscarLojaHome," + nomeFilialBuscarLoja + "," + "vazio"

                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        rec = mensagem_recebida.split(",")[:-1]
                        m = [rec]

                        # for i in range(3):
                        #     m.append(rec[i])


                        self.loadDadosDasLojas(m)

                        client_socket.close()

                    elif nomeFilialBuscarLoja != None and identificadorLoja != "0":
                        print("Opção três Nome = sim , id = sim")
                        a = "buscarLojaHome," + nomeFilialBuscarLoja + "," + identificadorLoja

                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        rec = mensagem_recebida.split(",")

                        m = [rec]

                        self.loadDadosDasLojas(m)

                        client_socket.close()

                    else:
                        print("Opção quatro nome = não, id = não")
                        a = "buscarLojaHome,vazio,vazio"
                        client_socket.send((a.encode()))
                        mensagem_recebida = client_socket.recv(1024).decode()

                        m=[]
                        rec = mensagem_recebida.split(";")[:-1]
                        for i in range(len(rec)):
                            rec2 = rec[i].split(",")[:-1]
                            rec2.reverse()
                            m.append(rec2)

                        self.loadDadosDasLojas(m)
                        client_socket.close()

    def estadoDoCheckBox4(self):
        if self.cb_id_loja_estoque.isChecked() == True:
            self.sb_id_loja_estoque.setDisabled(False)
        else:
            self.sb_id_loja_estoque.setDisabled(True)

    def estadoDoCheckBox3(self):
        if self.cb_nome_prod_estoque.isChecked() == True:
            self.txt_nome_produto_estoque.setDisabled(False)
        else:
            self.txt_nome_produto_estoque.setDisabled(True)

    def estadoDoCheckBox2(self):
        if self.cb_id_loja.isChecked() == True:
            self.sb_id_loja.setDisabled(False)
        else:
            self.sb_id_loja.setDisabled(True)

    def estadoDoCheckBox1(self):
        if self.cb_nome_filial.isChecked() == True:
            self.txt_nome_filial.setDisabled(False)
        else:
            self.txt_nome_filial.setDisabled(True)

    def conectarServer(self):
        ipentrada = self.txt_ip_server.toPlainText()

        if ipentrada == '':
            QtWidgets.QMessageBox.about(None, "Home", "Informar IP do Servidor!")

        ipentrada2 = ipentrada.split('.')
        testado = True
        for i in ipentrada2:
            if i.isdecimal() == True:
                pass
            else:
                testado = False
        if testado == False and ipentrada != '':
            QtWidgets.QMessageBox.about(None, "Home", "informar um IP válido!")

        if(ipentrada != '' and testado == True):
            ip = self.txt_ip_server.toPlainText()
            globalServer.ip = ip
            port = 7000
            addr = ((globalServer.ip, port))
            a = "Criar Cliente,"
            result = [False]
            mensagem_recebida = ['']
            t = threading.Thread(target = self.funcConecta, args = (result,addr,mensagem_recebida,a))
            t.start()
            n = 5
            while n>0 and result[0] == False:
                time.sleep(1)
                n -= 1

            if result[0]==True:
                QtWidgets.QMessageBox.about(None, "Conectar", mensagem_recebida[0])
                globalServer.conectado = True
                self.txt_ip_server.setText('')
            else:
                QtWidgets.QMessageBox.about(None, "Conectar", 'Erro')
                self.txt_ip_server.setText("")

    def funcConecta(self, result,addr, mensagem_recebida,msg='Criar Cliente'):
          client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          client_socket.connect(addr)
          client_socket.send((msg.encode()))
          msg_rec = client_socket.recv(1024).decode()
          mensagem_recebida[0] = msg_rec
          client_socket.close()
          result[0] = True

          # adicionar loja no produto
          # adicionar o endereço
          # tirar id da loja e colocar nome da filial
          # retirar a tela de buscar produto
          # colocar o botão vender no ver estoque
          # colocar nome cpf para a conexão
          # arquivo para ter o ip do server
          # campo senha no cadastro de funcionário
          # logar funcionário
          # tratamento das entradas

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_home = QtWidgets.QDialog()
    ui = Ui_ui_home()
    ui.setupUi(ui_home)
    ui_home.showMaximized()
    sys.exit(app.exec_())

