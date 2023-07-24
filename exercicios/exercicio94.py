pessoa = dict()
galera = list()
media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('ERRO! Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    media += pessoa['idade']
    pessoa.clear()
    saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while saida not in 'SsNn':
        saida = str(input('RESPOSTA INVÁLIDA! Quer continuar? [S/N]: ')).strip().upper()[0]
    if saida in 'Nn':
        break
print('=-'*40)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
media = media/(len(galera))
print(f'B) A média de idade é {media:.1f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='. ')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(f'Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')
