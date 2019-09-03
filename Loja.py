class Loja:
	__slots__ = ['nome_da_filial','identificador','Endereco']
	__init__(self,nome_da_filial,identificador,Endereco):
		self._nome_da_filial = nome_da_filial
		self._identificador = identificador
		self._endereco = Endereco
	#_____________________Nome da Filial_________________________
	def getNomeDaFilial(self):
		return self._nome_da_filial
	def setNomeDaFilial(self,nome_da_filial):
		self._nome_da_filial = nome_da_filial
		return True
	#________________________Endereco___________________________
	def getEndereco(self):
		return self._endereco
	def setEndereco(self,Endereco):
		self._endereco = Endereco
		return True
	#________________________Identificador______________________
	def getIdentificador(self):
		return self._identificador

	nome_da_filial = property(getNomeDaFilial(),setNomeDaFilial())
	Endereco = property(getEndereco(),setEndereco())
	identificador = property(getIdentificador())