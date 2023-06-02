# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
total = 0
media = 0
count = 0

while True:
    nota = input('Insira sua nota (de 0 a 10 ou "Resultado" para encerrar): ')

    if nota == 'Resultado':
        break

    nota = float(nota)

    if 0 <= nota <= 10:
        total += nota
        count += 1
    else:
        print('Digite um valor válido!')

if count > 0:
    media = total / count
    print(f'O total das suas notas é: {total}. A média é: {media}')
else:
    print('Nenhuma nota válida foi inserida.')
