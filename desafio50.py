'''DESAFIO 50
Leia 6 númeiros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o'''

somaPar = 0
qnt = 0
for cont in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        somaPar += num
        qnt += 1
print('Você digitou {} números pares e a soma entre eles vale {}'.format(qnt, somaPar))