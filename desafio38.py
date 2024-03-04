'''DESAFIO 38
Ler 2 inteiros e compare-os mostrando na tela uma mensagem
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a > b:
    print('O \033[34mprimeiro\033[m valor é \033[34mmaior\033[m')
elif a < b:
    print('O \033[34msegundo\033[m valor é \033[34mmaior\033[m')
else: 
    print('Não existe valor maior, os dois são \033[34miguais')
