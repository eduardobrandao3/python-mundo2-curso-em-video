'''DESAFIO 65
leia varios numeros inteiros. No final mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''

total = 0
soma = 0
resp = 'S'
while resp == 'S':
    num = int(input('Digite um número inteiro: '))
    total += 1
    soma += num
    if total == 1:
        maior = num
        menor = num
    else: 
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer digitar outro número [S/N]: ')).strip().upper()[0]

media = soma / total
print('Você digitou {} números e a média foi é {}'.format(total, media))
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))
