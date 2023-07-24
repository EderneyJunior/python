soma = 0
contador = 0
for c in range(1, 7):
    s = int(input(f'Digite o {c} numero: '))
    if s % 2 == 0:
        soma += s 
        contador += 1
print(f' A soma dos {contador} numeros  pares é igual a {soma}')
