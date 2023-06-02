from tkinter import *

def somar():
    total = float(enota1.get()) + float(enota2.get()) + float(enota3.get()) + float(enota4.get())
    soma = total / 4
    media.config(text=soma)

janela = Tk()
janela.geometry('450x150')
janela.title('Medias Bimestrais')

nota1 = Label(janela, text='1ª Nota:')
nota1.grid(row=0, column=0)
nota2 = Label(janela, text='2ª Nota:')
nota2.grid(row=1, column=0)
nota3 = Label(janela, text='3ª Nota:')
nota3.grid(row=2, column=0)
nota4 = Label(janela, text='4ª Nota:')
nota4.grid(row=3, column=0)

enota1 = Entry(janela)
enota1.grid(row=0, column=1)
enota2 = Entry(janela)
enota2.grid(row=1, column=1)
enota3 = Entry(janela)
enota3.grid(row=2, column=1)
enota4 = Entry(janela)
enota4.grid(row=3, column=1)

txmedia = Label(janela, text='Media Final:')
txmedia.grid(row=4, column=0)

media = Label(janela, text='')
media.grid(row=4, column=1)

botao = Button(janela, text='Resultado', command=somar)
botao.grid(row=5, column=0)

janela.mainloop()