def escreva(esc):
    tam = len(esc) + 4
    print('-'*tam)
    print(f'  {esc}')
    print('-'*tam)


palavra = str(input('Digite uma frase: ')).strip()
escreva(palavra)
