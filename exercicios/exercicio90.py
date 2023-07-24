pessoa = {}
pessoa['nome'] = str(input('Nome: ')).strip()
pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['media'] >= 6:
    pessoa['situação'] = 'Aprovado'
else:
    pessoa['situação'] = 'Reprovado'
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')
    