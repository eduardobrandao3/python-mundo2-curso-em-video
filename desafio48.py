'''DESAFIO 48
calcule a soma entre todos os números ímpares que são múltiplos de 3 que se encontram no intervalo de 1 até 500 '''

soma = 0
qnt = 0
for cont in range(1, 501, 2):
    if ((cont % 3) == 0):
        soma += cont
        qnt +=1 
print('A soma entre os {} ímpares e que são múltiplos de 3 no intervalo entre 1 e 500 é: {}'.format(qnt, soma))