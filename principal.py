from produtos import Produto
from funcionario import Funcionario
from endereço import Endereco
from loja import Loja
import socket

from Banco import Banco

host = ''
port = 7000
addr = (host,port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)

"""def cadastra_produto(lista_de_produto):
    valor = int(input("Cadastrar produto:\n1 - para sim\n2 - para não\n>>>"))

    while (valor == 1):
        nome = input("Informe o Nome do Produto: ")
        valor = float(input("informe o Preço do Produto: "))
        quantidade = int(input("Informe a quantidade do Produto: "))

        produto = Produto(nome, valor, quantidade)

        lista_de_produto.append(produto)
        print("O produto cadastrado possuí ID: {}".format(produto.identificador))

        valor = int(input("Cadastrar um novo produto:\n1 - para sim\n2 - para não\n>>>"))

    print('Produtos cadastrados:')

    for i in lista_de_produto:
        i.mostra_produto()"""

def conectar():
    while (True):
        print("Servidor está aguardando Conexão!")
        con, cliente = serv_socket.accept()
        print("Conectado!")
        recebe = con.recv(1024).decode()
        recebe = recebe.split(",")
        opcao = recebe[0]
        print(opcao)
        print('Mensagem recebida: ' + opcao)
        if opcao == "sair":
            return
        #cadastro de produtos
        elif opcao == "Produto":
            #cria produto
            #parametros que o produto recebe
            #a = "id_prod(pk auto incremento)" + nome + "," + quantidade + "," + preco + "," + id_loja(fk)-> em outra tabela
            verificacao2 = Banco().ProdutoConsulta(recebe[4],recebe[1])
            #IdentificadorProduto,NomeDoProduto,Quantidade,NomeDaFilial,PrecoUnitario,Quantidade
            #não está cadastrando produto!
            outra = outra2 = ''

            if verificacao2 == False:
                pass
            else:
                for i in verificacao2[0]:
                    outra += str(i) + ','
                outra2 = outra.split(',')

            if outra2 != '':
                verificacao3 = Banco().LojaConsulta(outra2[3])
                # NomeDaRua,Bairro,Numero,CEP,IdentificadorLoja
                outra3 = ''
                for i in verificacao3[0]:
                    outra3 += str(i) + ","

                outra4 = outra3.split(',')


                if(recebe[1] == outra2[1] and recebe[4] == outra4[4]):
                    nmensagem = "Não é possivel cadastrar o mesmo produto na loja"
                    mensagem = nmensagem.encode()
                else:
                    resp = Produto(recebe[1],recebe[2],recebe[3],recebe[3])
                    nmensagem = "Produto" + resp + " cadastrado"
                    mensagem = nmensagem.encode()
            else:
                nmensagem = "Erro!"
                mensagem = nmensagem.encode()
        #buscar produto para a tela
        elif opcao == "buscarProduto":
            #pegar valores no banco
            nmensagem = "Valores do produto"
            mensagem = nmensagem.encode()

        #alterando os valores do produto
        elif opcao == "alterarValoresdoProduto":
            #altera os valores no banco
            nmensagem = "Valores Alterador"
            mensagem = nmensagem.encode()

        #excluir produto
        elif opcao == "excluirProduto":
            #exclui produto do banco
            nmensagem = "Produto excluido!"
            mensagem = nmensagem.encode()

        #cadastro de funcionarios
        elif opcao == "Funcionario":
            #cria endereço para funcionário
            #métodos de recebimento
            # a = id_func(pk auto incremento) + nome + "," + rua + "," + num + "," + bairro + "," + cep + "," + senha + "," + cpf + "," + loja(fk em outra tabela fazendo a relação de relacionamento) + "," + numero_rua

            endereco_fun = Endereco(recebe[2],recebe[4],int(recebe[9]),recebe[5])
            #cria funcionário
            new_func = Funcionario(recebe[1],recebe[7],recebe[3],endereco_fun,recebe[6])
            Banco().Funcionario(recebe[1],recebe[7],recebe[3],recebe[6],recebe[8],recebe[2],recebe[4],recebe[9],recebe[5])
            nmensagem = "Funcionário " + new_func.nome_do_funcionario + " Cadastrado!"
            mensagem = nmensagem.encode()

        #buscar funcionario
        elif opcao == "buscarFuncionaio":
            #retona os valores do banco
            nmensagem = "Esses são os valores do funcionario"
            mensagem = nmensagem.encode()

        #alterar valores do funcionário
        elif opcao == "alterarDadosFuncionario":
            #recebe e altera os valores de um funcionario
            nmensagem = "Valores alterados"
            mensagem = nmensagem.encode()

        #exclusão de funcionário
        elif opcao == "excluirFuncionario":
            #excluir funcionário do banco
            nmensagem = "Funcionário excluido"
            mensagem = nmensagem.encode()
        #cadastro de lojas
        elif opcao == "Loja":
            #sequencia de cadastro no banco
            # a = id_loja(pk auto incremento) + nome + "," + rua + "," + num + "," + bairro + "," + cep

            #cria endereço da loja
            end_loja = Endereco(recebe[2],recebe[4],recebe[3],int(recebe[5]))
            #cria loja
            loja = Loja(recebe[1],end_loja)
            validacao = Banco().LojaConsulta(recebe[1])
            if validacao == []:
                Banco().DadosDaLoja(recebe[1],recebe[2],recebe[4],recebe[3],recebe[5])
                nmensagem = "Loja " + loja.nome_da_filial + " Cadastrada!"
                mensagem = nmensagem.encode()
            elif validacao != []:
                nmensagem = "Loja Não pode ser Cadastrada, há uma filial com o mesmo nome!"
                mensagem = nmensagem.encode()

        #buscando Loja
        elif opcao == "buscarLoja":
            #retorno de valores da loja pelo banco
            verificacao = Banco().LojaConsulta(recebe[1])
            print('verificacao',verificacao)
            if verificacao == []:
                nmensagem = str(False) + ","
                mensagem = nmensagem.encode()
            elif verificacao != []:
                outra = ''
                for i in verificacao[0]:
                    outra += str(i) + ","
                mensagem = outra.encode()

        #alterando valores da loja
        elif opcao == "valoresLojaAlterado":
            #recebe os valores da loja para ser alterados
            verificacao = Banco().LojaConsulta(recebe[1])
            if verificacao != []:
                outra = ''
                for i in verificacao[0]:
                    outra += outra + ","
                outra = outra.split(',')
                verificacao2 = Banco().AlterarDadosDaLoja(recebe[1], outra[4], recebe[2], recebe[4], recebe[3], recebe[5])
                verificacao2 = verificacao2 + ","
                mensagem = verificacao2.encode()
            elif verificacao == []:
                nmensagem = "Loja não encontrada, informe uma loja para alterar seus dados!"
                mensagem = nmensagem.encode()

        #exclusão da loja
        elif opcao == "excluirLoja":
            #exclui a loja do banco
            verificacao = Banco().LojaConsulta(recebe[1])
            if verificacao != []:
                verificacao2 = Banco().ExcluiLoja(recebe[1])
                verificacao2 = verificacao2 + ","
                mensagem = verificacao2.encode()
            elif verificacao == []:
                nmensagem = "Não é possível excluir a Loja pois a mesma não se encontra no banco!"
                mensagem = nmensagem.encode()

        #buscar estoque no home
        elif opcao == "buscarEstoqueHome":
            #busca as instancias no banco e retorna
            nmensagem = "Estoque home"
            mensagem = nmensagem.encode()

        #buscarLojaHome
        elif opcao == "buscarLojaHome":
            #busca a loja no banco de acordo com os parâmetros
            nmensagem = "Loja home"
            mensagem = nmensagem.encode()

        #login
        elif opcao == "Login":
            #a = "Login," + cpfentrada + "," + senha
            nmensagem = "Login efetuado!"
            mensagem = nmensagem.encode()

        #vender
        elif opcao == 'Vender':
            nmensagem = "Produto vendido!"
            mensagem = nmensagem.encode()

        #mensagem de conexão
        else:
            mensagem = "Cliente Conectado!".encode()
        con.send(mensagem)

    """lista_de_produto = []
    while (True):
        print(10 * '_' + 'MENU' + 10 * '_')
        print("1 - OPÇÔES DOS PRODUTOS")
        print("2 - OPÇÔES DE FUNCIONÁRIOS")
        print("3 - OPÇÔES DA LOJA")
        print('4 - SAIR')
        opcao = int(input('Opção: '))

        if opcao == 1:
            print('1 - CADASTRAR UM PRODUTO')
            print('2 - PARA MOSTRAR PRODUTOS')
            print('3 - BUSCAR UM PRODUTO')
            print('4 - EXLUIR UM PRODUTO')
            opcao2 = int(input('Opção: '))

            if opcao2 == 1:
                cadastra_produto(lista_de_produto)
            elif opcao2 == 2:
                for i in lista_de_produto:
                    i.mostra_produto()
            elif opcao2 == 3:
                iden = int(input("Informe o identificador do produto: "))
                valor = list(filter(lambda elemento: elemento.identificador == iden, lista_de_produto))
                if valor:
                    valor[0].mostra_produto()
                else:
                    print("Produto não encontrado")

        elif opcao == 4:
            break"""


if __name__ == '__main__':
    conectar()
