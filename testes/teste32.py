import time
import datetime

ano = int(input('Digite o ano que quer analisar, coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
bisexto = ano % 4

print(f'ANALIZANDO...')
time.sleep(3)

if bisexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bisexto!')
else:
    print(f'O ano {ano} não é bisexto!') 