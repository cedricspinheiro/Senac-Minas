
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
            cpf_dados_pessoais TEXT PRIMARY KEY,
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
        INSERT INTO dados_enderecos (cpf_dados_pessoais,rua, numero, bairro, cidade, uf)
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

def lista_cadastros():
    def atualizar_cpf():
        def gravar_alteracao():
            conexao = sqlite3.connect('cadastro_alunos.db')
            cursor = conexao.cursor()
            cursor.execute(f'''
                update dados_pessoais set
                nome = '{enome_up.get()}',
                cpf = '{et_cpf.get()}',
                telefone = '{etelefone_up.get()}',
                data = '{edata_up.get()}'
                where cpf = '{et_cpf.get()}';
            ''')

            cursor1 = conexao.cursor()
            cursor1.execute(f'''
                            update dados_enderecosn set
                            cpf_dados_pessoais = '{et_cpf.get()}'
                            rua = '{erua_up.get()}',
                            numero = '{enumero_up.get()}',
                            bairro = '{ebairro_up.get()}',
                            cidade = '{ecidade_up.get()}',
                            uf = '{euf_up.get()}'
                            where cpf_dados_pessoais = '{et_cpf.get()}';
                            ''')
            conexao.commit()
            conexao.close()

        Janela_atualizar = Tk()
        dados_up = LabelFrame(Janela_atualizar, text='Dados Pessoais', font='Arial 14 italic')
        dados_up.grid(row=0, column=0, sticky='we',padx=10, pady=10)
        dados_up.config(padx=10, pady=10)

        txnome_up = Label(dados_up, text='Nome:', anchor='e')
        txnome_up.grid(row=0, column=0, sticky='we')
        txcpf_up = Label(dados_up, text='CPF:', anchor='e')
        txcpf_up.grid(row=1, column=0, sticky='we')
        txtelefone_up= Label(dados_up, text='Telefone:', anchor='e')
        txtelefone_up.grid(row=1, column=2, sticky='we')
        txdata_up = Label(dados_up, text='Data de Nasc:')
        txdata_up.grid(row=1, column=4, sticky='we')

        enome_up = Entry(dados_up, width=100)
        enome_up.grid(row=0, column=1, columnspan=5)
        ecpf_up = Label(dados_up,text=str(et_cpf.get()), width=25)
        ecpf_up.grid(row=1, column=1)
        etelefone_up = Entry(dados_up, width=25)
        etelefone_up.grid(row=1, column=3)
        edata_up = Entry(dados_up, width=25)
        edata_up.grid(row=1, column=5)

        endereco_up= LabelFrame(Janela_atualizar, text='Endereço', font='Arial 14 italic')
        endereco_up.grid(row=1, column=0, sticky='we', padx=10, pady=10)
        endereco_up.config(pady=10, padx=10)

        txrua_up = Label(endereco_up, text='Rua:', anchor='e')
        txrua_up.grid(row=0, column=0, sticky='we')
        txnumero_up = Label(endereco_up, text='Nº:', anchor='e')
        txnumero_up.grid(row=0, column=4, sticky='we')
        txbairro_up= Label(endereco_up, text='Bairro:', anchor='e')
        txbairro_up.grid(row=1, column=0, sticky='we')
        txcidade_up = Label(endereco_up, text='Cidade:', anchor='e')
        txcidade_up.grid(row=1, column=2, sticky='we')
        txuf_up = Label(endereco_up, text='UF:', anchor='e')
        txuf_up.grid(row=1, column=4, sticky='we')

        erua_up = Entry(endereco_up, width=80)
        erua_up.grid(row=0, column=1, columnspan=3)
        enumero_up = Entry(endereco_up, width=15)
        enumero_up.grid(row=0, column=5)
        ebairro_up = Entry(endereco_up, width=35)
        ebairro_up.grid(row=1, column=1)
        ecidade_up = Entry(endereco_up, width=35)
        ecidade_up.grid(row=1, column=3)
        euf_up = Entry(endereco_up, width=15)
        euf_up.grid(row=1, column=5)

        lf_botao = LabelFrame(Janela_atualizar, padx=10, pady=10)
        lf_botao.grid(row=2, column=0, sticky='e')
        bt_gravar = Button(lf_botao, text='Atualizar', command=gravar_alteracao)
        bt_gravar.grid(row=0, column=1)

        Janela_atualizar.mainloop()
    def deletar_cpf():
        global lb_pessoas
        global lb_enderecos

        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute(f'DELETE FROM dados_pessoais WHERE cpf = "{et_cpf.get()}"')
        cursor2 = conexao.cursor()
        cursor2.execute(f'DELETE FROM dados_enderecos WHERE cpf_dados_pessoais = "{et_cpf.get()}"')
        conexao.commit()
        conexao.close()

        lb_deletado = Label(lf_resultado, text='Dados Deletados', anchor='center')
        lb_deletado.grid(row=0, column=0, columnspan=2, sticky='we')
        lb_pessoas.config(text='(' + str(et_cpf.get()) + ') - Dados DELETATOS', anchor='center')
        lb_enderecos.config(text='(' + str(et_cpf.get()) + ') - Dados DELETATOS', justify='center')

        et_cpf.delete(0, 'end')

    def search():
        global lb_deletado
        global lb_pessoas
        global lb_enderecos

        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor1 = conexao.cursor()
        cursor1.execute(f'select * from dados_pessoais WHERE cpf = "{et_cpf.get()}"')
        dados_pessoas = cursor1.fetchall()
        lb_pessoas = Label(lf_resultado, text='Leitura de Dados', justify='center')
        lb_pessoas.grid(row=1, column=0)
        for dados_pessoa in dados_pessoas:
            lb_pessoas['text'] += '\n' + str(dados_pessoa)

        cursor2 = conexao.cursor()
        cursor2.execute(f'select rua, numero, bairro, cidade, uf from dados_enderecos WHERE cpf_dados_pessoais = "{et_cpf.get()}"')
        dados_enderecos = cursor2.fetchall()
        lb_enderecos = Label(lf_resultado, text='Leitura de Endereços', justify='center')
        lb_enderecos.grid(row=1, column=1)
        for dados_endereco in dados_enderecos:
            lb_enderecos['text'] += '\n' + str(dados_endereco)
        conexao.close()
        lb_deletado.config(text=(''))

    def bc_pessoas():
        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute('select * from dados_pessoais')
        dados_pessoas = cursor.fetchall()

        lb_pessoas = Label(lf_pessoas, text='Leitura de Dados', justify='center')
        lb_pessoas.grid(row=1, column=0)

        for dados_pessoa in dados_pessoas:
            lb_pessoas['text'] += '\n' + str(dados_pessoa)
        conexao.close()

    def bc_endereco():
        conexao = sqlite3.connect('Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute('select rua, numero, bairro, cidade, uf from dados_enderecos')
        dados_enderecos = cursor.fetchall()

        lb_endereco = Label(lf_enderecos, text='Leitura de Endereços', justify='center')
        lb_endereco.grid(row=1, column=0)

        for dados_endereco in dados_enderecos:
            lb_endereco['text'] += '\n' + str(dados_endereco)


    janela_lista = Tk()
    janela_lista.title('Lista de Cadastros')
    janela_lista.configure(padx=10, pady=10)

    lf_busca = LabelFrame(janela_lista, text='Buscar CPF')
    lf_busca.grid(row=0, column=0, columnspan=2)

    lb_cpf = Label(lf_busca, text='CPF:', anchor='e')
    lb_cpf.grid(row=0, column=0, sticky='we', padx=10, pady=10, rowspan=2)
    et_cpf = Entry(lf_busca)
    et_cpf.grid(row=0, column=1, columnspan=2, sticky='we', rowspan=2)
    bt_buscar = Button(lf_busca, text='Buscar', anchor='w', command=search)
    bt_buscar.grid(row=0, column=3, padx=10, pady=10)
    bt_deletar = Button(lf_busca, text='Deletar', anchor='w', command=deletar_cpf)
    bt_deletar.grid(row=0, column=4, padx=10, pady=10)
    bt_atualizar = Button(lf_busca, text='Atualizar', anchor='w', command=atualizar_cpf)
    bt_atualizar.grid(row=0, column=5, padx=10, pady=10)

    lf_lista = LabelFrame(janela_lista, text='Lista de Cadastros')
    lf_lista.grid(row=0, column=0, columnspan=2)

    lf_resultado = LabelFrame(janela_lista, text='Resultado', labelanchor='n')
    lf_resultado.grid(row=1, column=0, columnspan=2, sticky='we')

    lf_pessoas = LabelFrame(janela_lista, text='Cadastros de Pessoas', labelanchor='n')
    lf_pessoas.grid(row=2, column=0)
    bc_pessoas()

    lf_enderecos = LabelFrame(janela_lista, text='Cadastros de Endereços', labelanchor='n')
    lf_enderecos.grid(row=2, column=1)
    bc_endereco()

    janela_lista.mainloop()

janela = Tk()
janela.title('Cadastro')
janela.config(borderwidth=10)
#janela.option_add('*Font', 'Arial 8 bold')

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

cadastros = Button(botoes, text='Cadastros', command=lista_cadastros)
cadastros.grid(row=3, column=1)

sair = Button(botoes, text='Sair', command=janela.quit)
sair.grid(row=3, column=2)

criar_banco()

janela.mainloop()
