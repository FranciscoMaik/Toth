class Produto:
    __slots__ = ['_nome_do_produto','_quantidade','_identificador','_preco_unitario']
    def __init__(self,nome_do_produto,identificador,preco_unitario,quantidade = 0):
        self._nome_do_produto = nome_do_produto
        self._quantidade = quantidade
        self._identificador = identificador
        self._preco_unitario = preco_unitario

    #+++++++++++++++++++++++nome==================
    @property
    def nome_do_produto(self):
        return self._nome_do_produto

    @nome_do_produto.setter
    def nome_do_produto(self,novo_nome):
        self._nome_do_produto = novo_nome
        return True
    #+++++++++++++++++++++quantidade+++++++++++++

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

    @property
    def identificador(self):
        return self._identificador

    @property
    def preco_unitario(self):
        return self._preco_unitario

    def alterar_valor(self,valor):
        self._preco_unitario = valor


prod = Produto('Cimento',1,43.50,42)
prod.quantidade
prod.nome_do_produto
prod.preco_unitario
prod.identificador

prod.adicionar_quantidade(10)
prod.quantidade
prod.retirar_quantidade(3)
prod.quantidade

