'''DESAFIO 43
Ler o peso e a altura de uma pessoa. Calcule IMC e mostre seu status, de acordo com a tabela abaixo:
-abaixo de 18.5: abaixo do peso
-entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-acima de 40: obesidade mórbida'''

peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em m: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está \033[31mABAIXO DO PESO\033[m'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}, você está com \033[32mPESO IDEAL\033[m'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}, você está com \033[31mSOBREPESO\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}, você está com \033[31mOBESIDADE\033[m'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com \033[1;31mOBESIDADE MÓRBIDA\033[m'.format(imc))