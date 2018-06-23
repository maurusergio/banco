# encoding: utf-8      //-----
# encoding: iso-8859-1 //-----|---> https://pt.stackoverflow.com/questions/67604/encoding-utf-8-permite-acentos
# encoding: win-1252   //-----
#from contacorrente import Corrente
#from poupanca import Poupanca
from cliente import Cliente
from random import randint
from datetime import datetime
from conta import Conta
from extrato import Extrato
now = datetime.now()
global clientes
global contas
global extratos
clientes = []
contas = []
extratos = []

class Principal:
    
    def __init__(self):
        for i in range(500):
            print " "
        print "                 ###### BANCO SPRING S/A ######"
        print ""
        print ""
        
    def cadastra(self):
        Principal().__init__()
        print "                 ++++++++++++++++++++++++++++++"
        print "                 +     CADASTRO DE CLIENTE    +"
        print "                 ++++++++++++++++++++++++++++++"
        print ""
        print ""
        cli = Cliente()
        nome = raw_input("                 Digite seu nome: ")
        cpf = raw_input("                 Digite seu Cpf: ")
        print ""
        print ""
        #raw_input("                 Confirmar cadastro [enter]")
        Principal().__init__()
        print "                 ++++++++++++++++++++++++++++++"
        print "                 +     CADASTRO DE CLIENTE    +"
        print "                 ++++++++++++++++++++++++++++++"
        print ""
        print ""
        print "                 Cliente: ",nome.swapcase()
        print "                 Cpf: %s" % cpf
        print ""
        cli.setNome(nome.swapcase())
        cli.setCpf(cpf)
        clientes.append(cli)
        print ""
        print "                 cadastrado efetuado com sucesso !"
        print ""
        raw_input("                 Pressione Enter pra continuar.")
        Principal().menu0()
    def criaconta(self,cpf):
            print "                 ++++++++++++++++++++++++++++++"
            print "                 +     CADASTRO DE CONTA    +"
            print "                 ++++++++++++++++++++++++++++++"
            print ""
            for i in range(len(clientes)):
                if cpf == clientes[i].getCpf():
                    print "                 Cliente: %s" % clientes[i].getNome()
                    print "                 Cpf: %s" % clientes[i].getCpf()
                    print ""
                    print ""
                    print "                 *** Escolha o Tipo de conta ***"
                    print ""
                    print "                 1 - Conta Corrente"
                    print "                 2 - Conta Poupanca"
                    print " "
                    p = Conta()
                    c = Conta()
                    tipo = input("                 Opção: ")
                    if tipo == 1:
                        c.setNumero(randint(1000,2000))
                        c.setTipo(tipo)
                        c.setDono(cpf)
                        c.setSaldo(0)
                        contas.append(c)
                    elif tipo == 2:
                        p.setNumero(randint(1000,2000))
                        p.setTipo(tipo)
                        p.setDono(cpf)
                        p.setSaldo(0)
                        contas.append(p)
                    else:
                        print "Opção Incorreta"
                        Principal().criaconta()
                    
                    Principal().__init__()
                    print "                 ++++++++++++++++++++++++++++++"
                    print "                 +     CADASTRO DE CONTA    +"
                    print "                 ++++++++++++++++++++++++++++++"
                    print ""
                    print "                 Cliente: %s" % clientes[i].getNome()
                    print "                 Cpf: %s" % clientes[i].getCpf()
                    print ""
                    print ""
                    for i in range(len(contas)):
                        if cpf == contas[i].getDono():
                            print "                 Numero da Conta: %d" % contas[i].getNumero()
                            print "                 Tipo: %s" % contas[i].getTipo()
                            print "                 Saldo atual: R$ %d,00 " % contas[i].getSaldo()
                            print ""
                            print ""

            print "                 Conta criada com sucesso !"
            print ""
            print "                 1 - Criar Nova Conta"
            print "                 2 - Voltar ao Menu Principal"
            print ""
            op7 = input("                 Escolha uma Opção: ")
            if op7 == 1:
                Principal().criaconta(cpf)
            elif op7 == 2:
                Principal().menu0()
            else:
                print "Opção Incorreta"
                Principal().menu0()
    def deposita(self):
            Principal().__init__()
            print "                 ++++++++++++++++++++++++++++++"
            print "                 +          DEPOSITO          +"
            print "                 ++++++++++++++++++++++++++++++"
            print ""
            print ""
            print ""
            print ""
            a = True
            while a == True:
                cnum = input("                 Numero da Conta: ")
                valor = input("                 Valor do deposito R$: ")
                for i in range(len(contas)):
                    if cnum == contas[i].getNumero():
                        Principal().__init__()
                        print "                 ++++++++++++++++++++++++++++++"
                        print "                 +          DEPOSITO          +"
                        print "                 ++++++++++++++++++++++++++++++"
                        print ""
                        print ""
                        print "                 Tipo: ",contas[i].getTipo()
                        print "                 Cliente: ",contas[i].getDono()
                        print "                 Numero da Conta:",contas[i].getNumero()
                        print "                 Valor: R$ %d,00" % valor
                        print " "
                        raw_input("                 Confirmar deposito [Enter]")
                        contas[i].deposita(valor)
                        extrato = Extrato()
                        extrato.setValor(valor)
                        extrato.setData(datetime.now())
                        extrato.setMov("deposito")
                        extrato.setNumconta(contas[i].getNumero())
                        extratos.append(extrato)
                        a = False
                        
                    else:
                        print ""
                        print ""
                        print "                 *** Conta inexistente ! ***"
                        print ""
                        print ""
                        print "                 1 - Sair"
                        print "                 2 - Tentar Novamente"
                        print ""
                        op6 = input("                 Opção: ")
                        if op6 == 1:
                            Principal().menu0()
                        elif op6 == 2:
                            Principal().deposita()
                        else:
                            print "                 Opção Incorreta"
                            continue
                        print "                 Dados incorretos"
            print " "
            print "                 Depósito efetuado com sucesso !"
            print " "
            raw_input("                 Pressione Enter pra continuar.")
            Principal().menu0()
    def saca(self):
            Principal().__init__()
            print "                 ++++++++++++++++++++++++++++++"
            print "                 +           SAQUE            +"
            print "                 ++++++++++++++++++++++++++++++"
            print ""
            print ""
            print ""
            c = Conta()
            a = True
            while a == True:
                cnum = input("                 Numero da Conta: ")
                valor = input("                 Valor do saque R$: ")
                for i in range(len(contas)):
                    if cnum == contas[i].getNumero():
                        Principal().__init__()
                        print "                 ++++++++++++++++++++++++++++++"
                        print "                 +           SAQUE            +"
                        print "                 ++++++++++++++++++++++++++++++"
                        print ""
                        print "                 Tipo: ",contas[i].getTipo()
                        print "                 Numero da conta: ",contas[i].getNumero()
                        print "                 Cliente: ",contas[i].getDono()
                        print "                 Valor: R$ %d,00" % valor
                        saldoatual = contas[i].getSaldo()
                        print ""
                        print ""
                        print ""
                        raw_input("                 Confirmar saque [Enter]")
                        if saldoatual < valor:
                            print '                 Saldo Insuficiente !'
                            print ""
                            raw_input("                 Pression Enter pra continuar...")
                            Principal().menu0()
                        else:
                            contas[i].saca(valor)
                            mov = Extrato()
                            mov.setNumconta(contas[i].getNumero())
                            mov.setData(now.day,now.month,now.year)
                            mvo.setMovimento("saque............ - ")
                            mov.setValor(valor)
                            extratos.append(mov)
                        a = False
                        break
                    else:
                        print ""
                        print ""
                        print "                 *** Conta inexistente ! ***"
                        print ""
                        print ""
                        #raw_input("                 Press enter")
                        print "                 1 - Sair"
                        print "                 2 - Tentar Novamente"
                        print ""
                        op5 = input("                 Opção: ")
                        if op5 == 1:
                            Principal().menu0()
                        elif op5 == 2:
                            Principal().saca()
                        else:
                            print "                 Opção Incorreta"
                            continue
            raw_input("                 Pressione enter pra continuar.")
            Principal().menu0()
    def saldo(self):
            Principal().__init__()
            print "                 ++++++++++++++++++++++++++++++"
            print "                 +     CONSULTA DE SALDO      +"
            print "                 ++++++++++++++++++++++++++++++"
            print ""
            print ""
            print ""
            print ""
            a = True
            while a:
                cnum = input("                 Numero da Conta: ")
                for i in range(len(contas)):
                    if cnum == contas[i].getNumero():
                        Principal().__init__()
                        print "                 ++++++++++++++++++++++++++++++"
                        print "                 +     CONSULTA DE SALDO      +"
                        print "                 ++++++++++++++++++++++++++++++"
                        print ""
                        print ""
                        print "                 Tipo: ",contas[i].getTipo()
                        print "                 Numero da conta: ",contas[i].getNumero()
                        print "                 Cliente: ",contas[i].getDono()
                        print "                 Saldo Atual: R$ %d,00" % contas[i].getSaldo()
                        
                        a = False
                        break
                    else:
                        
                        print "                 *** Conta inexistente ! ***"
                        print ""
                        print ""
                        #raw_input("                 Press enter")
                        print "                 1 - Sair"
                        print "                 2 - Tentar Novamente"
                        print ""
                        op4 = input("                 Opção: ")
                        if op4 == 1:
                            Principal().menu2()
                        elif op4 == 2:
                            Principal().saldo()
                        else:
                            print "                 Opção Incorreta"
                            continue
            print ""
            print ""
            raw_input("                 Pressione enter pra continuar.")
            Principal().menu0()
    def listaclientes(self):
            Principal().__init__()
            if len(clientes) == 0:
                print "                 Nenhum cliente cadastrado !"
                print ""
                print ""
                raw_input("                 Enter para continuar: ")
                print ""
                print ""
                Principal().menu0()
            else:
                Principal().__init__()
                print "                 ++++++++++++++++++++++++++++++"
                print "                 +    Clientes Cadastrados    +"
                print "                 ++++++++++++++++++++++++++++++"
                print ""
            
                for i in range(len(clientes)):
                    print '                 %d - Nome: %s' % (i,clientes[i].getNome())
                    print "                     Cpf: %s" % clientes[i].getCpf()    
                print " "
                print " "
                raw_input("                 Pressione Enter pra continuar.")
                Principal().menu0()
            
    def listacontas(self):
            Principal().__init__()
            print "                 ++++++++++++++++++++++++++++++"
            print "                 +     Contas Cadastradas     +"
            print "                 ++++++++++++++++++++++++++++++"
            print ""
            for i in range(len(contas)):
                for l in range(len(clientes)):
                    if contas[i].getDono() == clientes[i].getCpf():
                        print "                 ----------- CONTA--------------"
                        print "                 Cliente: %s" % clientes[i].getNome()
                        print "                 Cpf: %s" % clientes[i].getCpf()
                        print " "
                        print "                 Tipo: %s" % contas[i].getTipo()
                        print "                 Numero da Conta: %d" % contas[i].getNumero()
                        print "                 Saldo atual: %s,00" % contas[i].getSaldo()
                        print "                 ------------------------------"
                        break

            print " "
            raw_input("                 Pressione Enter pra continuar.")
            Principal().menu0()
    def busca(self):
        print "                 +++++++++++++++++++++++++++++++"
        print "                 +      BUSCA DE CLIENTE       +"
        print "                 +++++++++++++++++++++++++++++++"
        print " "
        print " "
        cpf = raw_input("                 Digite o CPF: ")
        for i in range(len(clientes)):
            if cpf.swapcase() == clientes[i].getCpf().swapcase():
                Principal().__init__()
                print ""
                print "                 Cliente: ",clientes[i].getNome()
                print "                 Cpf: ",clientes[i].getCpf()
                print ""
                for l in range(len(contas)):
                    if contas[l].getDono() == clientes[i].getCpf():
                        print "                 Conta: ",contas.getTipo()
                        print "                 Numero: ",contas.getNumero()
                        print "                 Saldo: ",contas.getSaldo()
                print ""
                print ""
                print "                 1 - Criar conta"
                print "                 2 - Sair"
                print ""
                print ""
                op3 = input("                 Opção: ")
                if op3 == 1:
                    Principal().criaconta(cpf)
                elif op3 == 2:
                    Principal().menu0()
                else:
                    print "                 Opção Invalida"
                    raw_input("                 Pressione enter")
                    Principal().menu0()

            else:
                print ""
                print ""
                print "                 *** Cliente nao encontrado ! ***"
                print ""
                print "                 1 - Nova busca"
                print "                 2 - Sair"
                print ""
                print ""
                op2 = input("                 Opção: ")
                if op2 == 1:
                    Principal().busca()
                elif op2 == 2:
                    Principal().menu0()
                else:
                    print "                 Opção incorreta"
                    Principal().menu0()
    def extrato(self,contaNum):
        Principal().__init__()
        print "                 ++++++++++++++++++++++++++++++"
        print "                 +           EXTRATO           +"
        print "                 ++++++++++++++++++++++++++++++"
        print ""
        print ""
        print ""
       # op5 = raw_input("Digite o numeo da conta: ")
        for i in range(len(extratos)):
            if len(extratos) == 0:
                print "                 Nenhum movimento cadastrado !"
                print ""
                raw_input("                 Pressione [Enter] pra continuar...")
                Principal().menu2()

            elif contaNum == extratos[i].getNumconta():
                Principal().__init__()
                print "                 ++++++++++++++++++++++++++++++"
                print "                 +           EXTRATO           +"
                print "                 ++++++++++++++++++++++++++++++"
                print ""
                print ""
                print ""
                print "                 Conta: %s" % contas[i].getNumconta
                print "                 Cliente: %s" % clientes[i].getNome()
                print "                 Data: %s/%s/%s/" % extratos[i].getData().day, extratos[i].getData().month, extratos[i].getData().month
                print "                 %sR$ %s,00" % extratos[i].getMovimento(), extratos[i].getValor()
            else:
                print ""
                print "                 Conta inexistente"
                print ""
                raw_input("Pression enter para continuar...")
                Principal().menu0()
    
    def menu0(self):
        print "                 +++++++++++++++++++++++++++++++"
        print "                 |     ESCOLHA SUA POSIÇÃO     |"
        print "                 +++++++++++++++++++++++++++++++"
        print " "
        print " "
        print "                 -------------------------------"
        print "                 |      1 - BANCO               |"
        print "                 -------------------------------"
        print ""
        print "                 -------------------------------"
        print "                 |    2 -CAIXA ELETRÔNICO       |"
        print "                 -------------------------------"
        print ""
        op0 = input("                   Escolha sua opcao: ")
        if op0 == 1:
            Principal().menu1()
        elif op0 == 2:
            Principal().menu2()
        else:
            print "                 Opcao invalida !"
            Principal().menu0()

    def menu1(self):
        
        print " "
        print " "
        print "                 -------------------------------"
        print "                 |          BANCO               |"
        print "                 -------------------------------"
        print "                 1 - Cadastrar Cliente"
        print "                 2 - Criar Conta"
        print "                 3 - Listar Clientes"
        print "                 4 - Total de Contas"
        print "                 5 - Buscar Clientes"
        print "                 6 - Lista de Contas"
        print ""

        op1 = input("                 Escolha uma Opção: ")


        if op1 == 3:
            Principal().listaclientes()
        elif op1 == 1:
            Principal().cadastra()
        elif op1 == 4:
                Principal().__init__()
                print "                 Contas cadastradas: %d" % len(contas)
                print ""
                print ""
                raw_input("                 Pressione [Enter] pra continuar...")
                Principal().menu0()
        elif op1 == 5:
            Principal().busca()
        elif op1 == 6:
            Principal().listacontas()
        elif op1 == 2:
            cpf = raw_input("                 Digite o Cpf aperte [Enter]: ")
            if len(clientes) == 0:
                Principal().__init__()
                print "                 Nenhum clientes cadastrado !"
                print ""
                print ""
                raw_input("                 Pressione [Enter] pra continuar...")
                Principal().menu0()
            elif len(clientes) > 0:
                for i in range(len(clientes)):
                    if cpf == clientes[i].getCpf():
                        Principal().criaconta(cpf)
                    else:
                        Principal().__init__()
                        print "                 Cliente não cadastrado !"
                        print ""
                        print "                 Cadastrar cliente ? escolha s:(sim), n:(não)"
                        print ""
                        op2 = raw_input("                   Opção: ")
                        if op2 == "s" :
                            Principal().cadastra()
                        elif op2 == "n":
                            Principal().menu0()
                        else:
                            print "                 Opção incorreta !"
                            Principal().menu0()

            else:
                print "                 Opção inválida !"
                Principal().menu0()
    def menu2(self):

        print "                 -------------------------------"
        print "                 |       CAIXA ELETRÔNICO       |"
        print "                 -------------------------------"
        print "                 7 - Deposito"
        print "                 8 - Saque"
        print "                 9 - Saldo"
        print "                 10 - Extrato"
        print ""
        op3 = input("                 Escolha uma Opção: ")
        
        if op3 == 7:
            Principal().deposita()
        
        elif op3 == 8:
            Principal().saca()
        
        elif op3 == 9:
            Principal().saldo()

        elif op3 == 10:
            num = raw_input("numero da conta: ")
            Principal().extrato(num)

            
        
      
        
        
