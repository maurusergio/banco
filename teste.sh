#!/usr/bin/python

from cliente import Cliente
from conta import Conta
from extrato import Extrato
from menu import Menu
from principal import Principal

for i in range(20):
	c = Conta()
	c.setNome("Mauro")
	c.setCpf("7545")
