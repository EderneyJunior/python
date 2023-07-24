print(f'=====================')
print(f'TERMOS DE UMA PA')
print(f'=====================')
ter = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
soma = ter
cont = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont < total:
        print(f'{soma}', end='')
        print(f' > ' if cont < total - 1 else ' > PAUSA!', end='')
        soma += raz
        cont += 1 
    mais = int(input('\nQuantos termos a mais quer mostar: '))
print(f'O processo terminou e foi mostrado {total} termos!')
