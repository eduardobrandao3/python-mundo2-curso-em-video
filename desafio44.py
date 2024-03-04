'''DESAFIO 44
Calcular valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto
-à vista cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros'''

preco = float(input('Digite o preço do produto: R$'))
print('-=-'*15)
print('OPÇÕES DE PAGAMENTO')
print('1 - À vista no dinheiro ou cheque')
print('2 - À vista no cartão')
print('3 - Em até 2x no cartão')
print('4 - 3x ou mais no cartão')
opcao = int(input('Digite o número relacionado a opção: '))
print('-=-'*15)

if opcao == 1:
    print('Você ganhou 10% de desconto! O produto custava R${:.2f} agora custará \033[32mR${:.2f}\033[m'.format(preco, (0.9*preco)))
elif opcao == 2:
    print('Você ganhou 5% de desconto! O produto custava R${:.2f} agora custará \033[32mR${:.2f}\033[m'.format(preco, (preco*0.95)))
elif opcao == 3: 
    print('Nessa condição o produto continua o mesmo preço \033[32mR${:.2f}\033[m'.format(preco))
    print('O valor de cada parcela será R${:.2f}'.format(preco/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Nessa condição o produto terá 20% de juros. Antes custava R${:.2f} e sairá por \033[31mR${:.2f}\033[m'.format(preco, (preco*1.2)))
    print('O valor de cada parcela será R${:.2f}'.format((1.2*preco)/parcelas))
else:
    print('\033[31mOpção Inválida!\033[m')