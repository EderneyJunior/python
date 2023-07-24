idade = mais18 = homem = mulher = 0

while True:
    sexo = ' '
    cont = ' '
    idade = int(input('Digite a idade da pessoa: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M\F]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    while cont not in 'SN':
        cont = str(input(f'[ S ] Para continuar\n[ N ] Para terminar\nSua escolha: ')).strip().upper()[0]
    if cont in 'N':
        break
if mais18 == 1:
    print(f'{mais18} pessoa tem mais de 18 anos')
else: 
    print(f'{mais18} pessoas tem mais de 18 anos')
if homem == 1:
    print(f'{homem} homem foi cadatrado')
else:
    print(f'{homem} homens foram cadastrados')
if mulher == 1:
    print(f'{mulher} mulher tem menos de 20 anos')
else: 
    print(f'{mulher} mulheres tem menos de 20 anos.')
