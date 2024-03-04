'''DESAFIO 40
leia duas notas de um aluno e calcule sua média. Mostre no final alguma mensagem
-Media abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média é {:.1f}, portanto você está \033[31mREPROVADO\033[m'.format(media))
elif (media >= 5.0) and (media < 7):
    print('Sua média é {:.1f}, portanto você está de \033[33mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Sua media é {:.1f}, portanto você está \033[32mAPROVADO\033[m'.format(media))
