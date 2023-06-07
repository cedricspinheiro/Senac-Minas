from tkinter import *

janela = Tk()
janela.title('Calculadora Amadora')
janela.config(borderwidth=10)
janela.option_add('*Font', 'Arial 10 bold')

historico = LabelFrame(janela)
historico.grid(row=0, column=0, sticky='we')
historico.config(padx=10, pady=10)

histcalc = Label(historico, text='', anchor='e')
histcalc.grid(row=0, column=0, sticky='we')

telacalculo=LabelFrame(janela)
telacalculo.grid(row=1, column=0, sticky='we')
telacalculo.config(pady=10)

entrada = Entry(telacalculo)
entrada.grid(row=0, column=0, sticky='we')

funcao = LabelFrame(janela)
funcao.grid(row=2, column=0)
funcao.config(padx=10, pady=10)
funcao.option_add('*width', '5')

bbspace = Button(funcao, background='Red', text='C')
bbspace.grid(row=0, column=0)
bparent1= Button(funcao, text='(')
bparent1.grid(row=0, column=1)
bparent2= Button(funcao, text=')')
bparent2.grid(row=0, column=2)
bmod = Button(funcao, text='mod')
bmod.grid(row=0, column=3)
bpi = Button(funcao, text='π')
bpi.grid(row=0, column=4)

num7 = Button(funcao, text='7')
num7.grid(row=1, column=0)
num8= Button(funcao, text='8')
num8.grid(row=1, column=1)
num9= Button(funcao, text='9')
num9.grid(row=1, column=2)
bdiv = Button(funcao, text='÷')
bdiv.grid(row=1, column=3)
braiz = Button(funcao, text='√')
braiz.grid(row=1, column=4)

num4 = Button(funcao, text='4')
num4.grid(row=2, column=0)
num5= Button(funcao, text='5')
num5.grid(row=2, column=1)
num6= Button(funcao, text='6')
num6.grid(row=2, column=2)
bvez = Button(funcao, text='x')
bvez.grid(row=2, column=3)
besp = Button(funcao, text='X²')
besp.grid(row=2, column=4)

num1 = Button(funcao, text='4')
num1.grid(row=3, column=0)
num2= Button(funcao, text='5')
num2.grid(row=3, column=1)
num3= Button(funcao, text='6')
num3.grid(row=3, column=2)
bmen = Button(funcao, text='x')
bmen.grid(row=3, column=3)
igual= Button(funcao, text='=', background='Green')
igual.grid(row=3,column=4, rowspan=2, sticky='ns')

num0 = Button(funcao, text='0')
num0.grid(row=4, column=0)
bvirg= Button(funcao, text=',')
bvirg.grid(row=4, column=1)
bporc= Button(funcao, text='%')
bporc.grid(row=4, column=2)
bsoma = Button(funcao, text='+')
bsoma.grid(row=4, column=3)

janela.mainloop()