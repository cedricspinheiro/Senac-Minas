#imc = p / (A x A)

print('Vamos calcular o seu IMC?')
p = float(input('Me fale o seu peso: '))
a = float(input('Me fale sua altura: '))

imc = p / (a*a)
imc_ar = round(imc, 3)

print('O resultado do seu IMC é de:', imc_ar)
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc <= 24.9:
    print('Você está no peso ideal! (Parabéns!!!)')
elif imc <= 29.9:
    print('Você está levemente acima do peso!')
elif imc <= 34.9:
    print('Você está com obesidade grau I')
elif imc <= 39.9:
    print('Você está com obesidade grau II (Reserva)')
else:
    print('Você está com obesidade III (Mórbida)')

