# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
# da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
# registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...
total = 0
qnt = 0
dinheiro = 0
print('LOJAS TABAJARA')
while True:
    valor = float(input(f'{qnt}- Informe o valor do produto ou 0 para sair: '))
    if valor != 0:
        if valor > 0:
            total += valor
            qnt += 1

    elif valor == 0:
        while True:
            print(f'Total da compra: {qnt} Itens, Valor total R${total}.')
            dinheiro = float(input('Dinheiro R$'))
            if dinheiro < total:
                print(f'Valor informado (R${dinheiro}) menor que o valor total da compra (R${total})')
                continue
            elif dinheiro > total:
                print(f'Troco R${dinheiro - total:.2f}')
                break
    else:
        print('Informe um valor valido!')
        continue
    print(f'Valor total {total}')
