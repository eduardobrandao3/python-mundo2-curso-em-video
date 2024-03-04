'''DESAFIO 51
leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa PROGRESSÃO'''

#an = a1 + (n-1)*r
a1 = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
for cont in range(1, 11):
    an = a1 + (cont - 1)*r
    print('{} \032'.format(an), end=' ')
print('ACABOU')
