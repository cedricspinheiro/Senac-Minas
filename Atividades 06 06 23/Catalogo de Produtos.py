from tkinter import *

def salvar():
    with open('/home/nkkara/Documentos/Repertorios/Senac Minas/Atividades 06 06 23/Produtos.txt', 'a') as arquivo:
        arquivo.write(
            f'Nome do Produto: {nome_produto.get()}, Preço: {preco_produto.get()}, Quantidade: {quantidade_produto.get()}, Descrição do produto: {descricao_produto.get()}')
        arquivo.write('\n')
        arquivo.close()

    exibir_produtos()
    nome_produto.delete(0, END)
    preco_produto.delete(0, END)
    quantidade_produto.delete(0, END)
    descricao_produto.delete(0, END)

    mensagem.config(text='Produto salvo com sucesso!')

def exibir_produtos():
    produtos_text.delete('1.0', END)
    with open('/home/nkkara/Documentos/Repertorios/Senac Minas/Atividades 06 06 23/Produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            linha_formatada = '{:<20}{:<15}{:<15}{:<20}'.format(*partes)
            produtos_text.insert(END, linha_formatada + '\n')


janela = Tk()
janela.title("Catálogo de Produtos")
janela.option_add('*Font', 'Arial 10 bold')
janela.config(padx=10, pady=10)

novos_produtos = LabelFrame(janela, text='Entrada de Produto', labelanchor='n')
novos_produtos.grid(row=0, column=0, sticky='ns,we', padx=10, pady=10)

nome = Label(novos_produtos, text='Nome:', anchor='e')
nome.grid(row=0, column=0, sticky='we')
nome_produto = Entry(novos_produtos)
nome_produto.grid(row=0, column=1, sticky='we')

preco = Label(novos_produtos, text='Preço:', anchor='e')
preco.grid(row=1, column=0, sticky='we')
preco_produto = Entry(novos_produtos)
preco_produto.grid(row=1, column=1, sticky='we')

quantidade = Label(novos_produtos, text='Quantidade:', anchor='e')
quantidade.grid(row=2, column=0, sticky='we')
quantidade_produto = Entry(novos_produtos)
quantidade_produto.grid(row=2, column=1, sticky='we')

descricao = Label(novos_produtos, text='Descrição:', anchor='e')
descricao.grid(row=3, column=0, sticky='we')
descricao_produto = Entry(novos_produtos)
descricao_produto.grid(row=3, column=1, sticky='we')

botao_salvar = Button(novos_produtos, text='Salvar', command=salvar)
botao_salvar.grid(row=4, column=0)

mensagem = Label(janela, text='', anchor='center')
mensagem.grid(row=5, column=0, sticky='we', columnspan=2)

lista_produtos = LabelFrame(janela, text='Lista de Produtos', labelanchor='n')
lista_produtos.grid(row=0, column=1, sticky='we', padx=10, pady=10)

produtos_text = Text(lista_produtos)
produtos_text.grid(row=0, column=0, sticky='we')

exibir_produtos()

janela.mainloop()
