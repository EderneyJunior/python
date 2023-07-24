''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, Digite seu sexo novamente: ')).upper().strip()
if sexo == 'M':
    print(f'Sexo masculino registrado!')
else:
    print(f'Sexo feminino registrado!')
