# escreva um codigo que faça o computador escolher um numero entre 0 e 5, faça o usuario descobiri o numero 
from random import randint
from time import sleep

cont = 1

computador = randint(0,10)
usuario = int(input(f'Pense em um numero entre 0 e 10: '))
print(f'ANALIZANDO...')
sleep(2)
while usuario != computador:
    if usuario > computador:
        usuario = int(input('\033[31mVocê errou!\033[m.O numero do PC é menor, Tente novamente: '))
    else:
        usuario = int(input(f'\033[31mVovê errou!\033[m. O numero do PC é maior, Tente novamente: '))
    print(f'ANALISANDO...')
    sleep(2)
    cont += 1
print(f'\033[32mVocê acertou!\033[m\nE precisou de {cont} tentativas')
