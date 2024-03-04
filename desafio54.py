'''DESAFIO 54
Leia o ano de nascimento de 7 pessoas. No final mostre quantas ainda não atingiram a maioridade e quantas já são maiores'''
 
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for cont in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(cont)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else: 
        menor += 1
print('''\nEntre as datas de nascimentos digitadas:
{} pessoas já atingiram a maioridade
{} pessoas não atingiram a maioridade ainda'''.format(maior, menor))