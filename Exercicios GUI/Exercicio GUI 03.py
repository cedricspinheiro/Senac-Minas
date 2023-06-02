from tkinter import *

def soma():
    calc = float(graus.get())
    resultado = 5 * ((calc - 32) / 9)
    resu.config(text="Cº{:.2f}".format(resultado))

janela = Tk()
janela.geometry('250x120')
janela.title('Calculadoura de temperatura')

texto = Label(janela, text='Entre com a temperatura graus Fahrenheit')
texto.grid(row=0, column=0)

graus = Entry(janela)
graus.grid(row=1, column=0)

txresu = Label(janela, text='Resultado')
txresu.grid(row=2, column=0)
resu = Label(janela, text='')
resu.grid(row=3, column=0)

botao = Button(janela, text='Calcular', command=soma)
botao.grid(row=4, column=0)

janela.mainloop()

