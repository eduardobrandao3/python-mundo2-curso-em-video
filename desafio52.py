'''DESAFIO 52 
faça um programa q leia um número int e diga se ele é ou não número primo'''

divisores = 0
num = int(input('Digite um número inteiro: '))

if num <= 1:
    print('O número {} \033[31mNÃO\033[m é primo'.format(num))
else: 
    for cont in range(1, num+1):
        if num % cont == 0:
            divisores +=1
            print('\033[33m{}\033[m'.format(cont), end=' ')
        else:
            print('\033[31m{}\033[m'.format(cont), end=' ')
    if divisores == 2:
        print('\nO número {} é \033[32mPRIMO\033[m'.format(num))
    else:
        print('\nO número {} \033[31mNÃO\033[m é primo'.format(num))
    print('Pois o número {} foi divisível {} vezes'.format(num, divisores))