import sqlite3
from tkinter import *


def criar_banco():
    # Conectar ao banco de dados
    conexao = sqlite3.connect('exemplo.db')

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Criar tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
        )
    ''')
    # Salvar as alterações
    conexao.commit()

    # fechar a conexão com o banco de dados
    conexao.close()


def ler():
    global lb_saida
    # Conectar ao banco de dados
    conexao = sqlite3.connect('exemplo.db')

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # criar um cursor para executar comandos SQL
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    # Cria o Label onde os dados serão impressos
    lb_saida = Label(quadro_saida, text='Leitura de dados:', justify='left')
    lb_saida.grid(row=3, column=0, columnspan=2)

    for cliente in clientes:
        lb_saida['text'] += '\n' + str(cliente)

    # Fechar a conexão com o banco de dados
    conexao.close()


def salvar():
    # Conectar ao banco de dados
    conexao = sqlite3.connect('exemplo.db')

    # Criar um cursor ppara executar comando SQL
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (in_nome.get(), in_email.get()))

    # Salvar as alterações
    conexao.commit()

    # Fechar a conexão com o banco de dados
    conexao.close()
    ler()


def buscar():
    global lb_saida
    # Conectar ao banco de dados
    conexao = sqlite3.connect('exemplo.db')

    # Criar um cursor ppara executar comando SQL
    cursor = conexao.cursor()

    cursor.execute(f"SELECT * FROM clientes WHERE nome='{in_buscar.get()}'")
    clientes = cursor.fetchall()

    # Cria o Label onde os dados serão impressos
    lb_saida.config(text='Leitura de dados:')

    for cliente in clientes:
        #lb_saida.config(text="f'\n' + {str(cliente)}")
        lb_saida['text'] += '\n' + str(cliente)

    # fecha a conexão com o banco de dados
    conexao.close()


### Inicio da interface grafica ###

janela = Tk()
janela.config(pady=10, padx=10)

quadro_entrada = LabelFrame(janela, text='Dados Pessoais', padx=10, pady=10)
quadro_entrada.grid(row=0, column=0, sticky='we')

quadro_saida = LabelFrame(janela, text='Saida de Dados', pady=10, padx=10)
quadro_saida.grid(row=1, column=0, sticky='we')

lb_nome = Label(quadro_entrada, text='Nome:', anchor='e')
lb_nome.grid(row=0, column=0, sticky='we')

lb_email = Label(quadro_entrada, text='E-mail:', anchor='e')
lb_email.grid(row=1, column=0, sticky='we')

in_nome = Entry(quadro_entrada)
in_nome.grid(row=0, column=1)

in_email = Entry(quadro_entrada)
in_email.grid(row=1, column=1)

bt_salvar = Button(quadro_entrada, text='Salvar', command=salvar)
bt_salvar.grid(row=1, column=3, sticky='we')

lb_buscar = Label(quadro_saida, text='Nome:', anchor='e')
lb_buscar.grid(row=0, column=0, sticky='we')

in_buscar = Entry(quadro_saida)
in_buscar.grid(row=0, column=1, sticky='we')

bt_buscar = Button(quadro_saida, text='Buscar', command=buscar)
bt_buscar.grid(row=0, column=2, sticky='we')

# Chama as Funções Criar_banco e Ler.
criar_banco()
ler()

janela.mainloop()

### Fim da interface grafica ###
