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



def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados.')
            return 0
        except:
            print(f'\033[31mERRO! Digite um numero real válido.\033[m')
        else:
            return n


n = leiaint('Digite um inteiro: ')
f = leiafloat('Digite um numero real: ')
print(f'O numero inteiro digitado foi {n} e o real foi {f:.1f}')
