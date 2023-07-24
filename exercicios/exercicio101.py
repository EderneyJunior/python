def voto(num):
    from datetime import date
    idade = date.today().year - num
    if idade >= 18 and idade < 65:
        return print(f'Com {idade} anos: VOTO É OBRIGATÓRIO!')
    elif idade >= 65 or idade >= 16 and idade < 18:
        return print(f'Com {idade} anos: O VOTO É OPCIONAL!')
    else:
        return print(f'Com {idade} anos: O VOTO É PROIBIDO!')


ano = int(input('Digite seu ano de nascimento: '))
voto(ano)
