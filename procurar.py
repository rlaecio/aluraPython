# encoding: utf-8
# procurar.py palavra fich1 [fich2 ...]

import sys
progName = sys.argv[0]
if len(sys.argv) < 3:
   print("Erro, utilizacao: '%s palavra fich1 [fich2 ...]'" % progName)
   print("- procura 'palavra' nos ficheiros e imprime as linhas com ela")
   sys.exit(1)
palavra = sys.argv[1]
ficheiros = sys.argv[2:]
for umFicheiro in ficheiros:
   f = open(umFicheiro, "r",encoding="UTF-8")
   listaLinhas = f.readlines()
   for indiceLinha in range(len(listaLinhas)):
       umaLinha = listaLinhas[indiceLinha]
       if umaLinha.find(palavra) != -1:
           print("%s:%d %s" % (umFicheiro, indiceLinha+1, umaLinha[:-1]))
   f.close()
