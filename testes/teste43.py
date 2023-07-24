alt = float(input('Digite sua altura em centimetros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso / ((alt**2) / 10000)

if imc <= 18.5:
    print(f'Seu imc é {imc:.2f} e você esta abaixo do peso')
elif imc > 18.5 and imc <= 25:
     print(f'Seu imc é {imc:.2f} e você esta no peso ideal')
elif imc > 25 and imc <= 30:
      print(f'Seu imc é {imc:.2f} e você esta com sobre peso')
elif imc > 30 and imc <= 40:
      print(f'Seu imc é {imc:.2f} e você esta obeso')
else:
      print(f'Seu imc é {imc:.2f} e você esta com obesidade mórbida') 
