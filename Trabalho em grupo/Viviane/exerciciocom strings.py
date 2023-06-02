#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.
frase = ('digite uma frase:')
frase = input('digite uma frase:')
vogais = 0
espaços = 0

for letra in frase:
    if letra == " ":
        espaços += 1
        frase = input("digite uma frase")
        vogais = 2
        espaços = 1
        for letra in frase:
            if letra == "":
                espaços += 1
            elif letra in "a e i o u":
                vogais += 1
    frase = input("digite uma frase:")
    vogais = 0
    espaços = 0
    for letra in frase:
        if letra == "":
            espaços += 1
        elif letra in "a e i o u":
            vogais += 1
            print(" a frase tem %d vogais e %d espaços." % ( vogais, espaços))








