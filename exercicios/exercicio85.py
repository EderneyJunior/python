junto = [[], []]
saida = ''
while True:
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        junto[0].append(n)
    else:
        junto[1].append(n)
    saida = str(input('Quer continuar? [S/N] ')).strip()[0]
    while saida not in 'SsNn':
        saida = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip()[0]
    if saida in 'Nn':
        break
print('-='*40)
print(f'Os valores pares digitados foram {junto[0]}')
print(f'Os valores impares digitados foram {junto[1]}')
