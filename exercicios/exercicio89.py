from time import sleep
aluno = list()
junto = list()
while True:
    aluno.append(str(input('Nome: ')).strip())
    aluno.append(int(input('Nota 1: ')))
    aluno.append(int(input('Nota 2: ')))
    junto.append(aluno[:])
    aluno.clear()
    saida = str(input('Quer continuar? [S/N] ')).strip()[0]
    while saida not in 'SsNn':
        saida = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip()[0]
    if saida in 'Nn':
        break
print('-='*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*40)
for i, c in enumerate(junto):
    print(f'{i:<4}{c[0]:<10}{(c[1] + c[2]) / 2:>8.1f}')
while True:
    print('-'*40)
    cont = int(input('Mostrar nota de qual aluno? (999 interrompe). '))
    if cont == 999:
        break
    else:
        print(f'As notas de {junto[cont][0]} são: {junto[cont][1:]}')
print('FINALIZANDO...')
sleep(1.5)
print('<<< VOLTE SEMPRE >>>')
