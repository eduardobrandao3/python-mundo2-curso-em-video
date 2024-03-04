'''DESAFIO 68
Jogar par ou ímpar com o computador
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele teve'''

from random import randint
vitorias = 0
while True:
    print('{:-^40}'.format('JOGO DE PAR OU IMPAR'))
    pc = randint(0, 10)
    soma = 0
    escolha = str(input('Par ou impar [P/I]? ')).strip().upper()[0]
    while escolha not in 'PI':
        print('Opção invalida!')
        escolha = str(input('Par ou impar [P/I]? ')).strip().upper()[0]
    jogador = int(input('Digite um valor: '))
    soma = pc + jogador
    print(f'Eu escolhi {pc} e você {jogador}')
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'Você \033[32m,venceu\033[m, pois {pc} + {jogador} = {soma} e é PAR')
            vitorias += 1
        else:
            print(f'Você \033[31mperdeu\033[m, pois {pc} + {jogador} = {soma} e é ÍMPAR ')
            break
    else:
        if soma % 2 != 0:
            print(f'Você \033[32mvenceu\033[m, pois {pc} + {jogador} = {soma} e é ÍMPAR')
            vitorias += 1
        else: 
            print(f'Você \033[31mperdeu\033[m, pois {pc} + {jogador} = {soma} e é PAR ')
            break
print(f'Você ganhou {vitorias} vezes consecutivas')