'''DESAFIO 56
Leia nome, idade e sexo de 4 pessoas. No final mostre:
media de idade; nome do homem mais velho e quantas mulheres tem menos de 20 anos'''

nomeHvelho = 'Não foi informado o nome de nenhum homem'
idadeHvelho = 0
somaId = 0
mulheresMenores = 0
for cont in range(1, 5):
    print('{}{}ª PESSOA{}'.format(('-')*15, cont, ('-')*15))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    somaId += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        if idade > idadeHvelho:
            idadeHvelho = idade
            nomeHvelho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheresMenores += 1
    else: 
        print('Opção Inválida')
print('''A média das idades informadas é: {:.2f}
O nome do homem mais velho é {} com {} anos
A quantidade de mulheres menores de 20 anos é: {}'''.format((somaId/4), nomeHvelho, idadeHvelho, mulheresMenores))