'''DESAFIO 39
leia o ano de nascimento de um jovem e informe de acordo com sua idade:
-se ele ainda vai se alistar ao serviço militar
-se é a hora de se alistar
-se já passou do tempo do alistamento
também precisa mostrar o tempo q falta ou q passou do prazo'''

from datetime import date

anoNasc = int(input('Digite o ano que você nasceu: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if idade == 18:
    print('É a hora de se alistar, pois em {} sua idade é 18 anos'.format(anoAtual))
elif idade < 18:
    print('Você ainda terá que se alistar, falta(m) {} ano(s) para se alistar'.format(18 - idade))
    print('Sua idade é {} anos em {}'.format(idade, anoAtual))
    print('Você terá que se alistar em {}'.format(anoAtual + (18 - idade)))
else:
    print('Já passou do tempo de se alistar. Passou-se {} ano(s)'.format(idade - 18))
    print('Sua idade é {} anos em {}'.format(idade, anoAtual))
    print('Você deveria ter se alistado em {}'.format(anoAtual - (idade - 18)))
