# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
# ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = float(input('Digite a área em metros² a ser pintada: '))

litros = metros / 3
latas = int(litros / 18)
if litros % 18 != 0:
    latas += 1
preco_total = latas * 80

print('Você precisará de', latas, 'latas de tinta')
print('Preço total: R$', preco_total)