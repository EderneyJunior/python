lista = list()
saida = ''
while True:
    lista.append(int(input('Digite um numero: ')))
    saida = str(input('Quer continuar ? [S/N]')).strip()[0]
    while saida not in 'SsNn':
        saida = str(input('Resposta Inválida! Quer continuar ? [S/N] ')).strip()[0]
    if saida in 'Nn':
        break
    print('-'*40)
print('-'*40)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} numeros.')
print(f'A lista em forma decrescente fica {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não esta na lista!')
