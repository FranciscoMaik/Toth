class Produto:
    __slots__ = ['_nome_do_produto','_quantidade','_identificador','_preco_unitario']
    def __init__(self,nome_do_produto,identificador,preco_unitario,quantidade = 0):
        self._nome_do_produto = nome_do_produto
        self._quantidade = quantidade
        self._identificador = identificador
        self._preco_unitario = preco_unitario

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

#____________________________teste de classe____________________________
prod = Produto('Cimento',1,43.50,42)
print('Quantidade do produto:',prod.quantidade)
print('Nome do produto:',prod.nome_do_produto)
print('Preço do produto:',prod.preco_unitario)
print('Identificador do produto:',prod.identificador)

prod.adicionar_quantidade(10)
print('Quantidade do produto:',prod.quantidade)
prod.retirar_quantidade(3)
print('Quantidade do produto:',prod.quantidade)

