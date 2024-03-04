'''DESAFIO 61
refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura do while'''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
qnt = 1
while qnt != 11:
    an = a1 + (qnt - 1)*r
    print('{} '.format(an), end="→ ")
    qnt += 1
print('ACABOU')