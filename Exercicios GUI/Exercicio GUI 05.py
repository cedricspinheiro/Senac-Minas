from tkinter import *


def calcular():
    if float(peso.get()) > 50:
        excesso = float(peso.get()) - 50
        multap = excesso * 4
        excedeu.config(text='Você excedeu o limite diário em: ' + str(excesso) + 'Kg')
        multa.config(text='Devera pagar uma multa de R$' + str(multap))
    else:
        excedeu.config(text='Parabens!!!')
        multa.config(text='Você não excedeu o limite diario de peso!')


janela = Tk()
#janela.geometry('375x375')
janela.title('Calculadora de Excesso')

texto = Label(janela, text='Informe a quantidade em Kg de peixe pescado no dia:')
texto.grid(row=0, column=0)

peso = Entry(janela)
peso.grid(row=1, column=0)

botao = Button(janela, text='Calcular', command=calcular)
botao.grid(row=2, column=0)

excedeu = Label(janela, text='')
excedeu.grid(row=3, column=0)
multa = Label(janela, text='')
multa.grid(row=4, column=0)

janela.mainloop()
