from tkinter import *

def clique():
    texto3.config(text=entrada.get())

janela = Tk()
janela.geometry('250x75')
janela.title('Terceiro GUI')

texto = Label(janela, text='Olá Mundo')
texto.grid(row=0, column=0)
texto2 = Label(janela, text='Meu Nome é:')
texto2.grid(row=1, column=0)
texto3 = Label(janela, text='')
texto3.grid(row=1, column=1)

entrada = Entry(janela)
entrada.grid(row=2, column=0)

botao = Button(janela, text='Clique Aqui!', command=clique)
botao.grid(row=2, column=1)

janela.mainloop()