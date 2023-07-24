def leiaDinheiro(msg):
    valido = False
    while not valido:
        res = str(input(msg)).replace(',', '.')
        if res.isalpha() or res.strip() == '':
            print(f'\033[31mERRO! {res} é um preço inválido.\033[m')
        else:
            res = float(res)
            valido = True
            return res
