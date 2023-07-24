matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[c][l] = int(input(f'Digite o valor para a posião [{c}, {l}]: '))
print('-='*30)
print('Os valores digitados foram: ')
for l in range(0,3):
    for c in range(0, 3):
        print(f'{matriz[c][l]:^5}', end='')
    print()
