total = 0
num1 = float(input('Digite um número: '))
menu = ''
total += num1

while menu != '5':
    menu = input('\nEntre com as opções a seguir:'
                 '\n1- Somar:'
                 '\n2- Subtrair:'
                 '\n3- Dividir:'
                 '\n4- Multiplicar:'
                 '\n5- Sair'
                 '\nC- Zerar número\n').upper()

    if (1 <= int(menu) <= 5) or (menu == 'C'):
        if menu == 'C':
            total = 0
            continue

        num2 = float(input('Digite um número: '))

        if menu == '1':
            total += num2
        elif menu == '2':
            total -= num2
        elif menu == '3':
            if num2 != 0:
                total /= num2
            else:
                print('\nA divisão não pode ser feita por ZERO\n')
                continue
        elif menu == '4':
            total *= num2
    else:
        print('Digite uma opção válida!')
        continue

    print(f'\nTotal: {total}\n')
