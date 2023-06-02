#exercicio 9
pf = input("CPF(xxx.xxx.xxx-xx) :")

for letra in cpf:
    if(cpf[1] !=".") or (cpf[5] !=".") or (cpf[11] !="-"):
        cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")
    else:
        print("O 'CPF' está no formato correto")
