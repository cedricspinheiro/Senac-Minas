# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus
# Fahrenheit.

#                 °F = °C × 1, 8 + 32

temp_cels = float(input('Digite a temperatura em celsius: '))
temp_fahr = temp_cels * 1.8 + 32
print('A temperatura em fahrenheit é de: {:.1f}'.format(temp_fahr),"ºF")