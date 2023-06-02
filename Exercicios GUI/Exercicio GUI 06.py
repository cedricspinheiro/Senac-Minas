from tkinter import *

def confirmo():
    dados1.config(text='Endereço:')
    dados2.config(text=f'Rua: {rua.get()}; Nº: {numero.get()}; Bairro: {bairro.get()}')
    dados3.config(text=f'Cidade: {cidade.get()}; UF: {uf.get()}; CEP: {cep.get()}.')

janela = Tk()
#janela.geometry('350x350')
janela.title('Cadastro de Endereço')

titulo = Label(janela, text='Entre com os deus dados')
titulo.grid(row=0,column=1)

textorua = Label(janela, text='Rua:')
textorua.grid(row=1, column=0)
textonumero = Label(janela, text='Numero:')
textonumero.grid(row=2, column=0)
textobairro = Label(janela, text='Bairro:')
textobairro.grid(row=3, column=0)
textocidade = Label(janela, text='Cidade:')
textocidade.grid(row=4, column=0)
textouf = Label(janela, text='Uf:')
textouf.grid(row=5, column=0)
textocep = Label(janela, text='CEP:')
textocep.grid(row=6, column=0)

rua = Entry(janela)
rua.grid(row=1, column=1)
numero = Entry(janela)
numero.grid(row=2, column=1)
bairro = Entry(janela)
bairro.grid(row=3, column=1)
cidade = Entry(janela)
cidade.grid(row=4, column=1)
uf = Entry(janela)
uf.grid(row=5, column=1)
cep = Entry(janela)
cep.grid(row=6, column=1)

confirmacao = Label(janela, text='Confirma que os dados inseridos')
confirmacao.grid(row=7, column=1)
confirmacao1 = Label(janela, text='acima estão corretos?')
confirmacao1.grid(row=8, column=1)

botao = Button(janela, text='Confirmo', command=confirmo)
botao.grid(row=9, column=1)

dados1 = Label(janela, text='')
dados1.grid(row=10, column=1)
dados2 = Label(janela, text='')
dados2.grid(row=11, column=1)
dados3 = Label(janela, text='')
dados3.grid(row=12, column=1)

janela.mainloop()