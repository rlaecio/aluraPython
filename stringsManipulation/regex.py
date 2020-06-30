import re

'''
email1 = "Meu numero de telefone é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "961234-1234 é o meu telefone"

padrao = "[0-9]{4,5}[-][0-9]{4}"

retorno = re.search(padrao, email3)
print(retorno.group())

print("\n --------------------------------------------------- \n")

padrao = "e[0-9]{1,2} [s,t][0-9]{1,2}"
conversa1 = "Estou no e 1 t 3 de Naruto"
conversa2 = "O e02 t2 é o melhor de Rick and Morty"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Boku no Hero é o e011 s02"

retorno = re.search(padrao, conversa3)
print(retorno.group())

print("\n --------------------------------------------------- \n") 

padrao1 = "[a-z]{20}[][0-9]{1,2}[h]"
padrao2 = "[a-z]{1,20}[][0-9]{1,2}[h]"
padrao3 = "[a]{1,20}[][0-9]{3}"


frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

retorno = re.search(padrao2, frase2)
print(retorno.group())
'''