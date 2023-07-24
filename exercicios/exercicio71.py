print('='*40)
print('{:^40}'.format('BANCO PEDROSO'))
print('='*40)
valor = int(input('Digite o valor que deseja sacer: R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print(f'VOLTE SEMPRE AO BANCO PREDOSO, TENHA UM BOM DIA!')