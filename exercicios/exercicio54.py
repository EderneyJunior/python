import datetime

ano = datetime.date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    idade = int(input(f'Digite o {c} ano de nascimento: '))
    pess = ano - idade
    if pess > 18:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores')
