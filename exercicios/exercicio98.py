from time import sleep
def contador(I, F, P):
    if P < 0:
        P *= -1
    elif P == 0:
        P = 1
    print('-='*20)
    if I < F:
        print(f'Contagem de {I} até {F} de {P} em {P}')
        for c in range(I, F+1, P):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print()
    else:
        print(f'Contagem de {I} até {F} de {P} em {P}')
        for c in range(I, F-1, -P):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é dua vesz de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:'))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
