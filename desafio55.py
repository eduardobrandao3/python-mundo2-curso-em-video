'''DESAFIO 55
Leia o peso de 5 pessoas e no final mostre o maior e o menor '''

maior = -1
menor = 1000000000

for cont in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em kg: '.format(cont)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('''Entre os pesos digitados
{:.2f} kg foi o maior peso lido
{:.2f} kg foi o menor peso lido'''.format(maior, menor))