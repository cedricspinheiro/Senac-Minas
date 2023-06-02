# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
# temperatura em graus Celsius.
#       • C = 5 * ((F-32) / 9).

#  calculo pego da internet: °C = (°F − 32) ÷ 1, 8

temp_fahr = float(input('Digite a temperatura em Fahrenheit: '))
temp_cels = (temp_fahr - 32) / 1.8
temp_cels_ar = round(temp_cels,1)
print('A temperatura em graus celsius é de: ',temp_cels_ar,'ºC')