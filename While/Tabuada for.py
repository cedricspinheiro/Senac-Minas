num = int(input('digite um numero, para mostrar sua taboada: '))

for espoente in range(0, 11):
    tabuada = num * espoente
    print(num, 'X', espoente, '=', tabuada)