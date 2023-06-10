from tkinter import *
from tkinter.ttk import Combobox

soma_gastos = 0


def selecionar_categoria():
    opcao_selecionada.set(combobox.get())
    print("Opção selecionada:", opcao_selecionada.get())


def salvar():
    global soma_gastos
    valor = float(entrada_valor.get())
    soma_gastos += valor
    total_soma_gastos.config(text=str(soma_gastos))
    with open('Despesas.txt', 'a') as arquivo:
        arquivo.write(
            f'Categoria: {opcao_selecionada.get()}, Valor: {valor}, Data: {entrada_data.get()}, Descrição: {entrada_descricao.get()}\n')
    exibir_gastos()
    entrada_valor.delete(0, END)
    entrada_data.delete(0, END)
    entrada_descricao.delete(0, END)
    combobox.delete(0, END)


def exibir_gastos():
    gastos_text.delete('1.0', END)
    with open('Despesas.txt', 'r') as arquivo:
        for linha in arquivo:
            gastos_text.insert(END, linha)


def calcular():
    entrada_dinheiro = float(entrada_dinheiro_entry.get())
    total = entrada_dinheiro - soma_gastos
    total_soma.config(text=str(total))


def limpar_arquivo():
    with open('Despesas.txt', 'w') as arquivo:
        arquivo.truncate(0)
    exibir_gastos()


janela = Tk()
janela.title("Gerenciador de despesas")
janela.config(padx=10, pady=10)

gastos = LabelFrame(janela, text='Gastos e Recebimentos', labelanchor='n')
gastos.grid(row=0, column=0, padx=10, pady=10)

gastos_text = Text(gastos)
gastos_text.grid(row=0, column=0, sticky='we')

entrada_gastos = LabelFrame(janela, text='Entrada de Gastos e Recebimentos', labelanchor='n')
entrada_gastos.grid(row=1, column=0, padx=10, pady=10, sticky='we')

categorias = ["Alimentação", "Transporte", "Moradia", "Saúde", "Educação", "Lazer"]
opcao_selecionada = StringVar()
combobox = Combobox(entrada_gastos, values=categorias, textvariable=opcao_selecionada)
combobox.grid(row=0, column=0)

botao = Button(entrada_gastos, text="Selecionar", command=selecionar_categoria)
botao.grid(row=1, column=0)

valor = Label(entrada_gastos, text='Valor', anchor='e')
valor.grid(row=0, column=1, sticky='e')
entrada_valor = Entry(entrada_gastos)
entrada_valor.grid(row=0, column=2)
entrada_valor.insert(END, '0.00')
entrada_valor.focus()

data = Label(entrada_gastos, text='Data', anchor='e')
data.grid(row=1, column=1, sticky='e')
entrada_data = Entry(entrada_gastos)
entrada_data.grid(row=1, column=2)
entrada_data.insert(END, 'dd/mm/aaaa')

descricao = Label(entrada_gastos, text='Descrição', anchor='e')
descricao.grid(row=2, column=1, sticky='e')
entrada_descricao = Entry(entrada_gastos)
entrada_descricao.grid(row=2, column=2)

incluir = Button(entrada_gastos, text='Salvar', command=salvar)
incluir.grid(row=1, column=3)

saida = LabelFrame(janela, text='Dados da Despesa')
saida.grid(row=0, column=1, padx=10, pady=10, sticky='ns')

entrada_texto = Label(saida, text='ENTRE COM O VALOR DO SALARIO')
entrada_texto.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
entrada_dinheiro_label = Label(saida, text='ENTRADA: R$', anchor='e')
entrada_dinheiro_label.grid(row=1, column=0, sticky='we')
entrada_dinheiro_entry = Entry(saida)
entrada_dinheiro_entry.grid(row=1, column=1, sticky='we')
entrada_dinheiro_entry.insert(END, '0.00')
entrada_dinheiro_entry.focus()

total_gastos = Label(saida, text='Gastos: R$', anchor='e')
total_gastos.grid(row=2, column=0, sticky='we')
total_soma_gastos = Label(saida, text='', foreground='red')
total_soma_gastos.grid(row=2, column=1)

total_soma = Label(saida, text='')
total_soma.grid(row=3, columnspan=2, sticky='we')

botao_calcular = Button(saida, text='Calcular', command=calcular)
botao_calcular.grid(row=4, column=0, columnspan=2)

botao_limpar = Button(saida, text='Limpar', command=limpar_arquivo)
botao_limpar.grid(row=5, column=0, columnspan=2)

logo = Label(janela,text='KKNeko Game House', font='Arial 16 bold')
logo.grid(row=1, column=1, sticky='ns,we')

exibir_gastos()

janela.mainloop()
