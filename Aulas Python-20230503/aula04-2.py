#entrada
nome = input('Entre com seu nome: ')
idade = input('Entre com sua idade: ')

#saida
print('Olá, meu nome é', nome, ', tenho', idade, 'anos!')

if idade < '18':
    print('Sou menor de idade.')
else:
    print('Sou maior de idade.')