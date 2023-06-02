# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Digite a area do circulo:'))
pi = 3.14159265359
area = pi * raio ** 2
area_ar = round(area, 2)
print('A área do círculo é:', area_ar)