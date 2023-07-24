
frase = str(input('Digite uma palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
# inverso = junto[::-1]
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

print(f'{junto} no inverso é {inverso}')

if inverso == junto:
    print(f'A palavra digitada é um palindromo!')
else:
    print(f'A palavra digitada não é um palindromo!')
