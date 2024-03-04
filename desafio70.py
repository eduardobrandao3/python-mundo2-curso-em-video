'''DESAFIO 70
Leia o nome e preço de vários produtos. O programa deve perguntar se o usuário vai continuar
No final mostre:
A)Total gasto na compra
b) qnts custam mais de 1000
c) nome do produto mais barato'''

total = qnt = maisMil = 0
while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: R$'))
    if qnt == 0:
        menor = preco
        maisBarato = nome
    total += preco
    qnt += 1
    if preco < menor:
        menor = preco
        maisBarato = nome
    if preco > 1000:
        maisMil += 1
    resp = str(input('Quer cadastrar mais? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção Inválida! Quer cadastrar mais? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''Você informou {qnt} produtos
Gastou no total R${total:.2f}
{maisMil} produtos custam mais de R$1000.00
O produto mais barato foi {maisBarato} e custou R${menor:.2f}''')