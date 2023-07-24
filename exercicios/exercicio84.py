dados = list()
galera = list()
saida = ''
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    saida = str(input('Quer continuar? [S/N]')).strip()[0]
    while saida not in 'SsNn':
        saida = str(input('Resposta inválida! Quer continuar? [S/N]')).strip()[0]
    if saida in 'Nn':
        break
print('-='*40)
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for c in galera:
    if c[1] == mai:
        print(f'{c[0]}', end='. ')
print(f'\nO menor peso foi {men}Kg. Peso de ', end='')
for c in galera:
    if c[1] == men:
        print(f'{c[0]}', end='. ')
