r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        print(f'Estes seguimentos formam um triângulo equilátero.')
    elif r1 == r2 != r3 or r3 == r1 != r2 or r3 == r2 != r1:
        print(f'Estes seguimentos formam um triângulo isóceles.')
    elif r1 != r2 != r3 != r1:
        print(f'Estes seguimenos formam um triângulo escaleno.')
else:
    print(f'Estes seguimentos não formam um triângulo.')
