# faça um programa que leia um numero de 0 a 9999 e os digite separadamente 
num = int(input("Digite um numero de 0 a 9999: "))

print(f"O numero {num} esta sendo analisado...")
print(f"""Unidade: {num // 1 % 10} \nDezena: {num // 10 % 10}
Centena: {num // 100 % 10} \nMilhar {num // 1000 % 10}""")
