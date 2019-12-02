import sqlite3
class Banco:
    def __init__(self):
        """
        Função de iniciação do banco
        """
        pass

    def Funcionario(self,NomeFuncionario:str,CPF:str,NumeroDeTelefone:str,Senha:str,id_loja:str,NomeDaRua:str,Bairro:str,Numero:str,CEP:str):
        """
        Função resonsavel pelo cadastro do funcionário no banco.

        :param NomeFuncionario: Nome do funcionario a ser cadastrado -> type(str)
        :param CPF: CPF do funcionário -> type(str)
        :param NumeroDeTelefone: Numero de telefone do funcionario -> type(str)
        :param Senha: Senha do funcionario -> type(str)
        :param id_loja: Identificador da loja onde o funcionário será cadastrado -> type(str)
        :param NomeDaRua: Nome da rua do endereço do funcionario -> type(str)
        :param Bairro: Nome do bairro do endereço do funcionario -> type(str)
        :param Numero: Numero do endereço do funcionário -> type(str)
        :param CEP: CEP do endereço do funcionário -> type(str)

        :return: A função retorna uma lista com os dados do funcionário cadastrado, caso contrario ela retorna uma
        lista vazia.
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Funcionario VALUES ('{0}','{1}','{2}','{3}',{4})".format(NomeFuncionario,CPF,NumeroDeTelefone,Senha,id_loja)
            executar.execute(sql)
            sql3 = "INSERT INTO EnderecoFuncionario VALUES ('{0}','{1}',{2},'{3}',{4})".format(NomeDaRua,Bairro,Numero,CEP,CPF)
            resultado = executar.execute(sql3)
            conexao.commit()
            conexao.close()
            return resultado
        except Exception as e:
            return []


    def Produto(self,NomeDoProduto:str,Quantidade:str,PrecoUnitario:str,id_loja:str):
        """
        Função de cadastro de produtos no banco.

        :param NomeDoProduto: Nome do produto para ser cadastrado -> type(str)
        :param Quantidade: Quantidade do produto cadastrado -> type(str)
        :param PrecoUnitario: Preço unitario do produto -> type(str)
        :param id_loja: Identificador da loja onde será cadastrado o produto -> type(str)


        :return: A função retorna o nome do produto quando o produto foi cadastrado, caso contrario
        o retorno é uma lista vazia.
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "INSERT INTO Produto VALUES ('{0}',{1},null,{2},{3})".format(NomeDoProduto,Quantidade,PrecoUnitario,id_loja)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
            return NomeDoProduto
        except Exception as e:
            return []

    def DadosDaLoja(self,NomeDaFilial:str,NomeDaRua:str,Bairro:str,Numero:str,CEP:str):
        """
        Função responsavel pelo cadastro de uma filial.

        :param NomeDaFilial: Nome da  filial a ser cadastrada -> type(str)
        :param NomeDaRua: Nome da rua da loja -> type(str)
        :param Bairro: Nome do bairro -> type(str)
        :param Numero: Numero do endereço da loja -> type(str)
        :param CEP: Numero do  CEP do endereço da loja -> type(str)

        :return: A função não possui retorno.
        """
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

    def ProdutoConsulta(self,id_loja:str,NomeDoProduto:str):
        """
        Função responsavel pela busca dos dados do produto no banco.
        A função pode receber o nome e o identificador da loja ou somente o nome ou somente o identificador da loja.

        :param id_loja: Identificador da loja -> type(str)
        :param NomeDoProduto: Nome do produto -> type(str)

        :return: A função retorna uma lista com os dados do produto cadastrado, caso contrario retorna um lista vazia.
        """
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
            return []

    def ProdutoConsultaItens(self,id_loja:str,NomeDoProduto:str):

        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            if ((id_loja != '') and (NomeDoProduto == None)):
                sql = "SELECT * FROM Produto WHERE IdentificadorLoja = {0}".format(id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            elif ((id_loja == None) and (NomeDoProduto != '')):
                sql = "SELECT * FROM Produto WHERE NomeDoProduto = '{0}'".format(NomeDoProduto)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado
            elif ((id_loja != "") and (NomeDoProduto != "")):
                sql = "SELECT * FROM Produto WHERE NomeDoProduto = '{0}' AND IdentificadorLoja = {1}".format(NomeDoProduto,id_loja,id_loja)
                resultado = executar.execute(sql)
                resultado = resultado.fetchall()
                conexao.commit()
                conexao.close()
                return resultado

        except Exception as e:
            return []

    def LojaConsultaHome(self,id_loja:str,NomeDaFilial:str):
        """
        Função responsável por retornar dados da filial, a função faz a busca utilizando o nome e identificador da loja ou somente
        o nome da filial ou somente o identificador da loja.

        :param id_loja: Identificador da filial que deseja se obter informações -> type(str)
        :param NomeDaFilial: Nome da filial que deseja se obter informações -> type(str)


        :return: A função retorna uma lista com os dados da loja, caso contrario ela retorna falso.
        """
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

    def todosOsDadosDaLoja(self):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT * FROM DadosDaLoja"
            resultado = executar.execute(sql)
            resultado = resultado.fetchall()
            conexao.commit()
            conexao.close()
            return resultado
        except Exception as e:
            return []

    def todosOsProdutos(self):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT * FROM Produto"
            resultado = executar.execute(sql)
            resultado = resultado.fetchall()
            conexao.commit()
            conexao.close()
            return resultado
        except Exception as e:
            return []

    def LojaConsulta(self,NomeDaFilial:str):
        """
        Função responsavel pela busca de uma loja no banco;

        :param NomeDaFilial: Nome da filial para a busca no banco -> type(str)

        :return: A função retorna uma lista com os dados da loja buscado, caso contrario ela retorna uma lista vazia
        """
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

    def ExcluiLoja(self,NomeDaFilial:str,id_loja:str):
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
            executar.execute(sql)
            sql1 = "DELETE FROM EnderecoLoja WHERE IdentificadorLoja = '{0}'".format(id_loja)
            executar.execute(sql1)
            conexao.commit()
            conexao.close()
            return NomeDaFilial
        except Exception as e:
            return False

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
            sql2 = "UPDATE EnderecoLoja SET NomeDaRua = '{0}', Bairro = '{1}', Numero = '{2}', CEP = '{3}' WHERE IdentificadorLoja = '{4}'".format(NomeDaRua,Bairro,Numero,CEP,id_loja)
            executar.execute(sql2)
            conexao.commit()
            conexao.close()
            return NomeDaFilial
        except Exception as e:
            return []

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
            sql = "DELETE FROM Produto WHERE NomeDoProduto = '{0}' AND IdentificadorLoja = '{1}'".format(NomeDoProduto,id_loja)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
            return "Exclusao"
        except Exception as e:
            return None

    def AlterarDadosDoProduto(self,NomeDoProduto:str,Quantidade:str,PrecoUnitario:str,IdentificadorProduto:str,IdentificadorLoja:str):
        """
        Função responsavel pela alteração dos dados do produto!

        :param NomeDoProduto: Novo nome do produto -> type(str)
        :param Quantidade: Nova quantidade para o produto -> type(str)
        :param PrecoUnitario: Novo preço unitario para o produto -> type(str)
        :param IdentificadorProduto: Identificador do produto que deve ter seus dados alterados -> type(str)
        :param IdentificadorLoja: identificador da loja onde possui um produto que deve ser alterado os valores -> type(str)


        :return: A função retorna o Nome do produto caso tenha conseguido fazer a alteração, caso contrario
        a função retorna uma lista vazia!
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql1 = "UPDATE Produto SET NomeDoProduto = '{0}',Quantidade = '{1}', PrecoUnitario = '{2}' WHERE IdentificadorProduto = '{3}' AND IdentificadorLoja = '{4}'".format(NomeDoProduto,Quantidade,PrecoUnitario,IdentificadorProduto,IdentificadorLoja)
            executar.execute(sql1)
            conexao.commit()
            conexao.close()
            return NomeDoProduto
        except Exception as e:
            return []

    def BuscaFuncionario(self,CPF:str):
        """
        Função responsavel por retornar dados dos funcionários dos funcionários buscados apartir do CPF.

        :param CPF: CPF do funcionário -> type(str)

        :return: A função retorna uma lista com os dados do funcionário, caso contrario retorna uma lista vazia.
        """
        try:
            lista = []
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT *FROM Funcionario WHERE CPF = '{0}'".format(CPF)
            resultado = executar.execute(sql)
            lista.append(resultado.fetchall())
            sql1 = "SELECT *FROM EnderecoFuncionario WHERE IdentificadorFuncionario = '{0}'".format(CPF)
            resultado2 = executar.execute(sql1)
            lista.append(resultado2.fetchall())
            conexao.commit()
            conexao.close()
            return lista
        except Exception as e:
            return []

    def AlteraFuncionario(self,NomeDoFuncionario:str,Rua:str,NumeroRua:str,Bairro:str,CEP:str,CPF:str,NumeroDeTelefone:str,Senha:str,IdentificadorLoja:str):
        """
        Função responsavel para alterar os dados do funcionario.

        :param NomeDoFuncionario: Novo nome do funcionario -> type(str)
        :param Rua: Novo nome da rua do funcionario -> type(str)
        :param NumeroRua: Novo numero da rua do funcionário -> type(str)
        :param Bairro: Novo nome do bairro do funcionario -> type(str)
        :param CEP: Novo CEP do endereço do funcionário -> type(str)
        :param CPF: CPF do funcionário, campo não alteravel -> type(str)
        :param NumeroDeTelefone: Novo numero de telefone do funcionario -> type(str)
        :param Senha: Nova senha do funcionario -> type(str)
        :param IdentificadorLoja: Nova loja onde o funcionário vai trabalhar -> type(str)


        :return: A função retorna o CPF do Funcionário caso a alteração seja bem sucedida, caso contrario a função retorna uma
        lista vazia.
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "UPDATE Funcionario SET NomeDoFuncionario = '{0}', NumeroDeTelefone = '{1}', Senha = '{2}', IdentificadorLoja = {3} WHERE CPF = '{4}'".format(NomeDoFuncionario,NumeroDeTelefone,Senha,IdentificadorLoja,CPF)
            executar.execute(sql)
            sql2 = "UPDATE EnderecoFuncionario SET NomeDaRua = '{0}', Bairro = '{1}', Numero = '{2}', CEP = {3} WHERE IdentificadorFuncionario = '{4}'".format(
                Rua, Bairro, NumeroRua, CEP, CPF)
            executar.execute(sql2)
            conexao.commit()
            conexao.close()
            return CPF
        except Exception as e:
            return []

    def ExcluiFuncionario(self,CPF:str):
        """
        Função responsavel por excluir um funcionário do banco!


        :param CPF: CPF do funcionário que será excluído do banco -> type(str)

        :return: A função retorna o CPF do funcionário se conseguir exclui-lo, caso contrario o retorno é uma lista
        vazia.
        """
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "DELETE FROM Funcionario WHERE CPF = '{0}'".format(CPF)
            executar.execute(sql)
            sql1 = "DELETE FROM EnderecoFuncionario WHERE IdentificadorFuncionario = '{0}'".format(CPF)
            executar.execute(sql1)
            conexao.commit()
            conexao.close()
            return CPF
        except Exception as e:
            return []

    def Login(self,CPF:str,Senha:str):
        """
        Função responsável para a verificar se existe o funcionário solicitado com aquela senha.

        :param CPF: CPF do funcionário -> type (str)
        :param Senha: Senha do funcionário -> type (str)

        :return: A função retorna um dicionário se encontrar aquele funcionário com aquela senha,
        caso contrario ele retorna uma lista vazia.
        """
        try:

            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = "SELECT *FROM Funcionario WHERE CPF = '{0}' AND Senha = '{1}'".format(CPF,Senha)
            resultado = executar.execute(sql)
            teste = resultado.fetchall()
            conexao.commit()
            conexao.close()
            return teste
        except Exception as e:
            return []

    def Vender(self,nomeVendedor,dataDaVenda,precoTotal):
        try:
            conexao = sqlite3.connect("Loja")
            executar = conexao.cursor()
            sql = ""
            resultado = executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            return []
