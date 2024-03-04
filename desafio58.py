'''DESAFIO 58
Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
pc = randint(0, 10)
palpites = 0
print('{:-^29}'.format('JOGO DE ADIVINHAÇÃO'))
print('Eu escolhi um número inteiro entre 0 e 10\nTente adivinhar')
jogador = -1

while jogador != pc:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador != pc:
        if jogador < pc:
            print('Mais...', end=' ')
        else:
            print('Menos...', end=' ')
        print('Tente novamente')
        print('-'*30)
    else:
        print('ACERTOU!')
print('Você precisou de {} tentativas para acertar'.format(palpites))