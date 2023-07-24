jogador = dict()
gols = list()
galera = list()
tot = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n):
        gols.append(int(input(f'Quantos gols ele fez na partida {c+1}: ')))
        tot += gols[c]
    jogador['gols'] = gols.copy()
    jogador['total'] = tot
    galera.append(jogador.copy())
    jogador.clear()
    gols.clear()
    saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if saida in 'N':
        break
print('-='*30)
print(f'{"cod":<4}{"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-'*40)
for k,v in enumerate(galera):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Quer saber os dados de qual jogador? (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(galera):
        print('ERRO! Esse jogador não existe')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {galera[busca]["nome"]}: ')
        for i, g in enumerate(galera[busca]['gols']):
            print(f'No jogo {i+1}, fez {g} gols')
        print('-'*40)
print('<<<  FINALIZADO >>>')