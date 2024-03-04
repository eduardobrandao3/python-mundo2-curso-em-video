'''DESAFIO 57
Leia o sexo de uma pessoa mas só aceite M ou F. Caso esteja errado peça a digitação novamente ate ter um valor certo'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos')
print('Sexo {} registrado com sucesso'.format(sexo))