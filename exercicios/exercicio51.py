print(f'=====================')
print(f'10 TERMOS DE UMA PA')
print(f'=====================')
novo = 'S'
while novo == 'S':
    ter = int(input('Primeiro termo: '))
    raz = int(input('Razão: '))
    soma = ter
    cont = 0
    while cont < 10:
            print(f'{soma}', end='')
            print(f' > ' if cont < 9 else ' > FIM!', end='')
            soma += raz
            cont += 1 
    novo = str(input('\n[S] Para continuar\n[N] Para não continuar\nDigite sua resposta: ')).strip().upper()
    if novo != 'S' or novo != 'N':
        while novo not in 'SN':
            novo = str(input('Resposta invalida. Digite novamente: ')).strip().upper()

'''for c in range(ter, (ter + (10-1) * raz) + raz, raz):
    print(f'{c}')'''
print(f'Volte sempre!')
