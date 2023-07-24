from random import randint
from time import sleep
jogos = list()
sor = list()
print('-'*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-'*30)
n = int(input('Quantos jogos que que eu jogue? '))
num = 0
for c in range(0, n):
    while len(sor) < 6:
        num = randint(1,60)
        if num not in sor:
            sor.append(num)
    jogos.append(sor[:])
    sor.clear()
print('{:=^40}'.format(f' SORTEANDO {n} JOGOS '))
for c, j in enumerate(jogos):
    print(f'Jogo {c+1}: {sorted(j)}')
    sleep(1)
print('{:=^40}'.format(' <  BOA SORTE! > '))
