peso = float(input('Informe a quantidade em Kg de peixe pescado no dia: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('Você excedeu o limite diário de peso e deverá pagar uma multa de R$', multa)

else:
    print('Você não excedeu o limite diário de peso, parabéns!')
