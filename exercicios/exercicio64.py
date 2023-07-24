'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = int(input('Digite um numero: '))
soma = n
cont = 0
while n != 999:
    n = int(input('[Digite 999 para terminar] ou Digite outro numero: '))
    cont += 1
    if n == 999:
        print(f'Foram digitados {cont} numeros e a soma entre eles foi de {soma}.')
    else:
        soma += n
print('FIM!')
