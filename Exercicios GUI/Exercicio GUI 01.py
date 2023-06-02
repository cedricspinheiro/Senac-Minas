from tkinter import *

def imc():
    resuimc = float(peso.get()) / float(altura.get())**2
    imcresu.config(text='{:.3}'.format(resuimc))
    if resuimc <= 18.5:
        resuresu='Você está abaixo do peso!'

    elif resuimc >= 18.6 and resuimc <= 24.9:
        resuimc='Você está no peso normal!'

    else:
        resuresu='Você está acima do peso!'
    resultadoresu.config(text=resuresu)


janela = Tk()
janela.geometry('750x150')
janela.title('Bem vindo a calculadora de IMC')

texto = Label(janela, text='Calculadora')
texto.grid(row=0, column=1)
texto1 = Label(janela, text='IMC')
texto1.grid(row=0, column=2)

peso_texto = Label(janela, text='Digite seu peso:')
peso_texto.grid(row=1, column=0)
peso = Entry(janela)
peso.grid(row=1, column=1)

altura_texto = Label(janela, text='Digite sua Altura:')
altura_texto.grid(row=1, column=2)
altura = Entry(janela)
altura.grid(row=1, column=3)

botao = Button(janela, text='Calcular', command=imc)
botao.grid(row=1, column=4)

imc = Label(janela, text='IMC:')
imc.grid(row=2, column=0)
imcresu = Label(janela, text='')
imcresu.grid(row=2, column=1)

resultado = Label(janela, text='Resultado')
resultado.grid(row=3, column=0)
resultadoresu = Label(janela, text='')
resultadoresu.grid(row=3, column=1)

janela.mainloop()
