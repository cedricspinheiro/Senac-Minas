import sqlite3
from tkinter import *


def criar_banco():
    conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_pessoais (
            nome TEXT,
            cpf TEXT PRIMARY KEY,
            telefone TEXT,
            data TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_enderecos (
            cpf TEXT PRIMARY KEY,
            rua TEXT,
            numero TEXT,
            bairro TEXT,
            cidade TEXT,
            uf TEXT
        )
    ''')

    conexao.commit()
    conexao.close()


def save():
    conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO dados_pessoais (nome, cpf, telefone, data)
        VALUES (?, ?, ?, ?);
    ''', (enome.get(), ecpf.get(), etelefone.get(), edata.get()))

    cursor.execute('''
        INSERT INTO dados_enderecos (cpf, rua, numero, bairro, cidade, uf)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', (ecpf.get(), erua.get(), enumero.get(), ebairro.get(), ecidade.get(), euf.get()))

    conexao.commit()
    conexao.close()
    enome.delete(0, 'end')
    ecpf.delete(0, 'end')
    etelefone.delete(0, 'end')
    edata.delete(0, 'end')
    erua.delete(0, 'end')
    enumero.delete(0, 'end')
    ebairro.delete(0, 'end')
    ecidade.delete(0, 'end')
    euf.delete(0, 'end')


def lista():
    def search():
        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM dados_pessoais where cpf = '{in_buscar.get()}'")
        dados_pessoais = cursor.fetchall()
        saida_pessoa = Label(lf_resultado, text='Dados Pessoais')
        saida_pessoa.grid(row=0, column=0)
        for dados_pessoal in dados_pessoais:
            saida_pessoa['text'] += '\n' + str(dados_pessoal).replace("'", "")
        cursor1 = conexao.cursor()
        cursor1.execute(f"select * from dados_enderecos where cpf = '{in_buscar.get()}'")
        dados_enderecos = cursor1.fetchall()
        saida_endereco = Label(lf_resultado, text='Dados do Endereço')
        saida_endereco.grid(row=0, column=1)
        for dados_endereco in dados_enderecos:
            saida_endereco['text'] += '\n' + str(dados_endereco).replace("'", "")
        conexao.close()

    def pessoal():
        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute('select * from dados_pessoais')
        dados_pessoais = cursor.fetchall()
        lb_saida_pes = Label(lf_pessoal, text='Leitura de Dados:', justify='left')
        lb_saida_pes.grid(row=0, column=0, sticky='we')
        for dados_pessoa in dados_pessoais:
            lb_saida_pes['text'] += '\n' + str(dados_pessoa).replace("'", "")
        conexao.close()

    def enderecos():
        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute('select * from dados_enderecos')
        dados_enderecos = cursor.fetchall()
        lb_saida_end = Label(lf_endereco, text='Leitura de Dados:', justify='left')
        lb_saida_end.grid(row=0, column=0, sticky='we')
        for dados_endereco in dados_enderecos:
            lb_saida_end['text'] += '\n' + str(dados_endereco).replace("'", "")
        conexao.close()

    janela_lista = Tk()
    janela_lista.title('Lista de Cadastros')
    janela_lista.config(pady=10, padx=10)

    lf_buscar = LabelFrame(janela_lista, text='Buscar Cadastro', labelanchor='n')
    lf_buscar.grid(row=0, column=0, columnspan=2)
    lf_buscar.config(padx=10, pady=10)
    lf_resultado = LabelFrame(janela_lista, text='Resultado', labelanchor='n')
    lf_resultado.grid(row=1, column=0, columnspan=2, sticky='we')
    lf_resultado.config(padx=10, pady=10)
    lf_pessoal = LabelFrame(janela_lista, text='Dados Pessoais', labelanchor='n')
    lf_pessoal.grid(row=2, column=0)
    lf_pessoal.config(padx=10, pady=10)
    pessoal()
    lf_endereco = LabelFrame(janela_lista, text='Dados de Endereços', labelanchor='n')
    lf_endereco.grid(row=2, column=1)
    lf_endereco.config(padx=10, pady=10)
    enderecos()
    lb_buscar = Label(lf_buscar, text='CPF:', anchor='e')
    lb_buscar.grid(row=0, column=0, sticky='we')

    in_buscar = Entry(lf_buscar)
    in_buscar.grid(row=0, column=1, sticky='we')

    bt_buscar = Button(lf_buscar, text='Buscar', command=search)
    bt_buscar.grid(row=0, column=2, sticky='we')


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

botoes = LabelFrame(janela)
botoes.grid(row=3, column=0, sticky='we', columnspan=5)
botoes.config(borderwidth=0)

gravar = Button(botoes, text='Gravar Dados', command=save)
gravar.grid(row=3, column=0)

lista = Button(botoes, text='Lista', command=lista)
lista.grid(row=3, column=1)

sair = Button(botoes, text='Sair', command=janela.quit)
sair.grid(row=3, column=2)

criar_banco()

janela.mainloop()
