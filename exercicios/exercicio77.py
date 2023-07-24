palavras = ('Palavra', 'Programar', 'Programador', 'Estudar', 'Python', 'Curso',
             'Gratis', 'Futuro', 'Mercado',  'Trabalho', 'Praticar')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
