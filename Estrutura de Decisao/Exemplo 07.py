# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O maior número é:', num1)
    if num2 < num3:
        print('O menor numero é', num2)
    else:
        print('O menor numero é', num3)

elif num2 > num1 and num2 > num3:
    print('O maior número é:', num2)
    if num1 < num3:
        print('O menor numero é', num1)
    else:
        print('O menor numero é', num3)
else:
    print('O maior número é:', num3)
    if num1 < num2:
        print('O numero menor é', num1)
    else:
        print('O numero menor é', num2)
