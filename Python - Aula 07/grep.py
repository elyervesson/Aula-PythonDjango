#!/usr/bin/env python
# encoding: utf-8

import sys

# chmod +x grep.py : Esse comando foi utilizado para dar permissão de execução
# ./grep.py 'dois' arq.txt teste.txt : Executa o 'search' nos arquivos (arq.txt teste.txt)
# sys.exit : Retorna um valor

FOUND = 0
NOT_FOUND = 1
ERROR = 2

# Criação de uma excessão
class MinhaException(Exception): 
	pass
	
def searchString(search, filename):
	f = open(filename) #Abre o arquivo
	for line in f:
		if search in line: #Verifica se o argumento procurado esta na linha
			yield line.strip() #Gera o iterador com todas as ocorrencias do 'search'
	f.close()

def main(args):
	try:
		search = args[1]
	except IndexError:
		print >>sys.stderr, "Usage: grep [OPTION]... PATTERN [FILE]..."
		return ERROR
		
	filenames = args[2:]

	retorno = NOT_FOUND
	for filename in filenames:
		try:
			for line in searchString(search, filename):
				print "%s: %s" % (filename, line)
				retorno = FOUND
		except IOError, ex:
			print >>sys.stderr, "grep.py: %s: %s" % (ex.filename, ex.strerror)
			retorno = ERROR
			
	return retorno
		
args = sys.argv
retorno = main(args)

sys.exit(retorno)

# OBS: A vantagem desse yield é que caso existam varias ocorrencias do
# 'search', se tivessimos usado uma lista para armazenar todas as ocorrencias
# poderia existir um estouro de memoria, porem, com o uso do yield cada vez
# que uma nova ocorrencia é encontrada  o comando 'print "%s: %s" % (filename, line)'
# é executado evitando assim o alocamento de memoria desnecessaria.
