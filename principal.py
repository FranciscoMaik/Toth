from produtos import Produto
import socket
host = ''
port = 7000
addr = (host,port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)

def cadastra_produto(lista_de_produto):
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
        i.mostra_produto()

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
        elif opcao == "Produto":
            prod = Produto(recebe[1],int(recebe[2]),float(recebe[3]))
            nmensagem = prod.nome_do_produto + " foi adicionado!"
            mensagem = nmensagem.encode()
        else:
            mensagem = "Cliente Conectado!".encode()
        con.send(mensagem)

    lista_de_produto = []
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
            break


if __name__ == '__main__':
    conectar()
