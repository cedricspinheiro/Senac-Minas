#           Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#           quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# • Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
# preços em 3 situações:
# • comprar apenas latas de 18 litros;
# • comprar apenas galões de 3,6 litros;
# • misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente
# 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


metros = float(input('Digite a area de em metros² a ser pintada: '))

litros = metros / 6
latas = int(litros / 18)
galoes = int(litros / 3.6)

# Tinta 18L
print('Caso queira só latas de 18L')
latasA = int(litros / 18)
if litros % 18 != 0:
    latasA += 1
precoA = latasA * 80
print('Você precisará de', latasA, 'latas 18L de tinta')
print('Preço total: R$', precoA)

# Galões 3.6L
print('Caso queira só galões de 3.6L')
galoesA = int(litros / 3.6)
if litros % 3.6 != 0:
    galoesA += 1
precoB = galoesA * 25
print('você presisa de', galoesA,'galões 3.6L de tinta')
print('Preço total: R$',precoB)

# Misturado + 10%
print('Caso queira a mistura de latas e galões com uma folga')
litro_folga = (metros / 6) * 1.1
total_latas = int(litro_folga // 18)
total_sobra = litro_folga % 18
total_galoes = int(total_sobra // 3.6)
if total_sobra % 3.6 != 0:
    total_galoes += 1
total_preco = total_latas * 80 + total_galoes * 25
print('Serão necessárias', total_latas,'latas de 18L e', total_galoes,'galões de 3.6L')
print(f'No valor total de R${total_preco:.2f}.')