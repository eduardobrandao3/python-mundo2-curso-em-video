'''DESAFIO 36
aprovar empréstimo bancário para compra de uma casa. Pergunta valor da casa, salário e em quantos anos vai pagar.
Calcule valor da prestação mensal sabendo q ela não pode exceder 30% do salário ou então o empréstimo será negado. 
Não vai considerar juros'''
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Digite em quantos anos quer pagar: '))
prestacao = valor / (anos*12)
valorMax = 0.3*salario
if prestacao > valorMax:
    print('O empréstimo foi \033[31mnegado\033[m, pois a prestação está no valor de R${:.2f}, mas poderia ser no máximo R${:.2f}'.format(prestacao, valorMax))
else: 
    print('O empréstimo foi \033[32maprovado\033[m. Valor da prestação: R${:.2f}'.format(prestacao))