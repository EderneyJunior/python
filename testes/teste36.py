import time
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salario: R$'))
tempo = int(input('Digite em quantos anos ira pagar: '))
prestacao = casa / (tempo * 12)
print(f'Para pagar o valor de {casa:.2f} da casa a prestacao sera de R${prestacao:.2f} em {tempo} anos')
print(f'Avaliando...')
time.sleep(2)
if prestacao  > salario * 0.3:
    print(f'O emprestimo foi negado!')
else: 
    print(f'O seu emprestimo foi aceito!')
