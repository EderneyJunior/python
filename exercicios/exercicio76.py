lista = ('Lapis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'estojo', 25.00,
         'Trasferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.50,
         'Canetas', 15.00,
         'Livro', 35.90)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇO'))
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:.2f}')
print('-'*40)
