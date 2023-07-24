
print(f'==========LOJAS PEDROSO==========')
valor = float(input('Digite o valor do produto: R$'))
pg = int(input('[1] dinheiro/cheque\n[2] A vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nDigite aqui: '))

if pg == 4:
    vezes = int((input('Digite quantas parcelas: ')))
    jur = valor * 0.2
    print(f'Você ira pagar 20% de juros!')
    parcela = (valor + jur) / vezes
    print(f'O valor dos juros foi de R${jur:.2f} e o valor a pagar sera {vezes} percelas de R${parcela:.2f}, totalizando R${parcela * vezes:.2f}')


if pg == 1:
    print(f'Você teve um desconto de 10%')
    des = valor * 0.1
    print(f'O valor do desconto foi de R${des:.2f} e o valor a pagar sera de R${valor - des:.2f}')
elif pg == 2:
    print(f'Você teve um desconto de 5%')
    des = valor * 0.05
    print(f'O valor do desconto foi de R${des:.2f} e o valor a pagar sera de R${valor - des:.2f}')
elif pg == 3:
    print(f'Você não teve desconto!')
    parcela = valor / 2
    print(f'O valor a pagar sera 2 parcelas de R${parcela:.2f}, totalizando {valor:.2f}')
   