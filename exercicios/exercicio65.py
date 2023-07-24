'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

n = media = cont = maior = menor = 0
c = 'S'
while c in 'Ss':
    if cont == 0:
        n = int(input('Digite um numero: '))
    else:
        n = int(input('Digite outro numero: '))
    cont += 1
    media += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print('=-'*20)
    c = str(input('[ S ] Para continuar\n[ N ] Para finalizar o programa\nSua resposta:')).strip()
    while c not in 'SsNn':
        print('=-'*20)
        c = str(input('Resposta invalida, Digite: \n[ S ] Para continuar\n[ N ] Para finalizar o programa\nSua resposta:'))
    print('=-'*20)
media = media / cont
print(f'Media: {media:.2f}\nMaior: {maior}\nMenor {menor}')
