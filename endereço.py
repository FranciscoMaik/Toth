class Endereco:
	__slots__ =['nome_da_rua','bairro','numero','cep']
    __init__(self,nome_da_rua,bairro,numero,cep):
    	self._nome_da_rua  = nome_da_rua
    	self._bairro = bairro
    	self._numero = numero
    	self._cep = cep
    #________________________nome da rua_____________________________

    def getNomeDaRua(self):
    	return self._nome_da_rua
    def setNomeDaRua(self,nome_da_rua):
    	self._nome_da_rua = nome_da_rua
    	return True
    #_________________________Bairro_________________________________

    def getBairro(self):
    	return self._bairro
    def setBairro(self,bairro):
    	self._bairro = bairro
    	return True
    #_________________________Numero__________________________________

    def getNumero(self):
    	return self._numero
    def setNumero(self,numero):
    	self._numero = numero
    	return True
    #_________________________________Cep______________________

    def getCep(self):
    	return self._cep
    def setCep(self,cep):
    	self._cep = cep
    	return True
    #_______________________propertys___________________________

    nome_da_rua = property(getNomeDaRua(),setNomeDaRua())
    bairro = property(getBairro(),setBairro())
    numero = property(getNumero(),setNumero())
    cep = property(getCep(),setCep())
        