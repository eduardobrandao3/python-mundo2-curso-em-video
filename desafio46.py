'''DESAFIO 46
Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, de 10 até 1. 
com pausa de 1 seg entre eles'''
from time import sleep
print('INICIO CONTAGEM PARA OS FOGOS:')
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('🎆✨')