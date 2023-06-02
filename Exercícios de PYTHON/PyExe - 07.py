# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o valor do lado do quadrado: '))
area = lado ** 2
area_ar = round(area, 2)
dobro = area * 2
dobro_ar = round(dobro, 2)
print('A área do quadrado é:', area_ar)
print('O dobro da área do quadrado é:', dobro_ar)