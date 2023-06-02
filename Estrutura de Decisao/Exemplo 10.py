# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

tempo = input('Digite em qual turno você está: M-matutino ou V-Vespertino ou N- Noturno: ').upper()
if tempo == 'M':
    print('Tenha um Bom Dia!')
elif tempo == 'V':
    print('Tenha uma Otima Tarde!')
elif tempo == 'N':
    print('Tenha uma Otima Noite!')
else:
    print('Você digitou o Valor Invalido!')