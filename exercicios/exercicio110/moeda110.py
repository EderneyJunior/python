def dobro(num, format=False):
    res = num * 2
    return res if format is False else moeda(res)


def metade(num, format=False):
    res = num / 2
    return res if format is False else moeda(res)


def aumento(num, aum, format=False):
    res = (aum / 100) * num + num
    return res if format is False else moeda(res)


def redução(num, red, format=False):
    res = num - (red / 100) * num
    return res if format is False else moeda(res)

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(preco = 0, aumen =  10, redu = 5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analizado: {moeda(preco)}')
    print(f'Dobro do preço: {dobro(preco, format=True)}')
    print(f'Metade do preço: {metade(preco, format=True)}')
    print(f'{aumen}% de aumento: {aumento(preco, aumen, format=True)}')
    print(f'{redu}% de redução: {redução(preco, redu, format=True)}')
    print('-'*30)
