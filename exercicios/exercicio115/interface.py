def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados.')
            return 0
        except:
            print(f'\033[31mERRO! Digite um numero inteiro válido.\033[m')
        else:
            return n


def cabeçalho(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)


def menu(*msg):
    opc = 0
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in msg:
        print(f'\033[33m{c} - \033[m\033[34m{item}\033[m')
        c += 1
    print('-'*40)
    opc = leiaint('\033[33mSua opção: \033[m')
    return opc
