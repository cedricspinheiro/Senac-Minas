import random

# Lista de palavras para o jogo
palavras = ['python', 'programacao', 'computador', 'jogos', 'desenvolvimento']

# Seleciona uma palavra aleatoriamente
palavra = random.choice(palavras)

# Inicializa as variáveis
acertos = []
erros = []
tentativas = 6

while True:
    # Exibe a palavra com os acertos até o momento
    resultado = ''
    for letra in palavra:
        if letra in acertos:
            resultado += letra
        else:
            resultado += '_ '
    print(resultado)

    # Verifica se o jogador ganhou
    if set(palavra) == set(acertos):
        print('Parabéns! Você ganhou!')
        break

    # Verifica se o jogador perdeu
    if len(erros) == tentativas:
        print('Você perdeu! A palavra era', palavra)
        break

    # Pede uma letra ao jogador
    letra = input('Digite uma letra: ')

    # Verifica se a letra já foi digitada antes
    if letra in acertos or letra in erros:
        print('Você já digitou essa letra. Tente novamente.')
        continue

    # Verifica se a letra está na palavra
    if letra in palavra:
        acertos.append(letra)
    else:
        erros.append(letra)
        print('A letra', letra, 'não está na palavra. Tentativas restantes:', tentativas - len(erros))