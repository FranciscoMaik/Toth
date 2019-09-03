class Loja:
	__slots__ = ['_nome_da_filial','_identificador','_endereco']
	def __init__(self,nome_da_filial,identificador,Endereco):
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
	#_______________________propertys___________________________

	nome_da_filial = property(getNomeDaFilial,setNomeDaFilial)
	Endereco = property(getEndereco,setEndereco)
	identificador = property(getIdentificador)
if __name__ == '__main__':
	loj = Loja("Nome","identificador","Endereco completo")
	print(loj.nome_da_filial,loj.identificador)