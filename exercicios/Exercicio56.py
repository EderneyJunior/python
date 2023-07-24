'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

nomevelho = ''
idadehomem = 0
jovem = 0
media = 0

for c in range(1,5):
    print(f'----- {c} PESSOA -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (M/F): ')).strip()
    media += idade
    if c == 1 and sexo in 'Mm':
            idadehomem = idade
            nomevelho = nome
    if sexo in 'Mm' and idadehomem < idade:
                idadehomem = idade
                nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        jovem += 1 
media = media / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O nome do homem mais velho é {nomevelho} e sua idade é {idadehomem} anos')
if jovem == 1:
    print(f'{jovem} mulherer tem menos de 20 anos')
elif jovem == 0:
    print(f'Nenhuma mulher tem menos de 20 anos')
else:
    print(f'{jovem} mulheres tem menos de 20 anos')
    