'''DESAFIO 69
Faça um programa q leia a idade e o sexo de várias pessoas a cada pessoa cadastrada o programa deve perguntar se quer continuar ou não
No final mostre:
A) qnts tem mais de 18
B) qnts homens foram cadastrados
C) qnts mulheres tem menos de 20'''

maior = 0
homens = 0
mulheresMenores = 0
total = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    total += 1
    while sexo not in 'MF':
        sexo = str(input('Opção inválida! Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    else: 
        if idade < 20:
            mulheresMenores += 1
    resp = str(input('Quer cadastrar mais? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção Inválida! Quer cadastrar mais? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''Das {total} pessoas cadastradas
{maior} são maiores de 18 anos
{homens} são homens
{mulheresMenores} são mulheres com menos de 20 anos''')
    