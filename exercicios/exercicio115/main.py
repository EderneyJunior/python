from interface import *
from time import sleep
from arquivo import *

arq = 'CursoEmVideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    res = menu('Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do sistema')
    if res == 1:            
        lerarquivo(arq)
    elif res == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastro(arq, nome, idade)
    elif res == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
