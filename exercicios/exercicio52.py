num  = int(input('Digite um numero para saber se ele é primo: '))
cont = 0

for c in range(0, num + 1):
    if num % c == 0:
        print(f'\033[32m', end='')
        cont += 1
    else:
        print(f'\033[31m', end='')

    print(f'{c}', end='')
    
print(f'O numero {num} foi divisivel {cont} vezes')
