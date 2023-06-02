print('Bem-vondo a calculadora de IMC!')
peso = float(input('Entre com o peso em "kilogramas": '))
altura = float(input('Entre com a altura em "metros": '))

imc = peso / altura**2

print('O imc é/:', imc)

if imc <= 18.5:
    print('Você está abaixo do peso!')

elif imc >=18.6 and imc <= 24.9:
    print('Você está no peso normal!')

else:
    print('Você está acima do peso!')