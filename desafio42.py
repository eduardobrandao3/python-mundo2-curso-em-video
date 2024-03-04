'''DESAFIO 42
Refaça o desafio 35 dos triâgulos, acrescentando o recurso de mostrar q tipo de triângulo será formado
-EQUILÁTERO: todos os lados iguais
-ISÓSCELES: 2 lados iguais
-ESCALENO: todos os lados diferentes'''

r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Os segmentos {}, {} e {} \033[32mPODEM\033[m formar um triângulo'.format(r1, r2, r3))
    if (r1 == r2) and (r1 == r3):
        print('Todos os lados são iguais, portanto triângulo \033[32mEQUILÁTERO\033[m')
    elif ((r1 == r2) and (r1 != r3)) or ((r1 == r3) and (r1 != r2)) or ((r2 == r3) and (r2 != r1)):
        print('Dois lados iguais, portanto triângulo \033[32mISÓSCELES\033[m')
    else:
        print('Todos os lados são diferentes, portando triângulo \033[32mESCALENO\033[m')
else: 
    print('Os segmentos {}, {} e {} \033[31mNÃO\033[m podem formar um trângulo'.format(r1, r2, r3))