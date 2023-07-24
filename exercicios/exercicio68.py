'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
n = s =  cont = 0
numpc = 0
print('-'*20)
print('JOGO DE PAR OU IMPAR')
print('-'*20)
while True:
    esc = ' '
    numpc = randint(0, 10)
    print('-'*20)
    n = int(input('Digite um Valor: '))
    while esc not in 'PI':
        esc = str(input('[ P ] PAR\n[ I ] IMPAR\nSua escolha? ')).strip().upper()
    print('-'*20)
    s = n + numpc
    print(f'Voce escolheu {n} e o pc escolheu {numpc} total de {s}, ', end='')
    print('Deu par!' if s % 2 == 0 else 'Deu impar!')
    if s % 2 == 0 and esc == 'P':
        print('\033[32mVocê ganhou!\033[m')
        cont += 1
    if s % 2 == 1 and esc == 'I':
        print('\033[32mVocê ganhou!\033[m')
        cont += 1
    if s % 2 == 0 and esc == 'I':
        print('\033[31mGAME OVER!\033[m', end='')
        break
    if s % 2 == 1 and esc == 'P':
        print('\033[31mGAME OVER!\033[m', end='')
        break
print(f' Você ganhou {cont} vezes')
