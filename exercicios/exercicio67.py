n = cont = 0
while True:
    cont = 1
    n = int(input('Digite um numero para saber sua tabuada: '))
    print('=-'*20)
    if n < 0:
        print(f'Você digitou um numero negativo. FIM DO PROGRAMA!')
        break
    while cont <= 10:
        mult = n * cont
        print(f'{n} X {cont} = {mult}')
        cont += 1
