from datetime import date
class Extrato:
	
	# ATRIBUTOS

	global dia,mes,ano,hora,movimento,numconta,data

	# METODOS

	def setData(self,data):
		self.data = data 

	def getData(self):
		return self.data

	def setValor(self,valor):
		self.valor = valor

	def getValor(self):
		return self.valor
	def setDia(self,dia):
		self.dia = dia

	def getDia(self):
		return self.dia

	def setMes(self,mes):
		self.mes = mes
	def getMes(self):
		return self.mes

	def setAno(self,ano):
		self.ano = ano	
	def getAno(self):
		return self.ano

	def setHora(self,hora):
		self.hora = hora
	def getHora(self):
		return self.hora

	def setMov(self,mov):
		self.movimento = mov
	def getMov(self):
		return self.movimento

	def setNumconta(self,numero):
		self.numconta = numero
	def getNumconta(self):
		return self.numconta