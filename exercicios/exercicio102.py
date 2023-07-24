def fatorial(num, show=False):
    """
    --> Calcula o factorial do número.
    :param num: Número a ser calculado.
    :param show: (Opcional) mostra a conta.
    :return: O retorco do factorial de um número num.
    """
    res = 1
    print('-='*15)
    for c in range(num, 0, -1):
        if c != 1:
            if show:
                print(c, end=' x ')
            res *= c
        else:
            print('1', end=' = ')
    return res


print(fatorial(5, show=True))
help(fatorial)
