from time import sleep
from random import randint


def sorteia(lista):
    print( 'Sorteando 5 valores para a lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[c]}', end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
def somapar(lista):
    res = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            res += lista[c]
    print(f'Somando os valores pares de {lista}, temos {res}')


num = list()
sorteia(num)
somapar(num)
