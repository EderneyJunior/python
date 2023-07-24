viajem = int(input('Digite a distancia da viagem em km: '))

if viajem <= 200:
    print(f'O valor da viajem de {viajem} km é de R$: {viajem * 0.5:.2f}')
else:
    print(f'O valor da viajem de {viajem} km é de R$: {viajem * 0.45:.2f}')
