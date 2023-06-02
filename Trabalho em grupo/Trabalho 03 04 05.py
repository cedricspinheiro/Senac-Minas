# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#
# F
# U
# L
# A
# N
# O

vocal = input('Digite uma frase ou palavra: ')

# Atividade 3
print('ATIVIDADE 3')
for caractere in vocal:
    print(caractere)

# Atividade 4
print('\n\nATIVIDADE 4')
x = ''
for caractere in vocal:
    x += caractere
    print(x)

# Arividade 5
print('\n\nATIVIDADE 5')
for i in range(len(vocal), 0, -1):
    print(vocal[:i])