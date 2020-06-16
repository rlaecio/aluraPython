import random

print('*****************************************')
print('Bem vindo ao nosso programa de advinhação')
print('*****************************************')

numero_secreto = round(random.randrange(0, 101))

total_de_tentativas = 30



for rodadas in range(1, total_de_tentativas+1):
    print('Tetativa: {} de {} '.format(rodadas, total_de_tentativas))
    chute = int(input('Digite um numero entre 1 e 100: '))
    if (chute < 1 or chute > 100):
        print('Você deve digitar um numero entre 1 e 101 ')
        continue

    acertou = (numero_secreto == chute)
    nMaior = chute > numero_secreto
    nMenor = chute < numero_secreto


    if (acertou):
        print('Você acertou!')
        break
    else:
        if(nMaior):
            print('Você errou! O seu numero foi maior que o numero secreto')
        elif(nMenor):
            print('Você errou! O seu numero foi menor que o numero secreto')


print('Fim do Jogo')
