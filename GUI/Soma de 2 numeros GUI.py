from tkinter import *


def soma():
    igual = float(entrada1.get()) + float(entrada2.get())
    resu.config(text='= ' + str(igual))


def subt():
    igual = float(entrada1.get()) - float(entrada2.get())
    resu.config(text='= ' + str(igual))


def mult():
    igual = float(entrada1.get()) * float(entrada2.get())
    resu.config(text='= ' + str(igual))


def divi():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())

    if valor1 != 0 and valor2 != 0:
        igual = valor1 / valor2
        resu.config(text='= ' + str(igual))
    else:
        resu.config(text='= 0')


janela = Tk()
janela.geometry('400x50')
janela.title('Soma de 2 Numeros!')

entrada1 = Entry(janela)
entrada1.grid(row=0, column=0)

entrada2 = Entry(janela)
entrada2.grid(row=0, column=1)

resultado = Label(janela, text='RESULTADO')
resultado.grid(row=1, column=0)

resu = Label(janela, text='=')
resu.grid(row=1, column=1)

botao1 = Button(janela, text='+', command=soma)
botao1.grid(row=0, column=3)
botao2 = Button(janela, text='-', command=subt)
botao2.grid(row=0, column=4)
botao3 = Button(janela, text='X', command=mult)
botao3.grid(row=1, column=3)
botao4 = Button(janela, text='/', command=divi)
botao4.grid(row=1, column=4)

janela.mainloop()
