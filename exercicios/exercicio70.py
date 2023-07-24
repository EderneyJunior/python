preco = maior = custo = total = 0
maisbarato = ''
cont = 1
print('='*30)
print('        LOJAS PEDROSO')
print('='*30)
while True:
    nome = ' '
    res = ' '
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    print('-'*30)
    total += preco
    if preco >= 1000:
        maior += 1
    if cont == 1:
        maisbarato = nome
        custo = preco
        cont += 1
    else:
        if custo > preco:
            maisbarato = nome
            custo = preco
    while res not in 'SN':
        res = str(input('[ S ] Para continuar\n[ N ] Para terminar a execusão\nSua resposta: ')).strip().upper()[0]
    print('-'*30)
    if res in 'N':
        break
print(f'O total da compra foi de R$ {total:.2f}')
print(f'{maior} produtos ultrapassaram R$ 1000.00')
print(f'{maisbarato} custou R$ {custo:.2f} e foi o produto mais barato')
    