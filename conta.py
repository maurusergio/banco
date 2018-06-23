class Conta:
    global saldo,cpfdono,numero,tipo 
    saldo = 0

    def setNumero(self,numero):
        self.numero = numero
    def getNumero(self):
        return self.numero
    def setSaldo(self,valor):
        self.saldo = valor
    def getSaldo(self):
        return self.saldo
    def setDono(self,cpf):
        self.cpfdono = cpf
    def getDono(self):
        return self.cpfdono
    def saca(self,valor):
        self.saldo -= valor
    def deposita(self,valor):
        self.saldo += valor
    def setTipo(self, op):
        if op == 1:
            self.tipo = "Conta Corrente"
        elif op == 2:
            self.tipo = "Conta Poupanca"

    def getTipo(self):
        return self.tipo
    def movimento(self,valor):
        return self.valor

