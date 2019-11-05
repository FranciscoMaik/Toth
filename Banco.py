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
            sql2 = "SELECT *FROM Funcionario;"
            ultimoid = executar.execute(sql2)
            id_funcionario = ultimoid.fetchall()
            contador = 0
            for x in id_funcionario:
                contador = contador + 1
            sql3 = "INSERT INTO EnderecoFuncionario VALUES ('{0}','{1}',{2},'{3}',{4})".format(NomeDaRua,Bairro,Numero,CEP,id_funcionario[contador-1][1])
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
    def ProdutoConsulta(self,id_loja,NomeDoProduto):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            if id_loja != None and NomeDoProduto == None:
                sql = "SELECT IdentificadorProduto,NomeDoProduto,QuantomeDaFilidade,Nial FROM Produto,DadosDaLoja ON DadosDaLoja.IdentificadorLoja = {0} GROUP BY SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                return resultado
            if id_loja == None and NomeDoProduto != None:
                sql = "SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial FROM Produto JOIN DadosDaLoja ON Produto.NomeDoProduto = {0} GROUP BY IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(NomeDoProduto)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                return resultado
            else:
                sql = "SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial FROM Produto JOIN DadosDaLoja ON Produto.NomeDoProduto = {0} AND DadosDaLoja.IdentificadorLoja = {1} GROUP BY IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(NomeDoProduto,id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                return resultado
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def LojaConsultaHome(self,id_loja,NomeDaFilial):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            if id_loja != None and NomeDaFilial == None:
                sql = "SELECT IdentificadorLoja,NomeDaFilial FROM DadosDaLoja WHERE IdentificadorLoja = {0}".format(id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                return resultado
            if id_loja == None and NomeDaFilial!= None:
                sql = "SELECT IdentificadorLoja,NomeDaFilial FROM DadosDaLoja WHERE NomeDaFilial = '{0}' ".format(NomeDaFilial)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                return resultado
            else:
                sql = "SELECT IdentificadorLoja,NomeDaFilial FROM DadosDaLoja WHERE NomeDaFilial = '{0}' AND IdentificadorLoja = {1}".format(NomeDaFilial,id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                return resultado
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def LojaConsulta(self,NomeDaFilial):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT NomeDaRua,Bairro,Numero,CEP FROM EnderecoLoja WHERE EnderecoLoja.IdentificadorLoja IN (SELECT DadosDaLoja.IdentificadorLoja FROM DadosDaLoja WHERE DadosDaLoja.NomeDaFilial = '{0}')".format(NomeDaFilial)
            resultado = executar.execute(sql)
            resultado = resultado.fetchall()
            conexao.commit()
            conexao.close()
            return resultado
        except Exception as e:
            return False

