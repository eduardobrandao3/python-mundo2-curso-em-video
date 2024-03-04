'''DESAFIO 66
Ler vários números inteiros. Só para quando o usuário digitar o número 999 (condição de parada)
No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

total = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break
    total += 1
    soma += num
print(f'Você digitou {total} números e a soma entre eles vale {soma}')