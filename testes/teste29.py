carro = float(input('Digite a velocidade do carro: '))

if carro > 80:
    print(f'Você excedeu o limite de {carro} km/h e sera multado em R$ {(carro - 80) * 7:.2f} Reais')
else:
    print(f'Bom dia, dirija com cuidado!')
