print('Informe as 4 notas bimestrais!')

nota_1=float(input('Nota 1° bimestre: '))
nota_2=float(input('Nota 2° bimestre: '))
nota_3=float(input('Nota 3° bimestre: '))
nota_4=float(input('Nota 4° bimestre: '))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

print('Sua média final é:', media)

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')