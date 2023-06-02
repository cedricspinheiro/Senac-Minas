# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

semana=int(input('Digite um numero: '))
if semana == 1:
    print('Hoje é DOMINGO, descanse bem que amanhã é dia de trabalhar!')
elif semana == 2:
    print('Hoje é SEGUNDA, hoje é dia de trabalhar preguicinha!')
elif semana ==3:
    print('Hoje é TERÇA, continua sendo dia de trabalhar!')
elif semana ==4:
    print('Hoje é QUARTA, Calma estamos do meio do caminho!')
elif semana ==5:
    print('Hoje é QUINTA, Muita calma nessa hora! não é hojé, mais já se prepara para amanhã!')
elif semana ==6:
    print('Hoje é... \nHoje é... \nHOJE É SEXTAAAA! SEXTOU BEBE!')
elif semana ==7:
    print('Shhh...\nHoje é SABADO! Vamos brincar de silencio que a ressaca ta braba!')
elif semana > 7:
    print('Digite um numero entre 1 a 7')
else:
    print('Valor Invalido')
