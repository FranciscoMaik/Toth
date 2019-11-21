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

        #Alterando os valores do produto
        elif opcao == "alterarValoresdoProduto":
            #altera os valores no banco
            nmensagem = "Valores Alterador"
            mensagem = nmensagem.encode()

        #Excluir produto
        elif opcao == "excluirProduto":
            verificacao = Banco().ProdutoConsulta(recebe[2],recebe[1])
            if verificacao != []:
                verificacao1 = Banco().ExcluiProduto(recebe[1],recebe[2])
                if verificacao1 != None:
                    nmensagem = "Produto excluido!"
                    mensagem = nmensagem.encode()
                else:
                    nmensagem = "Não foi possivel excluir o produto"
                    mensagem = nmensagem.encode()
            else:
                nmensagem = "O produto não existe nesta loja! Ou a loja não é cadastrada!"
                mensagem = nmensagem.encode()

        #Cadastro de funcionarios
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

        #Buscar funcionario
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

        #Alterar valores do funcionário
        elif opcao == "alterarDadosFuncionario":
            #recebe e altera os valores de um funcionario
            nmensagem = "Valores alterados"
            mensagem = nmensagem.encode()

        #Exclusão de funcionário
        elif opcao == "excluirFuncionario":
            #excluir funcionário do banco
            nmensagem = "Funcionário excluido"
            mensagem = nmensagem.encode()

        #Cadastro de lojas
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
                nmensagem = "naoencontrada,"
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

        #Exclusão da loja
        elif opcao == "excluirLoja":
            #Exclui a loja do banco
            verificacao = Banco().LojaConsulta(recebe[1])
            if verificacao != []:
                verificacao2 = Banco().ExcluiLoja(recebe[1])
                verificacao2 = verificacao2 + ","
                mensagem = verificacao2.encode()
            elif verificacao == []:
                nmensagem = "Não é possível excluir a Loja pois a mesma não se encontra no banco!"
                mensagem = nmensagem.encode()

        #Buscar estoque no home
        elif opcao == "buscarEstoqueHome":
            #busca as instancias no banco e retorna eles
            nmensagem = "Estoque home"
            mensagem = nmensagem.encode()

        #BuscarLojaHome
        elif opcao == "buscarLojaHome":
            #busca a loja no banco de acordo com os parâmetros
            nmensagem = "Loja home"
            mensagem = nmensagem.encode()

        #Login
        elif opcao == "Login":
            #a = "Login," + cpfentrada + "," + senha
            verificacao = Banco().Login(recebe[1],recebe[2])
            if verificacao != []:
                outra = ""
                for i in verificacao[0]:
                    outra += str(i) + ","
                mensagem = outra.encode()
            else:
                nmensagem = "naoencontrado,"
                mensagem = nmensagem.encode()

        #Vender
        elif opcao == 'Vender':
            nmensagem = "Produto vendido!"
            mensagem = nmensagem.encode()

        #Mensagem de conexão
        else:
            mensagem = "Cliente Conectado!".encode()
        con.send(mensagem)

if __name__ == '__main__':
    conectar()
