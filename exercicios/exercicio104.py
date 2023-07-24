def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31mERRO! Digite um numero inteiro válido: \033[m')
        print('-'*40)
        if ok:
            break
    return valor

n = leiaint('Digite um valor n: ')
print(f'Voce acabou de digitar o numero {n}')
