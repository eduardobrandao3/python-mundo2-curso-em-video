'''DESAFIO 63
Ler um numero inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci
ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

num = int(input('Quantos termos você quer mostrar? '))
p = 0
seg = 1
mostrou = 0
if num <= 0:
    print('Quantidade de termos inválidas!')
elif num == 1:
    print(p)
elif num == 2:
    print(p, end='  ')
    print(seg, end='  ')
else: 
    print(p, end='  ')
    print(seg, end='  ')
    mostrou = 2
    while mostrou != num:
        fib = p + seg
        print(fib, end='  ')
        p = seg
        seg = fib
        mostrou += 1


