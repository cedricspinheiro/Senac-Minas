# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


num = float(input('Digite um numero: '))

if num < 0:
    print('Numero negativo!')
elif num == 0:
    print('Numero igual a zero!')
else:
    print('Numero positivo')
