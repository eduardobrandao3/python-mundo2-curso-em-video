'''DESAFIO 64
Leia varios numeros inteiros. so para quando usuário digitar 999, que é a condição de parada
no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

num = 0
soma = 0
total = 0
while num != 999:
    num = int(input('Digite um valor inteiro [999 para parar]: '))
    if num != 999:
        total += 1
        soma += num
print('No total você digitou {} números e a soma entre eles é {}'.format(total, soma))