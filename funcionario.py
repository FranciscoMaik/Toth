class Funcionario:
	__slots__ = ['_nome_do_funcionario', '_cpf', '_numero_de_telefone', '_endereco']
	def __init__(self,nome_do_funcionario,cpf,numero_de_telefone,endereco):
		self._nome_do_funcionario = nome_do_funcionario
		self._cpf = cpf
		self._numero_de_telefone = numero_de_telefone
		self._endereco = endereco
	#_________________________________nome do funcionario______________________

	def getNomeDoFuncionario(self):
		return self._nome_do_funcionario
	def setNomeDoFuncionario(self,nome_do_funcionario):
		self._nome_do_funcionario = nome_do_funcionario
		return True
	#____________________________numero telefone_________________________________

	def getNumeroDeTelefone(self):
		return self._numero_de_telefone
	def setNumeroDeTelefone(self,numero_de_telefone):
		self._numero_de_telefone = numero_de_telefone
	#__________________________cpf_____________________________

	def getCpf(self):
		return self._cpf
	def setCpf(self,cpf):
		self._cpf = cpf
	#________________________Endereco___________________________

	def getEndereco(self):
		return self._endereco
	def setEndereco(self,Endereco):
		self._endereco = Endereco
		return True
	#_______________________propertys___________________________

	nome_do_funcionario = property(getNomeDoFuncionario,setNomeDoFuncionario)
	cpf = property(getCpf,setCpf)
	numero_de_telefone = property(getNumeroDeTelefone,setNumeroDeTelefone)
	endereco = property(getEndereco,setEndereco)
if __name__ == '__main__':
	func = Funcionario("nome dele","Cpf","numero","Endereco")
	print(func.cpf)