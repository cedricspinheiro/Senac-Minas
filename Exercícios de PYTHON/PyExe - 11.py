# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       a. o produto do dobro do primeiro com metade do segundo.
#       b. a soma do triplo do primeiro com o terceiro.
#       c. o terceiro elevado ao cubo.

n1 = int(input('Digite o primeiro numero (inteiro): '))
n2 = int(input('Digite o segundo numero (inteiro): '))
n3 = float(input('Digite o terceiro numero (real): '))
print('Produto A: ', (n1 * 2) * (n2 / 2))
print('produto B: ', (n1 * 3) + n3)
print('Produto C: ', n3 ** 3)
