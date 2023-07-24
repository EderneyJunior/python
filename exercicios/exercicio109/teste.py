from moeda109 import *

n = float(input('Digite o preço: R$'))
print('-='*20)
print(f'O dobro de {moeda(n)} é {dobro(n, format=True)}')
print(f'A metade de {moeda(n)} é {metade(n, format=True)}')
print(f'Com aumento de 10%, fica {aumento(n, format=True)}')
