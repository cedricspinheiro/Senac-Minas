# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

valor1 = float(input('Informe o valor do 1° Produto: '))
valor2 = float(input('Informe o valor do 2° Produto: '))
valor3 = float(input('Informe o valor do 3° Produto: '))

if valor1 < valor2 and valor1 < valor3:
    print('O produto mais barato é', valor1)
elif valor2 < valor1 and valor2 < valor3:
    print('O produto mais barato é', valor2)
else:
    print('O produto mais barato é', valor3)