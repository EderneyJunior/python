n = (int(input('Digite um valor: ')),
int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))
print(f'Você digitou os numeros {n}')
print(f'O numero nove apareceu {n.count(9)} vezes')
'''while True:
    for t in range(0,4):
        if n[t] == 3:
            print(f'O numero tres apareceu a primeira vez na posição {n.index(3) + 1}')
        if n[t] == 3:
            break
    break'''
if 3 in n:
    print(f'O numero três apareceu a primeira vez na posição {n.index(3) + 1}')
else:
    print('O numero três não foi digitado')
print(f'Os numeros pares foram: ', end='')
for c in range(0,4):
    if n[c] % 2 == 0:
        print(f'{n[c]} ', end=' ')
