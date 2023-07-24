# mostre o nome com todas as letras maiusculas e minusculas, quantas letras sem considerar espaços e quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome: ")).strip()

print(f"O seu nome maiusculo fica: {nome.upper()} \nO seu nome minuscolo fica: {nome.lower()}")
dividido = nome.split()
print(f"""O seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras
Seu nome inteiro tem {len(nome) - nome.count(' ')} letras""")
