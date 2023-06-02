print('cadastro de usuario e senha.')
usuario = input('Digite o usuario para cadastro: ')
senha = input('Dgite a senha para cadastro: ')

print('Login com o usuário cadastrado.')
in_usuario = input('Informe o usuário: ')
in_senha = input('Informa a senha: ')

if in_usuario == usuario and in_senha == senha:
    print('Login efetuado com sucesso!!!')

else:
    print('Falha no login. \nUsuário / Senha incorreto')