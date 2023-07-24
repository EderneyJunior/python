from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip()
idade = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - idade
pessoa['ctps'] = int(input('Carteira de trabalho. (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = int(input('Salário: R$ '))
    pessoa['Aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - date.today().year)
print('-='*40)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
