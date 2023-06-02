valor = float(input('Digite o valor do produto ou digite 0 para sair: '))
total = 0
desc = 0

while valor != 0:
    if valor > 0:
        total += valor
    else:
        print('Você digitou um valor NEGATIVO!')
    valor = float(input('Digite o valor do produto ou digite 0 para sair: '))
else:
    if total > 1000:
        desc = total * 0.1
        total -= desc
    print('O valor informado foi R$', total, 'desconto de R$', desc)
