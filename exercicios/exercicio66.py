n = cont = soma = 0
while True:
    n = int(input('Digite um numero. [999] Para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foi mostrado {cont} numeros e a soma entre eles é de {soma}')
