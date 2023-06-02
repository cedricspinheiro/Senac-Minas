# 00/00/0000
while True:  # Aqui começa o loop
    date = input('Digite a data no formato DD/MM/AAAA: ')

    if len(date) == 10:
        if date[2] == '/' and date[5] == '/':
            dia, mes, ano = date.split('/')

            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)

                if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1:
                    break  # A data é válida, encerra o loop
                else:
                    print('Data inválida. Tente novamente.')
            else:
                print('Data inválida. Tente novamente.')
        else:
            print('Data inválida. Tente novamente.')
    else:
        print('Data inválida. Tente novamente.')
if '/01/' in date:
    date = date.replace('/01/', ' de Janeiro de ')
elif '/02/' in date:
    date = date.replace('/02/', ' de Fevereito de ')
elif '/03/' in date:
    date = date.replace('/03/', ' de Março de ')
elif '/04/' in date:
    date = date.replace('/04/', ' de Abril de ')
elif '/05/' in date:
    date = date.replace('/05/', ' de Maio de ')
elif '/06/' in date:
    date = date.replace('/06/', ' de Junho de ')
elif '/07/' in date:
    date = date.replace('/07/', ' de Julho de ')
elif '/08/' in date:
    date = date.replace('/08/', ' de Agosto de ')
elif '/09/' in date:
    date = date.replace('/09/', ' de Setembro de ')
elif '/10/' in date:
    date = date.replace('/10/', ' de Outubro de ')
elif '/11/' in date:
    date = date.replace('/11/', ' de Novembro de ')
elif '/12/' in date:
    date = date.replace('/12/', ' de Dezembro de ')
print(date)
