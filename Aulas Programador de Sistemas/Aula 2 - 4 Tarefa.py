#imc = p / (A x A)

print('Vamos calcular o seu IMC?')
p = float(input('Me fale o seu peso: '))
a = float(input('Me fale sua altura: '))

imc = p / (a*a)
imc_ar = round(imc, 3)

print('O resultado do seu IMC é de:',imc_ar)