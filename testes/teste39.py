import datetime

nas = int(input('Digite seu ano de nascimento: '))
ano = datetime.date.today().year - nas

if ano == 18:
    print(f'Esta na hora de se alistar!')
elif ano > 18:
    print(f'Já passou {ano - 18} anos do aliamento, Vamos se alistar!')
elif ano == 17:
    print(f'falta {18-ano} ano para se alistar.')
else:
    print(f'Ainda falta {18-ano} anos para se alistar.')