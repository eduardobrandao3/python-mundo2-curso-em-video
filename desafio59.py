'''DESAFIO 59
Crie um programa q leia dois valores e mostre na tela um menu
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa'''

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('{:-^28}'.format('MENU'))
    print('''[1] Somar
[2] Multiplicar
[3] Mostrar maior
[4] Digitar novos números
[5] Sair do programa''')
    opcao = int(input('OPÇÃO: '))
    print('-'*28)
    if opcao == 1:
        print('SOMA:\n{} + {} = {}\n'.format(v1, v2, (v1 + v2)))
    elif opcao == 2:
        print('MULTIPLICAÇÃO:\n{} X {} = {}\n'.format(v1, v2, (v1*v2)))
    elif opcao == 3:
        print('MOSTRAR O MAIOR:')
        if v1 > v2:
            print('{} é maior que {}\n'.format(v1, v2))
        elif v2 > v1:
            print('{} é maior que {}\n'.format(v2, v1))
        else:
            print('{} e {} são iguais\n'.format(v1, v2))
    elif opcao == 4:
        print('DIGITAR NOVOS VALORES:')
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('SAINDO DO PROGRAMA...')
    else: 
        print('OPÇÃO INDISPONÍVEL!\n')
