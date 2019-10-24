import sqlite3
class Banco:
    def __init__(self):
        pass
    def Funcionario(self,NomeFuncionario,CPF,NumeroDeTelefone,Endereco):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Funcionario VALUES ('"+NomeFuncionario+"','"+CPF+"','"+NumeroDeTelefone+"','"+Endereco+"')"
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def Produto(self,NomeDoProduto,Quantidade,Identificador,PrecoUnitario):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Produto VALUES ('{0}',{1},{2},{3})".format(NomeDoProduto,Quantidade,Identificador,PrecoUnitario)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def Endereco(self,NomeDaRua,Bairro,Numero,CEP):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Endereco VALUES ('{0}','{1}',{2},'{3}')".format(NomeDaRua,Bairro,Numero,CEP)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def DadosDaLoja(self,NomeDaFilial,EnderecoDaFilial):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO DadosDaLoja VALUES ('{0}','{1}')".format(NomeDaFilial,EnderecoDaFilial)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            raise

Banco().Funcionario("Maik","06121129344","665622","meu endereço")


