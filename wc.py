# encoding: utf-8
# wc.py fich1 [fich2 ...]
# imprime nº de carateres, palavras e linhas

import sys
progName = sys.argv[0]
if len(sys.argv) < 2:
  print("Erro, utilizacao: '%s fich1 [fich2 ...]'" % progName)
  print("- conta carateres, palavras e linhas nos ficheiros")
  sys.exit(1)
ficheiros = sys.argv[1:]

for umFicheiro in ficheiros:
  f = open(umFicheiro, "r",encoding="UTF-8")
  listaLinhas = f.readlines()
  linhas = len(listaLinhas)
  palavras = len("".join(listaLinhas).split())
  carateres = len("".join(listaLinhas))
  print("%s: %d linhas %d palavras %d carateres" % (umFicheiro,
                                                     linhas, palavras, carateres))
  f.close()
