# . Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
# são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça
# um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Horas trabalhadas no mês **:**     Ganho por hora R$****,**
#                                                    + Salário bruto: R$****,**
#                                                    - IR (11%): R$****,**
#                                                    - INSS (8%): R$****,**
#                                                    - Sindicato (5%): R$****,**
#                                                    = Salário Líquido: R$****,**
#Obs.: Salário Bruto R$****,** - Descontos R$****,** = Salário Líquido R$****,**

ganho_hora = float(input('Informe quanto você ganha por hora: '))
hora_mes = float(input('Informe quantas horas você trabalhou no ultimo mês: '))

salario_bruto = ganho_hora * hora_mes
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato
descontos = salario_bruto - salario_liquido

print('Horas trabalhadas no mês: ',hora_mes,'.     Ganho por hora R$',ganho_hora)
print('                                                     + Salário bruto: R$',salario_bruto)
print('                                                     - IR (11%): R$',ir)
print('                                                     - INSS (8%): R$', inss)
print('                                                     - Sindicato (5%): R$',sindicato)
print('                                                     = Salário Líquido: R$',salario_liquido)
print('Obs.: Salário Bruto R$',salario_bruto,' - Descontos R$',descontos,' = Salário Líquido R$',salario_liquido)