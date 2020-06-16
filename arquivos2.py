#encoding UTF-8
'''
Created on 11 de jul de 2017

@author: rsouza
'''
arquivo = open('tabela2.txt','w')
for i in range(100):
    arquivo.write('%i dolares valem %.2f reais \n' %(i, i*3.14))
arquivo.close()

