salario = float(input('Digite o seu salario: '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print(f'O aumento do seu salario foi de {aumento} e seu novo salario é de R$: {salario + aumento:.2f} ')
