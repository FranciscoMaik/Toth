class Endereco:
    __init__(self,nome_da_rua,bairro,numero,cep):
    	self._nome_da_rua  = nome_da_rua
    	self._bairro = bairro
    	self._numero = numero
    	self._cep = cep
    def getNomeDaRua(self):
    	return self._nome_da_rua
    def setNomeDaRua(self,nome_da_rua):
    	self._nome_da_rua = nome_da_rua
    def getBairro(self):
    	return self._bairro
    def setBairro(self,bairro):
    	self._bairro = bairro
    def getNumero(self):
    	return self._numero
    def setNumero(self,numero):
    	self._numero = numero
    def getCep(self):
    	return self._cep
    def setCep(self,cep):
    	self._cep = cep
    nome_da_rua = property(getNomeDaRua(),setNomeDaRua())
    bairro = property(getBairro(),setBairro())
    numero = property(getNumero(),setNumero())
    cep = property(getCep(),setCep())
        