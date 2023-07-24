tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 
'Athletico - PR', 'Atletico - MG', 'Fortaleza', 'São Paulo', 'América - MG',
 'Botafogo', 'Santos', 'Goías', 'Bragantino', 'Coritiba',
   'Cuíaba', 'Ceará', 'Atletico - GO', 'Avai', 'Juventude')
print('Os 5 primeiros colocadods são: ')
for c in range(0, 5):
    print(f'{tabela[c]}')
print(f'\nOs times rebaixados foram: ')
for n in range(16, 20):
    print(f'{tabela[n]}')
print(f'\nOs times em ordem alfábetica são: {sorted(tabela)}')
print(f'\nO santos esta em {tabela.index("Santos") + 1}° colocado')
