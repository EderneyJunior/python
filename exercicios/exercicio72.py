n = 'Zero', 'Um', 'Dois', 'Tres'< 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte'
c = int(input('Digite um numero entre 0 e 20: '))
while True:
    if c < 0 or c > 20:
        c = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    else:
        break
print(f'Voce digitou o numero {n[c - 1]}!')
