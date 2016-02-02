#!/usr/bin/env python
# encoding: utf-8

import pprint

notas = {
	"Graham Chapman": 5.5,
	"John Cleese": 7.0,
	"Terry Gilliam": 4.5,
	"Terry Jone": 4.5,
	"Eric Idle": 10,
	"Michael Palin": 3.5,
}
# Nome com 20 caracteres com alinhamento para esquerda

print "%-20s-+-%-7s" % ("-" * 20, "-" * 7)
print "%-20s | %-7s" % ("Nome", "Nota")
print "%-20s-+-%-7s" % ("-" * 20, "-" * 7)

soma = 0
contador = 0

for nome in sorted(notas):
	print "%-20s | %4.1f" % (nome, notas[nome])
	soma += notas[nome]
	contador += 1

print "%-20s-+-%-7s" % ("-" * 20, "-" * 7)
print "%-20s | %4.1f" % (u"Média", soma/(contador * 1.0))
print "%-20s-+-%-7s" % ("-" * 20, "-" * 7)
