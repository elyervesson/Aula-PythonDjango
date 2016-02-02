#!/usr/bin/env python
# encoding: utf-8

import sys

# chmod +x grep.py : Esse comando foi utilizado para dar permissão de execução
# ./grep.py 'dois' arq.txt teste.txt : Executa o 'search' nos arquivos (arq.txt teste.txt)

# Todos os argumentos eparametros passados para 
# o nosso programa estaram dentro dessa lista argv

search = sys.argv[1]
filenames = sys.argv[2:]

for filename in filenames:
	f = open(filename) #Abre o arquivo
	for line in f:
		if search in line: #Verifica se o argumento procurado esta na linha
			print "%s: %s" % (filename, line.strip())
	f.close()
