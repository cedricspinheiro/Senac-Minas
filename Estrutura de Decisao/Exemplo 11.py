# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print('Aumento Organizações Tabajala')

salario = float(input('Digite o seu Salario ATUAL: '))

if salario <= 280:
    porcento = 20
elif salario <= 700:
    porcento = 15
elif salario <= 1500:
    porcento = 10
else:
    porcento = 5

aumento = salario * porcento / 100
salario_novo = salario + aumento

print('O salário antes do reajuste: R$ {:.2f}'.format(salario))
print('O percentual de aumento aplicado: {}%'.format(porcento))
print('O valor do aumento: R$ {:.2f}'.format(aumento))
print('O novo salário, após o aumento: R$ {:.2f}'.format(salario_novo))