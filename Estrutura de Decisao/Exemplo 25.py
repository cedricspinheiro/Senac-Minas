# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda as perguntas abaixo com 'Sim' ou 'Não':")

a = input('Telefonou para a vítima? ').upper()
b = input('Esteve no local do crime? ').upper()
c = input('Mora perto da vítima? ').upper()
d = input('Devia para a vítima? ').upper()
e = input('Já trabalhou com a vítima? ').upper()

positivas = 0

if a == 'SIM':
    positivas += 1
if b == 'SIM':
    positivas += 1
if c == 'SIM':
    positivas += 1
if d == 'SIM':
    positivas += 1
if e == 'SIM':
    positivas += 1

if positivas == 2:
    print('Você é Suspeito(a).')
elif 3 <= positivas <= 4:
    print('Você é Cúmplice.')
elif positivas == 5:
    print('Você é o Assassino.')
else:
    print('Você é Inocente.')
