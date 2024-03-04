'''DESAFIO 71
simular funcionamento de caixa eletrônico. Pergunte qual valor será sacado(inteiro) 
e o programa vai informar quantas cédulas de cada valor. Considere que o caixa tem cédulas de 50, 20, 10 e 1'''

while True:
    c50 = c20 = c10 = c1 = 0
    valor = int(input('Informe o valor que deseja sacar: R$'))
    c50 = valor // 50
    c20 = (valor % 50) // 20
    c10 = ((valor % 50) % 20) // 10
    c1 = ((valor % 50) % 20) % 10
    print(f'''Você sacará R${valor} da seguinte maneira:
{c50} notas de R$50 = R${c50 * 50:.2f}
{c20} notas de R$20 = R${c20 * 20:.2f}
{c10} notas de R$10 = R${c10 * 10:.2f}
{c1} notas de R$1 = R${c1 * 1:.2f}''')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção Inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('VOLTE SEMPRE!!')