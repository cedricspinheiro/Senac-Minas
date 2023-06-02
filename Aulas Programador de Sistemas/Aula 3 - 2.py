n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 != 0 and n2 != 0:
    soma = n1 + n2
    subtracao = n1 - n2
    divisao = n1 / n2
    div_ar = round(divisao, 2)
    multiplicacao = n1 * n2
    print('A soma dos numeros são:', soma, '\nA subtração dos numeros são:', subtracao, '\nA divisão dos numeros são:', div_ar, '\nA multiplicação dos numeros são:', multiplicacao)

else:
    print('O numero deve ser diferente de 0')