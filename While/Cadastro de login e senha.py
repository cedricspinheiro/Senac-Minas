login=input('Cadastre um login: ')
senha=input('Cadastre ema senha: ')

while True:
    novo_login=input('Digite seu login: ')
    nova_senha=input('Digite sua senha: ')

    if novo_login == login:
        if nova_senha == senha:
            print('Login realizado com sucesso!')
            break
        else:
            print('Login ou senha invalida!')
    else:
        print('Login ou senha invalida!')