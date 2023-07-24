from time import sleep

operacao = 0
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
while operacao != 5:
    operacao = int(input('''    [ 1 ] Soma\n    [ 2 ] Multiplicação
    [ 3 ] Divisão\n    [ 4 ] Novos numeros\n    [ 5 ] Sair do programa\nDigite a operação que deseja fazer: '''))
    if operacao == 1:
        print(f'O resultado da soma entre {num1} e {num2} foi {num1 + num2}') 
    elif operacao == 2:
        print(f'O resultado da multiplicação entre {num1} e {num2} foi {num1 * num2}')
    elif operacao == 3:
        if num2 != 0:
            print(f'O resultado da divisão entre {num1} e {num2} foi {num1 / num2} ')
        else:
            print(f'Não foi possivel fazer a divisão!')
    elif operacao == 4:
        num1 = float(input('Digite um numero: '))
        num2 = float(input('Digite outro numero: '))
    elif operacao < 1 or operacao > 5:
        print(f'Opção inválida. Tente novamente')
    elif operacao == 5:
        print('FINALIZANDO...')
        sleep(2)
print('FIM DO PROGRAMA!')
