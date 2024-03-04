'''DESAFIO 53
Leia uma frase qualquer e diga se ela é palíndromo, desconsiderando espaços'''

frase = str(input('Digite uma frase: ')).strip().upper()
dividido = frase.split()
junto = ''.join(dividido)
tam = len(junto)
compara = tam-1 
diferentes = 0
for cont in range(0, (tam//2)):
    if(junto[cont] != junto[compara]):
        diferentes += 1
    compara -=1 
if diferentes != 0:
    print('\033[31mNÃO\033[m é palíndromo')
else:
    print('É \033[34mPALÍNDROMO\033[m')

print('Pois a frase que você digitou é {} e ao contrário é '.format(junto), end='')
for cont in range (tam-1, -1, -1):
    print(junto[cont], end='')