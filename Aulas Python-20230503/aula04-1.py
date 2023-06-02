#entrada
print('Bem-vondo a calculadora de IMC!')
peso = float(input('Entre com o peso em "kilogramas": '))
altura = float(input('Entre com a altura em "metros": '))

#processamento
imc = peso / altura**2

#saida
print('O imc é/:', imc)

## condicionais
### 1ª condição
if imc <= 18.5:
    print('Você está abaixo do peso!')

### 2ª condição
elif imc >=18.6 and imc <= 24.9:
    print('Você está no peso normal!')

### 3ª condição
else:
    print('Você está acima do peso!')