# from toth.Classes.produtos import produtos
# from funcionario import Funcionario
# from endereço import Endereco
# from loja import Loja
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
    global mensagem
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
                ver_existe_loja = Banco().LojaConsultaHome(recebe[4], None)
                #Se ver_existe_loja retornar falso a loja não existe
                if ver_existe_loja == []:
                    nmensagem = "Loja não existe, por favor cadastre em uma loja existente!"
                    mensagem = nmensagem.encode()
                else:
                    #Se a loja existe, cadastra o produto
                    verificacao3 = Banco().Produto(recebe[1],recebe[2],recebe[3],recebe[4])
                    # Verificação se o produto foi realmente cadastrado
                    if verificacao3 != []:
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
            #Verifica se o produto existe naquela loja
            verificacao = Banco().ProdutoConsulta(recebe[4],recebe[1])
            #se existir ele cadastra altera os valores do produto
            if verificacao != []:
                identificadorProd = verificacao[0][0]
                verificacao2 = Banco().AlterarDadosDoProduto(recebe[1],recebe[2],recebe[3],identificadorProd,recebe[4])
                if verificacao2 != []:
                    nmensagem = "Valores do produto " + str(verificacao2) + " alterados!"
                    mensagem = nmensagem.encode()
            #caso contrario ele manda uma mensadem de aviso!
            else:
                nmensagem = "Produto não cadastrado na loja ou loja não existente!"
                mensagem = nmensagem.encode()

        #Excluir produto
        elif opcao == "excluirProduto":
            verificacao = Banco().ProdutoConsulta(recebe[2],recebe[1])
            print(verificacao)
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
                if verificacao1 != [] and verificacao1 != [[],[]]:
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
        elif opcao == "buscarFuncionario":
            #Verifica se o funcionário existe!
            verificacao = Banco().BuscaFuncionario(recebe[1])
            #Caso o funcionário exista é retornado os valores do funcionário
            if verificacao != [] and verificacao != [[],[]]:
                outra = "existe,"
                for i in verificacao:
                    for j in i[0]:
                        outra += str(j) + ","
                mensagem = outra.encode()
            #Caso ele não esteja cadastrado no banco é retornado vazio!
            else:
                nmensagem = "noexiste,"
                mensagem = nmensagem.encode()

        #Alterar valores do funcionário
        elif opcao == "alterarDadosFuncionario":
            verificacao = Banco().BuscaFuncionario(recebe[7])
            #Verifica se o funcionario realmente existe
            if verificacao != [] and verificacao !=[[],[]]:
                verificacao1 = Banco().LojaConsultaHome(recebe[8], None)
                # verifica se a nova loja na qual o funcionario vai ser cadastrado existe
                if verificacao1 != []:
                    verificacao2 = Banco().AlteraFuncionario(recebe[1],recebe[2],recebe[9],recebe[4],recebe[5],recebe[7],recebe[3],recebe[6],recebe[8])
                    if verificacao2 != []:
                        nmensagem = "Dados do funcionário alterados!"
                        mensagem = nmensagem.encode()
                    else:
                        nmensagem = "Não foi possivel alterar os dados do funcionário!"
                        mensagem = nmensagem.encode()
                else:
                    nmensagem = "Loja onde deseja cadastrar o funcionário não existe!"
                    mensagem = nmensagem.encode()
            else:
                nmensagem = "Funcionário não cadastrado!"
                mensagem = nmensagem.encode()

        #Exclusão de funcionário
        elif opcao == "excluirFuncionario":
            #verifica se o funcionário existe
            verificacao = Banco().BuscaFuncionario(recebe[1])
            if verificacao != [[],[]] or verificacao !=[]:
                verificacao2 = Banco().ExcluiFuncionario(recebe[1])
                #verifica se o funcionário foi excluído
                if verificacao2 != []:
                    nmensagem = "Funcionário removido do banco!"
                    mensagem = nmensagem.encode()
                #caso não tenha conseguido remover o funcionário ele manda uma mensagem de alerta!
                else:
                    nmensagem = "Não foi possivel excluir funcionário!"
                    mensagem = nmensagem.encode()
            #caso o funcionario não exista ele recebe uma mensagem de alerta
            else:
                nmensagem = "Funcionário não cadastrado!"
                mensagem = nmensagem.encode()

        #Cadastro de lojas
        elif opcao == "Loja":
            validacao = Banco().LojaConsulta(recebe[1])
            if validacao == []:
                Banco().DadosDaLoja(recebe[1],recebe[2],recebe[4],recebe[3],recebe[5])
                nmensagem = "Loja " + recebe[1] + " Cadastrada!"
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
            print("existe loja",verificacao)
            if verificacao != []:
                outra = ''
                #for para pegar o id_loja da tabela LojaConsulta
                for i in verificacao[0]:
                    outra += str(i) + ","
                outra = outra.split(',')
                print(outra)

                verificacao2 = Banco().AlterarDadosDaLoja(recebe[1], outra[4], recebe[2], recebe[4], recebe[3], recebe[5])
                print("Alteração",verificacao2)
                verificacao2 = verificacao2 + ","
                mensagem = verificacao2.encode()
            elif verificacao == []:
                nmensagem = "Loja não encontrada, informe uma loja para alterar seus dados!"
                mensagem = nmensagem.encode()

        #Exclusão da loja
        elif opcao == "excluirLoja":
            #Exclui a loja do banco
            verificacao = Banco().LojaConsultaHome(None,recebe[1])
            if verificacao != []:
                verificacao2 = Banco().ExcluiLoja(recebe[1],verificacao[0][0])
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
            if recebe[1] == "vazio" and recebe[2] != "vazio":
                verificacao = Banco().LojaConsultaHome(recebe[2],None)
                if verificacao != []:
                    outra = ""
                    for i in verificacao[0]:
                        outra += str(i) + ","
                    mensagem = outra.encode()

                elif verificacao == []:
                    nmensagem = "Loja não cadastrada!"
                    mensagem = nmensagem.encode()

            elif  recebe[1] != "vazio" and recebe[2] == "vazio":
                print("Entrou opcao 2")
                verificacao = Banco().LojaConsultaHome(None,recebe[1])
                print("Verificação 2", verificacao)
                if verificacao != []:
                    outra = ""
                    for i in verificacao[0]:
                        outra += str(i) + ","
                    print(outra)
                    mensagem = outra.encode()
                elif verificacao == []:
                    print("Entrou aqui! Opção dois!")
                    nmensagem = "Loja não cadastrada!"
                    mensagem = nmensagem.encode()

            elif recebe[1] == "vazio" and recebe[2] == "vazio":
                verificacao = Banco().LojaConsultaHome(None,None)
                print(verificacao)
                if verificacao != False:
                    outra = ""
                    for i in verificacao:
                        for j in i:
                            outra = str(j) + ","
                        outra += ";"
                    mensagem = outra.encode()

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
