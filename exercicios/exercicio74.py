from random import randint
n = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os numeros gerados foram: {n}')
maior = menor = n[0]
'''for c in range(0,5):
    if n[c] > maior:
        maior = n[c]
    if n[c] < menor:
        menor = n[c]
print(f'O maior numero foi {maior} e o menor numero foi {menor}')'''
print(f'O maior valor foi {max(n)}')
print(f'O menor valor for {min(n)}')
