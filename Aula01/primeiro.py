#!/usr/bin/env python
# -*- encoding utf-8 -*-
# primeiro.py - Nosso primeiro programa python

import random

numero = random.randint(1, 100)

tentativas = 0
escolha = 0

while escolha != numero:
	escolha = input("Informe um numero entre 1 e 100: ")
	tentativas += 1
	if escolha > numero:
		print "Maior"
	elif escolha < numero:
		print "Menor"

print "Acertou!!! O numero sorteado era", numero
print "Voce usou", tentativas, "tentativas"