import sqlite3
class Banco:
    def __init__(self):
        pass
    def Funcionario(self,NomeFuncionario,CPF,NumeroDeTelefone,Senha,id_loja,NomeDaRua,Bairro,Numero,CEP):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Funcionario VALUES ('{0}','{1}','{2}','{3}',{4})".format(NomeFuncionario,CPF,NumeroDeTelefone,Senha,id_loja)
            executar.execute(sql)
            sql2 = "SELECT *FROM Funcionario WHERE CPF = (SELECT MAX(CPF) FROM Funcionario);"
            ultimoid = executar.execute(sql2)
            id_funcionario = ultimoid.fetchall()
            sql3 = "INSERT INTO EnderecoFuncionario VALUES ('{0}','{1}',{2},'{3}',{4})".format(NomeDaRua,Bairro,Numero,CEP,id_funcionario[0][1])
            executar.execute(sql3)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def Produto(self,NomeDoProduto,Quantidade,PrecoUnitario,id_loja):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Produto VALUES ('{0}',{1},null,{2},{3})".format(NomeDoProduto,Quantidade,PrecoUnitario,id_loja)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def DadosDaLoja(self,NomeDaFilial,NomeDaRua,Bairro,Numero,CEP):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql1 = "INSERT INTO DadosDaLoja VALUES ('{0}',null)".format(NomeDaFilial)
            executar.execute(sql1)
            sql2 = "SELECT *FROM DadosDaLoja WHERE IdentificadorLoja = (SELECT MAX(IdentificadorLoja) FROM DadosDaLoja);"
            ultimoid = executar.execute(sql2)
            id_loja = ultimoid.fetchall()
            sql3 = "INSERT INTO EnderecoLoja VALUES ('{0}','{1}',{2},'{3}',{4})".format(NomeDaRua,Bairro,Numero,CEP,id_loja[0][1])
            executar.execute(sql3)
            conexao.commit()
            conexao.close()
        except Exception as e:
            raise
    def Produto(self):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Produto VALUES ('{0}',{1},null,{2},{3})".format(NomeDoProduto,Quantidade,PrecoUnitario,id_loja)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
#Banco().Funcionario("Nathanael","58555","45558985","senha",17,"Rua 0","Junco",855,"Ceep da rua")
#Banco().DadosDaLoja("Perdigao","Rua 0","Junco",855,"Ceep da rua")
#Banco().Produto("Leite",50,55.2,17)
