num = int(input('Digite um numero para saber seu fatorial: '))
c = num
fat = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(f'{fat}')
