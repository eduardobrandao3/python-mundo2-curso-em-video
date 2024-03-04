'''DESAFIO 60
leia um número qualquer e mostre o seu fatorial
faça com while e com for'''

num = int(input('Digite um número para obter seu fatorial: '))
fatorial = num
mult = num - 1
if num < 0:
    print('Número negativo não tem fatorial!')
elif num == 0:
    print('0! = 1')
else:
    while mult != 0:
        fatorial *= mult
        mult -= 1
    print('{}! = {}'.format(num, fatorial))


#UTILIZANDO FOR
'''num = int(input('Digite um número para saber seu fatorial: '))
fatorial = num
if num < 0:
    print('Número negativo não tem fatorial!')
elif num == 0:
    print('0! = 1')
else:
    for mult in range(num-1, 0, -1):
        fatorial = fatorial * mult
    print('{}! = {}'.format(num, fatorial))'''