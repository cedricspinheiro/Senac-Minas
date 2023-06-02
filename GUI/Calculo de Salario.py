from tkinter import *


def calcular():
    salariob = float(ehora.get()) * float(evalor.get())
    ir = salariob * 0.11
    inss = salariob * .08
    sindicato = salariob * 0.05
    liquido = salariob - ir - inss - sindicato
    exsalariob.config(text='{:.2f}'.format(salariob))
    exir.config(text='{:.2f}'.format(ir))
    exinss.config(text='{:.2f}'.format(inss))
    exsindicato.config(text='{:.2f}'.format(sindicato))
    exsalariol.config(text='{:.2f}'.format(liquido))


janela = Tk()
janela.config(borderwidth=10)
janela.title('Calculo de Salario')
janela.option_add('*Font', 'Arial 12')
janela.option_add('*Foreground', 'Red')

quadro_entrada = LabelFrame(janela, text='Entrada de Dados', labelanchor='n', font='Verdana 12 bold', borderwidth=1, fg='#AE31CB')
quadro_entrada.grid(row=0, column=0, sticky='we', columnspan=3)
quadro_entrada.config(borderwidth=10)

horas = Label(quadro_entrada, text='Horas Trabalhadas:', anchor='e')
horas.grid(row=0, column=0, sticky='we')
valor = Label(quadro_entrada, text='Valor da Hora:', anchor='e')
valor.grid(row=1, column=0, sticky='we')

ehora = Entry(quadro_entrada)
ehora.grid(row=0, column=1)
evalor = Entry(quadro_entrada)
evalor.grid(row=1, column=1)

botao = Button(quadro_entrada, text='Calcular', command=calcular)
botao.grid(row=1, column=2, sticky='we', padx=10)

barra = LabelFrame(janela, text='Saida de Dados', labelanchor='n', font='Verdana 12 bold', borderwidth=1, fg='#AE31CB')
barra.grid(row=2, column=0, columnspan=3, sticky='we')
barra.config(borderwidth=10)

txsalariob = Label(barra, text='+ Salario Bruto: R$', anchor='e')
txsalariob.grid(row=0, column=0, sticky='we')
txir = Label(barra, text='- IR (11%): R$', anchor='e')
txir.grid(row=1, column=0, sticky='we')
txinss = Label(barra, text='- INSS (8%): R$', anchor='e')
txinss.grid(row=2, column=0, sticky='we')
txsindicato = Label(barra, text='- Sindicato (5%): R$', anchor='e')
txsindicato.grid(row=3, column=0, sticky='we')
txsalariol = Label(barra, text='= Salário Liquido: R$', anchor='e')
txsalariol.grid(row=4, column=0, sticky='we')

exsalariob = Label(barra, text='', anchor='w')
exsalariob.grid(row=0, column=1, sticky='we')
exir = Label(barra, text='', anchor='w')
exir.grid(row=1, column=1, sticky='we')
exinss = Label(barra, text='', anchor='w')
exinss.grid(row=2, column=1, sticky='we')
exsindicato = Label(barra, text='', anchor='w')
exsindicato.grid(row=3, column=1, sticky='we')
exsalariol = Label(barra, text='', anchor='w')
exsalariol.grid(row=4, column=1, sticky='we')

janela.mainloop()
