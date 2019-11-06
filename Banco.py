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
                sql = "SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial,PrecoUnitario,Quantidade FROM Produto,DadosDaLoja ON DadosDaLoja.IdentificadorLoja = {0} GROUP BY SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            if id_loja == None and NomeDoProduto != None:
                sql = "SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial,PrecoUnitario,Quantidade FROM Produto JOIN DadosDaLoja ON Produto.NomeDoProduto = {0} GROUP BY IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(NomeDoProduto)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            else:
                sql = "SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial,PrecoUnitario,Quantidade FROM Produto JOIN DadosDaLoja ON Produto.NomeDoProduto = {0} AND DadosDaLoja.IdentificadorLoja = {1} GROUP BY IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(NomeDoProduto,id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
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
    def ExcluiLoja(self,NomeDaFilial):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "DELETE FROM DadosDaLoja WHERE NomeDaFilial = '{0}'".format(NomeDaFilial)
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
            return NomeDaFilial
        except Exception as e:
            return False
    def AlterarDadosDaLoja(self,NomeDaFilial,id_loja,NomeDaRua,Bairro,Numero,CEP):
        self.ExcluiLoja(NomeDaFilial)
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql1 = "UPDATE DadosDaLoja SET NomeDaFilial = '{0}' WHERE IdentificadorLoja = '{1}'".format(NomeDaFilial,id_loja)
            executar.execute(sql1)
            sql2 = "UPDATE EnderecoLoja SET NomeDaRua = '{0}', Bairro = '{1}', Numero = {2}, CEP = '{3}' WHERE IdentificadorLoja = '{4}'".format(NomeDaRua,Bairro,Numero,CEP,id_loja)
            executar.execute(sql2)
            conexao.commit()
            conexao.close()
        except Exception as e:
            raise
    def ExcluiProduto(self,NomeDoProduto):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "DELETE FROM Produto WHERE NomeDoProduto = '{0}'".format(NomeDoProduto)
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
            return NomeDaFilial
        except Exception as e:
            return False
    def AlterarDadosDoProduto(self,NomeDoProduto,Quantidade,PrecoUnitario,IdentificadorProduto):
        self.ExcluiLoja(NomeDaFilial)
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql1 = "UPDATE Produto SET NomeDoProduto = '{0}',Quantidade = {1}, PrecoUnitario = {2} WHERE IdentificadorProduto = {3}".format(NomeDoProduto,Quantidade,PrecoUnitario,IdentificadorProduto)
            executar.execute(sql1)
            conexao.commit()
            conexao.close()
        except Exception as e:
            raise
    def BuscaFuncionario(self,CPF):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT *FROM Funcionario WHERE CPF = '{0}'".format(CPF)
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
            return resultado.fetchall()
        except Exception as e:
            return False
    def AlteraFuncionario(self,NomeDoFuncionario,CPF,NumeroDeTelefone,Senha,IdentificadorLoja):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "UPDATE Funcionario SET NomeDoFuncionario = '{0}', NumeroDeTelefone = '{1}', Senha = '{2}', IdentificadorLoja = {3} WHERE CPF = '{4}'".format(NomeDoFuncionario,NumeroDeTelefone,Senha,IdentificadorLoja,CPF)
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            return False
    def ExcluiFuncionario(self,CPF):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "DELETE FROM Funcionario WHERE CPF = '{0}'".format(CPF)
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            return False
    def Login(self,CPF,Senha):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT *FROM Funcionario WHERE CPF = '{0}', Senha = '{1}'".format(CPF,Senha)
            resultado = executar.execute(sql)
            teste = resultado.fetchall()
            conexao.commit()
            conexao.close()
            return teste[0][0]
        except Exception as e:
            return False
    def Vender(self,CPF):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = ""
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            return False
