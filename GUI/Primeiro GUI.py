from tkinter import *

janela = Tk()
janela.geometry('300x50')
janela.title('Primeira GUI')

texto = Label(janela, text='Olá Mundo')
texto.grid(row=0, column=0)

texto2 = Label(janela, text='By NKKara')
texto2.grid(row=1, column=5)

janela.mainloop()