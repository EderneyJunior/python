from random import randint
from time import sleep
from operator import itemgetter
jogadas = {
            'jogador1' : randint(1,6),  
            'jogador2' : randint(1,6), 
            'jogador3' : randint(1,6), 
            'jogador4' : randint(1,6),  
}
ranking = list()
print('Sorteando...')
for k, v in jogadas.items():
    print(f'{k} jogou {v}')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('=====  RANKING  =====')
for k, v in enumerate(ranking):
    print(f'{k+1}° {v[0]} que jogou {v[1]}')
    sleep(1)
