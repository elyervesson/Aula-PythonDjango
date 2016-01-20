#!/usr/bin/env python
# encoding: utf-8

import sys

# chmod +x grep.py : Esse comando foi utilizado para dar permissão de execução
# ./grep.py 'dois' arq.txt teste.txt : Executa o 'search' nos arquivos (arq.txt teste.txt)
# sys.exit : Retorna um valor

FOUND = 0
NOT_FOUND = 1
ERROR = 2

def searchString(search, filename):
	f = open(filename) #Abre o arquivo
	for line in f:
		if search in line: #Verifica se o argumento procurado esta na linha
			yield line.strip() #Gera o iterador com todas as ocorrencias do 'search'
	f.close()

def main(args):
	search = args[1]
	filenames = args[2:]

	retorno = NOT_FOUND
	for filename in filenames:
		for line in searchString(search, filename):
			print "%s: %s" % (filename, line)
			retorno = FOUND
	
	return retorno
		
args = sys.argv
retorno = main(args)

sys.exit(retorno)

# OBS: A vantagem desse yield é que caso existam varias ocorrencias do
# 'search', se tivessimos usado uma lista para armazenar todas as ocorrencias
# poderia existir um estouro de memoria, porem, com o uso do yield cada vez
# que uma nova ocorrencia é encontrada  o comando 'print "%s: %s" % (filename, line)'
# é executado evitando assim o alocamento de memoria desnecessaria.
