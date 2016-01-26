#!/usr/bin/env python
# encoding: utf-8

# OBS: o uso do '_' (underline) antes do nome da variavel é uma conveção
# indica que essa variavel é privada (EX: _ponto = (1,1))

from math import sqrt

class Ponto(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return "P(%s, %s)" % (self.x, self.y)
		
	def distancia(self, p2):
		return sqrt( pow(p2.x - self.x, 2) + pow(p2.y - self.y, 2))
		
p1 = Ponto(10, 10)
p2 = Ponto(20, 15)

print p1, p2
print "d(P1, P2):", p1.distancia(p2)

#parei nos 9 min
