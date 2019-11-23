class Produto:

    _identificador_do_produto = 0
    @staticmethod
    def identificador_do_produto():
        return Produto._identificador_do_produto

    __slots__ = ['_nome_do_produto','_quantidade','_identificador','_preco_unitario']
    def __init__(self,nome_do_produto,preco_unitario,quantidade = 0):
        self._nome_do_produto = nome_do_produto
        self._quantidade = quantidade
        Produto._identificador_do_produto += 1
        self._preco_unitario = preco_unitario
        self._identificador = Produto._identificador_do_produto
    #____________________________nome____________________________
    @property
    def nome_do_produto(self):
        return self._nome_do_produto

    @nome_do_produto.setter
    def nome_do_produto(self,novo_nome):
        self._nome_do_produto = novo_nome
        return True
    #____________________________quantidade____________________________
    @property
    def quantidade(self):
        return self._quantidade

    def retirar_quantidade(self,valor):
        if valor > self.quantidade:
            return False
        else:
            self._quantidade-=valor
            return True

    def adicionar_quantidade(self,valor):
        self._quantidade += valor
        return True

    # ____________________________identificador____________________________
    @property
    def identificador(self):
        return self._identificador

    # ____________________________preço____________________________
    @property
    def preco_unitario(self):
        return self._preco_unitario

    def alterar_valor(self,valor):
        self._preco_unitario = valor

    def mostra_produto(self):
        print("Nome: {}\nIdentificador: {}\nPreço: {}\nQuantidade: {}\n\n".format(self.nome_do_produto, self.identificador,
                                                                                    self.preco_unitario, self.quantidade))

#____________________________teste de classe____________________________
if __name__ == '__main__':
    lista = []
    prod = Produto('Cimento',43.50,42)
    prod2 = Produto('Reajunte', 12.00, 10)
    lista.append(prod);
    #Criar função com lambida
    #valor = list(filter(lambda elemento : elemento.identificador == identificador(entrada), lista_de_produtos))
    #if valor :
    #    print(valor.mostrar dados())
    #else:
    #   print("Produto não encontrado")


    print('Quantidade do produto:',prod.quantidade)
    print('Nome do produto:',prod.nome_do_produto)
    print('Preço do produto:',prod.preco_unitario)
    print('Identificador do produto 1:',prod.identificador)
    print('Identificador do produto 2:', prod2.identificador)
    prod.adicionar_quantidade(10)
    print('Quantidade do produto:',prod.quantidade)
    prod.retirar_quantidade(3)
    print('Quantidade do produto:',prod.quantidade)

