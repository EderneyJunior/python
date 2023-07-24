def dobro(num, format=False):
    res = num * 2
    return res if format is False else moeda(res)


def metade(num, format=False):
    res = num / 2
    return res if format is False else moeda(res)


def aumento(num, format=False):
    res = 0.1 * num + num
    return res if format is False else moeda(res)

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
