num = int(input('Digite um numero: '))
converter = int(input('''[1] Para converter em binario
[2] Para converter em octal\n[3] Para convertar em hexadicimal\nSua opção: '''))

if converter == 1:
    print(f'O numero {num} convertido para binario é {bin(num)[2:]}')
elif converter == 2:
    print(f'O numero {num} convertido para octal é {oct(num)[2:]}')
elif converter == 3:
    print(f'O numero {num} convertido em hexadecimal é {hex(num)[2:]}')
else:
    print(f'Opção invalida, tente novamente!')