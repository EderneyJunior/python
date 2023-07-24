from moedas108 import *

n = float(input('Digite o preço: R$'))
print('-='*20)
print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
print(f'A metade de {moeda(n)} é {moeda(metade(n))}')
print(f'Com aumento de 10%, fica {moeda(aumento(n))}')
