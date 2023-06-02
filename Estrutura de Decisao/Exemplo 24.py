# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
t_oper = int(input('Qual operação você deseja?\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - multiplicação\nNumero: '))
if t_oper == 1:
    resu = num1 + num2
elif t_oper == 2:
    resu = num1 - num2
elif t_oper == 3:
    resu = num1 / num2
elif t_oper == 4:
    resu = num1 * num2
else:
    print('Digite uma operação certa')

if resu > 0:
    porc = 'POSITIVO'
else:
    porc = 'NEGATIVO'

if resu % 2 == 0:
    print('A conta deu:',resu,'alem de ser PAR, ele é',porc)
else:
    print('A conta deu:',resu,'alem de ser IMPAR, ele é',porc)
