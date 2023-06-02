num = int(input('digite um numero, para mostrar sua taboada: '))

espoente = 0

while espoente <= 10:
    tabuada = num * espoente
    print(num, 'X', espoente, '=', tabuada)
    espoente += 1
else:
    print('fim da taboada!')
