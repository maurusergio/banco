class Cliente:
    
    global nome,cpf,conta
    conta  = None
    
    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCpf(self,cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

    def setConta(self,numero):
        self.conta = numero

    def getConta(self):
        return self.conta
    
