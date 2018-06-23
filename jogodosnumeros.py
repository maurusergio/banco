class  JogoNumero():
        __int__(self):
        for i in range(2):
                print "*****************************************"
                print "++++++++++++++++++++++++++"
                print "	   JOGO DOS NUMEROS"
        def jogo(self):
		for i in range(2):
		print "++++++++++++++++++++++++++"
		print "*****************************************"
	print ""
	print "TENTE ACERTAR  O NUMERO ENTRE 1 e 100  :)"
	print ""
	print ""
	tentativas = 100
	num = randint(1,100)
	for i in range(tentativas):
		op = input("Qual o numero:  ")
		if op == num:
			print ""
			print "PARABENS  VOCE  ACERTOU!  o numero e:  %d" % num
			break
			jogo()
		elif op  > num:
			tentativas -= 1
			print ""
			print "Voce errou !! O numero eh MENOR !!"
			print ""
		elif op < num:
			print ""
			print "Voce errou !! O numero eh MAIOR !"
			print ""
		else:
			print " Opcao invalida"
			jogo()
