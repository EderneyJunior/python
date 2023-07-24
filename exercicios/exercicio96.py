def area(a, b):
    res = a * b
    print(f'A area de um terreno {a}X{b} é {res}m2')


print(f'{"Area de um terreno"}')
print('-'*20)
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
