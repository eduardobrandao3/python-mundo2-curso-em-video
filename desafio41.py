'''DESAFIO 41
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
-ate 9 anos: MIRIM
-ate 14 anos: INFANTIL
-ate 19 anos: JUNIOR
-ate 20 anos: SÊNIOR
-Acima: MASTER'''

from datetime import date
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade <= 9:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é SÊNIOR')
else:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é MASTER')