from tkinter import *

def salvar():
    with open('Contatos.txt', 'a') as arquivo:
        arquivo.write((f'Nome: {enome.get()}, Celular: {ecelular.get()}\n'
                       f'Email: {eemail.get()}, Observações: {eobservacao.get()}\n\n'))

def pesquisar():
    janela2 = Tk()


janela = Tk()
janela.title('Agenda de Contatos')
janela.option_add('*Font', 'Arial 8 bold')
janela.config(padx=10, pady=10)

novo_contato = LabelFrame(janela, text='Novo Contato', labelanchor='n')
novo_contato.grid(row=0, column=0, sticky='we')
novo_contato.config(padx=10, pady=10)

nome = Label(novo_contato, text='Nome:', anchor='e')
nome.grid(row=0, column=0, sticky='we')
enome = Entry(novo_contato)
enome.grid(row=0, column=1, sticky='we')

celular = Label(novo_contato, text='Celular:', anchor='e')
celular.grid(row=0, column=2, sticky='we')
ecelular = Entry(novo_contato)
ecelular.grid(row=0, column=3, sticky='we')

email = Label(novo_contato, text='Email:', anchor='e')
email.grid(row=1, column=0, sticky='we')
eemail = Entry(novo_contato)
eemail.grid(row=1, column=1, sticky='we')

observacao = Label(novo_contato, text='Observação:', anchor='e')
observacao.grid(row=1, column=2, sticky='we')
eobservacao = Entry(novo_contato)
eobservacao.grid(row=1, column=3, sticky='we,ns', rowspan=2)

telefone = Label(novo_contato, text='Telefone:', anchor='e')
telefone.grid(row=2, column=0, sticky='we')
etelefone = Entry(novo_contato)
etelefone.grid(row=2, column=1, sticky='we')

salvar = Button(novo_contato, text='Salvar', anchor='w', command=salvar)
salvar.grid(row=3, column=2)
pesquisar = Button(novo_contato, text='Pesquisar', anchor='e', command=pesquisar)
pesquisar.grid(row=3, column=1)

janela.mainloop()
