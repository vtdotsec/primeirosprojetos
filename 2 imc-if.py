peso = float(input('Digite seu peso em Kg: '))
altu = float(input('Digite sua altura em cm: '))
alt = altu / 100
imc = peso / (alt * alt)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')