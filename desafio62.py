'''DESAFIO 62
Melhore o desafio 61, perguntando se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser q quer mostrar 0 termos'''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
qnt = 1
while qnt != 11:
    an = a1 + (qnt - 1)*r
    print(' {} '.format(an), end='')
    qnt += 1

mais = int(input('\nQuer que mostre mais quantos termos? '))
mostrou = 0
total = 10
while mais != 0:
    an = a1 + (qnt - 1)*r
    print(' {} '.format(an), end=' ')
    total += 1
    mostrou += 1
    qnt += 1
    if mostrou == mais:
        mostrou = 0
        mais = int(input('\nQuer que mostre mais quantos termos? '))
print('ACABOU! No total foram mostrados {} termos'.format(total))