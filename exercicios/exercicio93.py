jogador = dict()
gols = list()
tot = 0
jogador['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, n):
    gols.append(int(input(f'Quantos gols ele fez na partida {c+1}: ')))
    tot += gols[c]
jogador['gols'] = gols.copy()
jogador['total'] = tot
print('-='*40)
print(jogador)
print('-='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for i, c in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {c} gols')
print(f'Com o total de {jogador["total"]} gols.')
