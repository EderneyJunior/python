def dobro(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res


def aumento(num):
    res = 0.1 * num + num
    return res

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
