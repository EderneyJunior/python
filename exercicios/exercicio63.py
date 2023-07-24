print('-'*30)
print('Sequência de fibonacci')
print('-'*30)
n = int(input('Digite quantos termos deseja mostar: '))
f1 = 0
f2 = 1
f3 = 0
cont = 3
print(f'{f1}', end=' > ')
print(f'{f2}', end=' > ')
while cont <= n:
    f3 = f1 + f2
    print(f'{f3}', end=' > ')
    f1 = f2
    f2 = f3
    cont += 1
print(f'FIM!')