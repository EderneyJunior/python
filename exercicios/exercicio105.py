def notas(*num, sit=False):
    """"
    --> Função para analizar a nota e situação de varios alunos.
    :param num: Recebe uma ou mais notas dos alunos (aceita varias).
    :param sit: Valor opcional, Se deve ou não mostar a situação da turma.
    :return: Retorna um dicionario com as informações da turma.
    """
    resp = dict()
    soma = 0
    resp['total'] = len(num)
    for c in range(0, len(num)):
        if c == 0:
            resp['maior'] = num[c]
            resp['menor'] = num[c]
        else:
            if resp['maior'] < num[c]:
                resp['maior'] = num[c]
            if resp['menor'] > num[c]:
                resp['menor'] = num[c]
    for i in range(0, len(num)):
        soma += num[i]
    resp['média'] = soma/len(num)
    if sit:
        if resp['média'] >= 8:
            resp['situação'] = 'MUITO BOA'
        elif resp['média'] >= 6:
            resp['situação'] = 'BOA'
        elif resp['média'] >= 5:
            resp['situação'] = 'RAZOÁVEL'
        elif resp['média'] >= 4:
            resp['situação'] = 'RUIM'
        elif resp['média'] < 4:
            resp['situação'] = 'MUITO RUIM'
    return resp


resp = notas(5, 6, 3, 9, sit=True)
print(resp)
