pilha = list()
expressão = str(input('Digite a expressão: ')).strip()
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('-='*30)
if len(pilha) == 0:
    print('Sua resposta é valida!')
else:
    print('Sua resposta está errada!')
