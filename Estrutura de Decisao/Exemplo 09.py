# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Informe o 1° numero: '))
n2 = float(input('Informe o 2° numero: '))
n3 = float(input('Informe o 3° numero: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(n1, n2, n3)
    else:
        print(n1, n3, n2)
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(n2, n1, n3)
    else:
        print(n2,n3,n1)
else:
    if n1 > n2:
        print(n3, n1, n2)
    else:
        print(n3, n2, n1)