def jogador(nome = '<desconhecido>', gols = 0):
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


j = str(input('Nome do jogador: ')).strip()
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j == '':
    jogador(gols = g)
else:
    jogador(j, g)
