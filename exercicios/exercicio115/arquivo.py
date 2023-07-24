from interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        print(f'Arquivo {nome} já existe.')
        return True


def criararquivo(nome):
    a = open(nome, 'wt+')
    a.close
    print(f'Arquivo {nome} foi criado com sucesso.')

def lerarquivo(nome):
    a = open(nome, 'rt')
    cabeçalho('Pessoas cadastradas')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    a.close()

def cadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ouve um erro na hora de escrever dados')
    else:
        a.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado.')
        a.close()
