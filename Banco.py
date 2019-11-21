import sqlite3
class Banco:
    def __init__(self):
        pass
    #Função de cadastro de Funcionário
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
            resultado = executar.execute(sql3)
            conexao.commit()
            conexao.close()
            return resultado
        except Exception as e:
            return []

    #Função de cadastro de produtos
    def Produto(self,NomeDoProduto,Quantidade,PrecoUnitario,id_loja):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Produto VALUES ('{0}',{1},null,{2},{3})".format(NomeDoProduto,Quantidade,PrecoUnitario,id_loja)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
            return NomeDoProduto
        except Exception as e:
            return False

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

    #Função que busca o produto na loja
    def ProdutoConsulta(self,id_loja,NomeDoProduto):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            if ((id_loja != '') and (NomeDoProduto == None)):
                sql = "SELECT IdentificadorProduto,NomeDoProduto,NomeDaFilial,PrecoUnitario,Quantidade FROM Produto,DadosDaLoja ON DadosDaLoja.IdentificadorLoja = {0} GROUP BY SELECT IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            elif ((id_loja == None) and (NomeDoProduto != '')):
                sql = "SELECT IdentificadorProduto,NomeDoProduto,NomeDaFilial,PrecoUnitario,Quantidade FROM Produto JOIN DadosDaLoja ON Produto.NomeDoProduto = '{0}' GROUP BY IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(NomeDoProduto)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            elif ((id_loja != "") and (NomeDoProduto != "")):
                sql = "SELECT IdentificadorProduto,NomeDoProduto,NomeDaFilial,PrecoUnitario,Quantidade FROM DadosDaLoja INNER JOIN Produto ON Produto.NomeDoProduto = '{0}' AND Produto.IdentificadorLoja = {1} AND DadosDaLoja.NomeDaFilial IN (SELECT DadosDaLoja.NomeDaFilial FROM DadosDaLoja WHERE DadosDaLoja.IdentificadorLoja = {2}) GROUP BY IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial".format(NomeDoProduto,id_loja,id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado

        except Exception as e:
            return False

    #Função que retorna dados da loja
    def LojaConsultaHome(self,id_loja,NomeDaFilial):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            if ((id_loja != '') and (NomeDaFilial == None)):
                sql = "SELECT IdentificadorLoja,NomeDaFilial FROM DadosDaLoja WHERE IdentificadorLoja = {0}".format(id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            elif ((id_loja == None) and (NomeDaFilial!= '')):
                sql = "SELECT IdentificadorLoja,NomeDaFilial FROM DadosDaLoja WHERE NomeDaFilial = '{0}' ".format(NomeDaFilial)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            elif(id_loja != "") and (NomeDaFilial != ""):
                sql = "SELECT IdentificadorLoja,NomeDaFilial FROM DadosDaLoja WHERE NomeDaFilial = '{0}' AND IdentificadorLoja = {1}".format(NomeDaFilial,id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado

        except Exception as e:
            return False

    #Função que retorna dados de uma unica loja
    def LojaConsulta(self,NomeDaFilial):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT NomeDaRua,Bairro,Numero,CEP,IdentificadorLoja FROM EnderecoLoja WHERE EnderecoLoja.IdentificadorLoja IN (SELECT DadosDaLoja.IdentificadorLoja FROM DadosDaLoja WHERE DadosDaLoja.NomeDaFilial = '{0}')".format(NomeDaFilial)
            resultado = executar.execute(sql)
            resultado = resultado.fetchall()
            conexao.commit()
            conexao.close()
            return resultado
        except Exception as e:
            return []

    #Função de exclusão de loja, Natan está função não exclui os dados do endereço da loja, somente a loja.
    def ExcluiLoja(self,NomeDaFilial):
        """
        Função responsavel pela exclusão de dados de uma filial, exclui todos os seus campos no banco.

        :param NomeDaFilial: Nome da filial a qual será removida do banco - type(str)
        :return: A função retorna o nome da filial excluida caso tenha conseguido remover os dados da filial do banco,
        caso contrario ele retorna False.
        """
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

    #Função de alteração dos dados do produto
    #Função não está funcionando, Natan está função não está sobscrevendo os antigos dados da loja, apesar de termos visto
    #que a alteração foi feita quando utilizamos o DB Browser SQLite, quando utilizado aqui ela não funcionou.
    def AlterarDadosDaLoja(self,NomeDaFilial:str,id_loja:str,NomeDaRua:str,Bairro:str,Numero:str,CEP:str):
        """
        Função responsavel pela alteração dos dados da loja, é recebido os novos paramentros para sobescrever os antigos dados.

        :param NomeDaFilial: Novo nome da filial -> type(str)
        :param id_loja: Identificador da loja, ele não pode ser alterado, é utilizado somente para a busca da loja -> type(str)
        :param NomeDaRua: Novo nome da rua da fialial -> type(str)
        :param Bairro: Novo nome do bairro da filial -> type(str)
        :param Numero: Novo numero do local onde a filial se situa -> type(str)
        :param CEP: Novo CEP da filial -> type(str)

        :return: A função retorna o nome da filial caso tenha conseguido alterar os dados, caso contrario ela retorna uma lista vazia.
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql1 = "UPDATE DadosDaLoja SET NomeDaFilial = '{0}' WHERE IdentificadorLoja = '{1}'".format(NomeDaFilial,id_loja)
            executar.execute(sql1)
            sql2 = "UPDATE EnderecoLoja SET NomeDaRua = '{0}', Bairro = '{1}', Numero = {2}, CEP = '{3}' WHERE IdentificadorLoja = '{4}'".format(NomeDaRua,Bairro,Numero,CEP,id_loja)
            executar.execute(sql2)
            conexao.commit()
            conexao.close()
            return NomeDaFilial
        except Exception as e:
            return []

    #Função de exclusão de um produto, Natan em relação a essa função o problema está que quando tento excluir um produto de uma loja
    #a exclusão quando  utilizada no DB Browser SQLite funciona de forma correta, só que quando utilizada aqui o produto não é excluído
    #do banco.
    def ExcluiProduto(self,NomeDoProduto:str,id_loja:str):
        """
        Função responsável por exclusão de um produto em uma loja determinada.

        :param NomeDoProduto: Nome do produto que deseja excluir -> type(str)
        :param id_loja: Identificador da loja na qual objetiva excluir o produto -> type(str)

        :return: A função retorna a String Exclusão quando foi o produto foi excluido do banco, caso contrário a função
        retorna None.
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "DELETE FROM Produto WHERE NomeDoProduto = '{0}' AND IdentificadorLoja = '{0}'".format(NomeDoProduto,id_loja)
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
            return "Exclusao"
        except Exception as e:
            return None
    
    def AlterarDadosDoProduto(self,NomeDoProduto,Quantidade,PrecoUnitario,IdentificadorProduto):
        self.ExcluiLoja(NomeDoProduto)
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql1 = "UPDATE Produto SET NomeDoProduto = '{0}',Quantidade = {1}, PrecoUnitario = {2} WHERE IdentificadorProduto = {3}".format(NomeDoProduto,Quantidade,PrecoUnitario,IdentificadorProduto)
            executar.execute(sql1)
            conexao.commit()
            conexao.close()
        except Exception as e:
            raise

    #Função de Busca de Funcionário
    def BuscaFuncionario(self,CPF):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT *FROM Funcionario WHERE CPF = '{0}'".format(CPF)
            resultado = executar.execute(sql)
            sql = "SELECT *FROM EnderecoFuncionario WHERE IdentificadorFuncionario = '{0}'".format(CPF)
            resultado2 = executar.execute(sql)
            conexao.commit()
            conexao.close()
            lista = []
            lista.append(resultado.fetchall())
            lista.append(resultado2.fetchall())
            return lista
        except Exception as e:
            return []

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

    def Login(self,CPF:str,Senha:str):
        """
        Função responsável para a verificar se existe o funcionário solicitado com aquela senha.

        :param CPF: CPF do funcionário -> type (str)
        :param Senha: Senha do funcionário -> type (str)
        :return: A função retorna um dicionário se encontrar aquele funcionário com aquela senha,
        caso contrario ele retorna uma lista vazia.
        """
        try:
            print(CPF,Senha)
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT *FROM Funcionario WHERE CPF = '{0}' AND Senha = '{1}'".format(CPF,Senha)
            resultado = executar.execute(sql)
            teste = resultado.fetchall()
            print(teste)
            conexao.commit()
            conexao.close()
            return teste
        except Exception as e:
            return []

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
