print('Faça o seu cadastro')
login = input('Cadastre o seu USUARIO: ')
senha = input('Cadastre sua SENHA: ')
print('Cadastro completo!')
print('\n\n\nFaça o login com o usuario cadastrado!')
login2 = input('Entre com o seu login: ')
senha2 = input('Entre com a sua sanha: ')

if login == login2 and senha == senha2:
    print('Login realizado com sucesso!')
else:
    print('USUARIO ou SENHA estão incorretos')
