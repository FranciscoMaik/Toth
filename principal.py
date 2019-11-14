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
            #Buscar se aquele produto já está cadastrado na loja
            verificacao2 = Banco().ProdutoConsulta(recebe[4],recebe[1])

            #verifica se o retorno é falso, caso seja falso aquele produto não foi cadastrado naquela loja
            if verificacao2 == []:
                #verificar se a loja existe
                ver_existe_loja = Banco().LojaConsultaHome(int(recebe[4]), None)
                #Se ver_existe_loja retornar falso a loja não existe
                if ver_existe_loja == []:
                    nmensagem = "Loja não existe, por favor cadastre em uma loja existente!"
                    mensagem = nmensagem.encode()
                else:
                    #Se a loja existe, cadastra o produto
                    verificacao3 = Banco().Produto(recebe[1],recebe[2],recebe[3],recebe[4])
                    # Verificação se o produto foi realmente cadastrado
                    if verificacao3 != False:
                        #trasforma em String para mandar para o cliente
                        nmensagem = "Produto cadastrado com Sucesso!"
                        mensagem = nmensagem.encode()

            #caso contraio o produto já foi cadastrado naquela loja
            else:
                nmensagem = "Este produto já foi cadastrado nesta loja!"
                mensagem = nmensagem.encode()

        #buscar produto para a tela
        elif opcao == "buscarProduto":
            #verifica se a loja onde se esta buscando o produto realmente existe
            verificacao1 = Banco().LojaConsultaHome(int(recebe[2]), None)
            if verificacao1 != []:
                verificacao = Banco().ProdutoConsulta(recebe[2], recebe[1])
                if verificacao != []:
                    outra = "prodexiste,"
                    for i in verificacao[0]:
                        outra += str(i) + ","
                    mensagem = outra.encode()
                else:
                    nmensagem = "prodnoexiste"
                    mensagem = nmensagem.encode()
            else:
                nmensagem = "lojanoexiste"
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
            #verifica se existe a loja na qual está tentando cadastrar o funcionário
            verificacao = Banco().LojaConsultaHome(recebe[8],None)
            if verificacao != []:
                #verifica se o funcionário já está cadastrado
                verificacao1 = Banco().BuscaFuncionario(recebe[7])
                print(verificacao1)
                if verificacao1 != []:
                    nmensagem = "Este funcionário já está cadastrado em alguma filial!"
                    mensagem = nmensagem.encode()
                else:
                    #cadastra o funcionário caso o mesmo não esteja cadastrado
                    verificacao2 = Banco().Funcionario(recebe[1],recebe[7],recebe[3],recebe[6],recebe[8],recebe[2],recebe[4],recebe[9],recebe[5])
                    if verificacao2 != []:
                        nmensagem = "Funcionário cadastrado com sucesso!"
                        mensagem = nmensagem.encode()
                    else:
                        #caso dê algum problema no cadastro do funcionário
                        nmensagem = "Não foi possivel cadastrar o funcionário tente novamente!"
                        mensagem = nmensagem.encode()
            else:
                #Caso esteja tentando um cadastro em uma loja que não existe!
                nmensagem = "A loja na qual está tentando cadastrar o funcionário não existe, tente em uma loja existente!"
                mensagem = nmensagem.encode()

        #buscar funcionario
        #função de busca não está funcionando aqui!
        elif opcao == "buscarFuncionario":
            #Verifica se o funcionário existe!
            verificacao = Banco().BuscaFuncionario(recebe[1])
            #Caso o funcionário exista é retornado os valores do funcionário
            if verificacao != []:
                outra = "existe,"
                for i in verificacao[0]:
                    outra += str(i) + ","
                mensagem = outra.encode()
                print(outra)
            #Caso ele não esteja cadastrado no banco é retornado vazio!
            elif verificacao == []:
                nmensagem = "noexiste,"
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

        #Buscando Loja
        elif opcao == "buscarLoja":
            #retorno de valores da loja pelo banco
            verificacao = Banco().LojaConsulta(recebe[1])
            if verificacao == []:
                nmensagem = str(False) + ","
                mensagem = nmensagem.encode()
            elif verificacao != []:
                outra = ''
                for i in verificacao[0]:
                    outra += str(i) + ","
                mensagem = outra.encode()

        #Alterando valores da loja
        elif opcao == "valoresLojaAlterado":
            #recebe os valores da loja para ser alterados
            #verifica se a loja existe
            verificacao = Banco().LojaConsulta(recebe[1])
            if verificacao != []:
                outra = ''
                #for para pegar o id_loja da tabela LojaConsulta
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
            #busca as instancias no banco e retorna eles
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
