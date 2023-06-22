import sqlite3
from tkinter import *

def criar_banco():
    conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_pessoais (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            data TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_enderecos (
            id INTEGER PRIMARY KEY,
            rua TEXT,
            numero TEXT,
            bairro TEXT,
            cidade TEXT,
            uf TEXT
        )
    ''')

    conexao.commit()
    conexao.close()


def ler():
    global lb_saida
    conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM dados_pessoais, dados_enderecos')
    dados_cadastrais = cursor.fetchall()

    lb_saida = Label(quadro_saida, text='Leitura de dados:', justify='left')
    lb_saida.grid(row=3, column=0, columnspan=2)
    print(dados_cadastrais)
    for dados_pessoal in dados_cadastrais:
        lb_saida['text'] += '\n' + str(dados_pessoal)
    conexao.close()


def save():
    conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO dados_pessoais (nome, cpf, telefone, data)
        VALUES (?, ?, ?, ?);
    ''', (enome.get(), ecpf.get(), etelefone.get(), edata.get()))

    cursor.execute('''
        INSERT INTO dados_enderecos (rua, numero, bairro, cidade, uf)
        VALUES (?, ?, ?, ?, ?);
    ''', (erua.get(), enumero.get(), ebairro.get(), ecidade.get(), euf.get()))

    conexao.commit()
    conexao.close()
    ler()
    enome.delete(0, 'end')
    ecpf.delete(0, 'end')
    etelefone.delete(0, 'end')
    edata.delete(0, 'end')
    erua.delete(0, 'end')
    enumero.delete(0, 'end')
    ebairro.delete(0, 'end')
    ecidade.delete(0, 'end')
    euf.delete(0, 'end')



def search():
    global lb_saida
    conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM dados_pessoais WHERE nome = '{in_buscar.get()}'")
    dados_cadastrais = cursor.fetchall()
    lb_saida = Label(quadro_saida, text='Leitura de dados', justify='left')
    lb_saida.grid(row=1, column=0, columnspan=2)
    for dados_pessoal in dados_cadastrais:
        lb_saida['text'] += '\n' + str(dados_pessoal)
    conexao.close()


janela = Tk()
janela.title('Cadastro')
janela.config(borderwidth=10)
janela.option_add('*Font', 'Arial 8 bold')

dados = LabelFrame(janela, text='Dados Pessoais', font='Arial 14 italic')
dados.grid(row=0, column=0, sticky='we', columnspan=5)
dados.config(padx=10, pady=10)

txnome = Label(dados, text='Nome:', anchor='e')
txnome.grid(row=0, column=0, sticky='we')
txcpf = Label(dados, text='CPF:', anchor='e')
txcpf.grid(row=1, column=0, sticky='we')
txtelefone = Label(dados, text='Telefone:', anchor='e')
txtelefone.grid(row=1, column=2, sticky='we')
txdata = Label(dados, text='Data de Nasc:')
txdata.grid(row=1, column=4, sticky='we')

enome = Entry(dados, width=100)
enome.grid(row=0, column=1, columnspan=5)
ecpf = Entry(dados, width=25)
ecpf.grid(row=1, column=1)
etelefone = Entry(dados, width=25)
etelefone.grid(row=1, column=3)
edata = Entry(dados, width=25)
edata.grid(row=1, column=5)

endereco = LabelFrame(janela, text='Endereço', font='Arial 14 italic')
endereco.grid(row=1, column=0, sticky='we', columnspan=5)
endereco.config(pady=10, padx=10)

txrua = Label(endereco, text='Rua:', anchor='e')
txrua.grid(row=0, column=0, sticky='we')
txnumero = Label(endereco, text='Nº:', anchor='e')
txnumero.grid(row=0, column=4, sticky='we')
txbairro = Label(endereco, text='Bairro:', anchor='e')
txbairro.grid(row=1, column=0, sticky='we')
txcidade = Label(endereco, text='Cidade:', anchor='e')
txcidade.grid(row=1, column=2, sticky='we')
txuf = Label(endereco, text='UF:', anchor='e')
txuf.grid(row=1, column=4, sticky='we')

erua = Entry(endereco, width=80)
erua.grid(row=0, column=1, columnspan=3)
enumero = Entry(endereco, width=15)
enumero.grid(row=0, column=5)
ebairro = Entry(endereco, width=35)
ebairro.grid(row=1, column=1)
ecidade = Entry(endereco, width=35)
ecidade.grid(row=1, column=3)
euf = Entry(endereco, width=15)
euf.grid(row=1, column=5)

quadro_saida = LabelFrame(janela, text='Dados Cadastrais', padx=10, pady=10, font='Arial 14 italic')
quadro_saida.grid(row=2, column=0, sticky='we')

lb_buscar = Label(quadro_saida, text='Nome:', anchor='e')
lb_buscar.grid(row=0, column=0, sticky='we')

in_buscar = Entry(quadro_saida)
in_buscar.grid(row=0, column=1, sticky='we')

bt_buscar = Button(quadro_saida, text='Buscar', command=search)
bt_buscar.grid(row=0, column=2, sticky='we')

botoes = LabelFrame(janela)
botoes.grid(row=3, column=0, sticky='we', columnspan=5)
botoes.config(borderwidth=0)

gravar = Button(botoes, text='Gravar Dados', command=save)
gravar.grid(row=3, column=0)

sair = Button(botoes, text='Sair', command=janela.quit)
sair.grid(row=3, column=1)

criar_banco()
ler()

janela.mainloop()
