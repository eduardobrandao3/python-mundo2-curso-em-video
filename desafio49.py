'''DESAFIO 49
Refaça o desafio 009 mostrando a tabuada de um número q o usuário escolher, mas gora com o laço for '''

num = int(input('Digite o número que você quer a tabuada: '))

print('{:-^17}'.format('TABUADA'))
for cont in range(1, 11):
    print('{} X {:2} = {}'.format(num, cont, (num*cont)))
print('-'*17)