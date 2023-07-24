valores = list()
par = list()
impar = list()
saida = ''
while True:
    n = int(input('Digite um numero: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    saida = str(input('Quer continuar ? [S/N]')).strip()[0]
    while saida not in 'SsNn':
        saida = str(input('Resposta Inválida! Quer continuar ? [S/N] ')).strip()[0]
    if saida in 'Nn':
        break
'''for i, v in enummerate(valores)
      if v % 2 == 0:
        par.append(v)
      else:
          impar.append(v)'''
print('-'*60)
print(f'Você digitou os valores {valores}')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')
