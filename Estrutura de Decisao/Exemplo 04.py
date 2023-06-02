# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Informe uma letra: ').upper()
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(letra, 'é uma vogal!')
elif letra.isnumeric():
    print('Você digitou um numero!')
else:
    print(letra, 'é uma consoante!')
