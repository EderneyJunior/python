valores = list()
saida = ''
while True:
    cont = int(input('Digite um valor: '))
    if cont in valores:
        print('VALOR DUPLICADO! Não vou adicionar.')
    else:
        valores.append(cont)
        print('VALOR ADICIONADO COM SUCESSO!')
    saida = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Opção invalida. Quer continuar [S/N]? ')).strip().upper()[0]
    if saida == 'N':
        break
print('-='*40)
print(f'Você adicionou os valores {sorted(valores)}')
