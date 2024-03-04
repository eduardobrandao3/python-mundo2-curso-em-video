'''DESAFIO 45
Faça o computador jogar jokenpô com você'''

from random import choice
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaPc = choice(lista)
print('-=-'*10)
print('{:^30}'.format('JOKENPÔ'))
print('-=-'*10)

jogador = str(input('Escolha entre "pedra", "papel" ou "tesoura": ')).upper().strip()
if (jogador == 'PEDRA') or (jogador == 'PAPEL') or (jogador == 'TESOURA'):
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ')
    print('Eu escolhi {} e você escolheu {}'.format(escolhaPc, jogador))
    if escolhaPc == jogador:
        print('EMPATE')
    elif escolhaPc == 'PEDRA':
        if jogador == 'PAPEL':
            print('\033[32mVOCÊ VENCEU!\033[m')
        elif jogador == 'TESOURA':
            print('\033[31mVOCÊ PERDEU!\033[m')
    elif escolhaPc == 'PAPEL':
        if jogador == 'TESOURA':
            print('\033[32mVOCÊ VENCEU!\033[m')
        elif jogador == 'PEDRA':
            print('\033[31mVOCÊ PERDEU!\033[m')
    elif escolhaPc == 'TESOURA':
        if jogador == 'PEDRA':
            print('\033[32mVOCÊ VENCEU!\033[m')
        elif jogador == 'PAPEL':
            print('\033[31mVOCÊ PERDEU!\033[m')
else: 
    print('OPÇÃO INVÁLIDA!')
    
