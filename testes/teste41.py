import datetime

ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano

if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é mirim')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é infantil')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é júnior')
elif idade > 19 and idade <= 25:
    print(f'Você tem {idade} anos e sua categoria é sênior')
else:
    print(f'Voce tem {idade} anos e sua categoria é master')
