# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua sugunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4:
    print(f'Suas notas são {nota1} e {nota2}, a media é {media}e sua nota é E. Você está REPROVADO!')
elif media <= 6:
    print(f'Suas notas são {nota1} e {nota2}, a media é {media}e sua nota é D. Você está REPROVADO!')
elif media <= 7.5:
    print(f'Suas notas são {nota1} e {nota2}, a media é {media}e sua nota é C. Você está APROVADO!')
elif media <= 9:
    print(f'Suas notas são {nota1} e {nota2}, a media é {media}e sua nota é B. Você está APROVADO!')
else:
    print(f'Suas notas são {nota1} e {nota2}, a media é {media}e sua nota é A. Você está APROVADO!')