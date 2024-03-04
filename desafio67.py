'''DESAFIO 67
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
O programa será interrompido quando o número solicitado for negativo'''
print('Informe numero negativo para encerrar o programa')
print('{:-^27}'.format('TABUADA'))
while True:
    num = int(input('Informe um número para ver a tabuada: '))
    if num < 0:
        break
    for cont in range (1, 11):
        print(f'{num} X {cont:2} = {cont*num}')
    print('-'*20)
print('Programa de tabuada encerrado!')