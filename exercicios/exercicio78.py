valor = list()
for cont in range(0,5):
    valor.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Você digitou os valores {valor}')
maior = max(valor)
menor = min(valor)
print(f'O maior valor foi {maior} e foi encontrado na posição ', end='')
for c in range(0,5):
    if valor[c] == maior:
        print(f'{c}', end='...')
print(f'\nO menor valor foi {menor} e foi encontrado na posição ', end='')
for c in range(0,5):
    if valor[c] == menor:
        print(f'{c}', end='...')
