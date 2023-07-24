matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
maior = somapar = somater =  0 
for l in range(0,3):
    for c in range(0, 3):
        matriz[c][l] = int(input(f'Digite o valor para a posião [{c}, {l}]: '))
        if c == 2:
            somater += matriz[c][l]
        if matriz[c][l] % 2 == 0:
            somapar += matriz[c][l]
print('-='*30)
print('Os valores digitados foram: ')
for l in range(0,3):
    for c in range(0, 3):
        print(f'{matriz[c][l]:^5}', end='')
    print()
print('-='*40)
print(f'A soma dos pares ficou {somapar}')
print(f'A soma dos valores da terceira coluna ficou {somater}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[c][1]
    else:
        if matriz[c][1] > maior:
            maior = matriz[c][1]
print(f'E o maior valor da linha 2 foi {maior}')
