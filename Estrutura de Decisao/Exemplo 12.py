# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
# do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
# Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
# trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor_hora = float(input('Qual é o valor da ganho em hora: '))
quant_hora = float(input('Quantas hora trabalhadas no mês: '))

salario_bruto = valor_hora * quant_hora
sindicato = salario_bruto * .03
fgts = salario_bruto * .11

if salario_bruto <= 900:
    desc_ir = 0
elif salario_bruto <= 1500:
    desc_ir = 5
elif salario_bruto <= 2500:
    desc_ir = 10
else:
    desc_ir = 20

ir = salario_bruto * (desc_ir / 100)
desconto = sindicato + ir
salario_liquido = salario_bruto - desconto

print('Salario Bruto: R${:.2f}'.format(salario_bruto))
print('(-) Sindicato: (3%) R${:.2f}'.format(sindicato))
print('(-) IR(', desc_ir, '%): R${:.2f}'.format(ir))
print('FGTS (11%): R${:.2f}'.format(fgts))
print('Total de descontos: R${:.2f}'.format(desconto))
print('Salario Liquido: R${:.2f}'.format(salario_liquido))
