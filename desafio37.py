'''DESAFIO 37
leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
1 - binário
2 - octal
3 - hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma oção para conversão: 
[ 1 ] - converter para BINÁRIO
[ 2 ] - converter para OCTAL
[ 3 ] - converter para HEXADECIMAL''')
opcao = int(input('Opção escolhida: '))
if opcao == 1:
    print('{} convertido para BINÁRIO vale {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL vale {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL vale {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA!')

