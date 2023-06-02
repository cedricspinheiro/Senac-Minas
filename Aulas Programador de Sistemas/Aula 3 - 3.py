nome = input('Escreva seu nome: ')
idade = int(input('Escreva sua idade: '))

print("Ola, ",nome, ", sua idade é de: ", idade," anos.")

if idade <= 17:
    print('Você é menor de idade!')
else:
    print('Você é maior de idade!')
