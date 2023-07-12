import sqlite3
from tkinter import *
from tkinter import messagebox

################################################
root = Tk ()
root.title("Main Window")
root.configure(padx=10, pady=10)
################################################
lf_pessoas = None
lf_enderecos = None
################################################
def BANCO():
    conexao = sqlite3.connect("Senac-Minas\Banco de Dados\Bancos_Dados\Dados pes e end.db")
    cursor = conexao.cursor()
    cursor.execute("""
                create table if not exists Dados_Pessoas(
                Nome text not null,
                CPF text primary key,
                telefone text not null,
                data text not null
            )
    """)
    cursor.execute("""
                create table if not exists Dados_Enderecos(
                    ID interger primary key,
                    CEP text not null,
                    Rua text not null,
                    Numero text not null,
                    Bairro text not null,
                    Cidade text not null,
                    UF text not null,
                    CPF_Pessoas text not null,
                    foreign key (CPF_Pessoas) references Dados_Pessoas(CPF)
            )
    """)
    conexao.commit()
    conexao.close()


def save():
    try:
        conexao = sqlite3.connect("Senac-Minas\Banco de Dados\Bancos_Dados\Dados pes e end.db")
        cursor = conexao.cursor()
        cursor.execute("""
                    insert into Dados_Pessoas(Nome, CPF, telefone, data)
                    values(?,?,?,?)
                """, (enome.get(), ecpf.get(), etelefone.get(), edata.get()))
        cursor.execute('''
                    INSERT INTO Dados_Enderecos (CEP, Rua, Numero, Bairro, Cidade, UF, CPF_Pessoas)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                ''', (ecep.get(), erua.get(), enumero.get(), ebairro.get(), ecidade.get(), euf.get(), ecpf.get()))
        conexao.commit()
        conexao.close()
    except sqlite3.IntegrityError:
        messagebox.showerror("ERRO", "CPF já cadastrado!")
    else:
        messagebox.showinfo("SUCESSO", "CPF cadastrado com sucesso!")
        enome.delete(0, 'end')
        ecpf.delete(0, 'end')
        etelefone.delete(0, 'end')
        edata.delete(0, 'end')
        ecep.delete(0, 'end')
        erua.delete(0, 'end')
        enumero.delete(0, 'end')
        ebairro.delete(0, 'end')
        ecidade.delete(0, 'end')
        euf.delete(0, 'end')
    

def search():
    global lb_enderecosB, lb_pessoasB, lb_deletado
    conexao = sqlite3.connect('Senac-Minas\Banco de Dados\Bancos_Dados\Dados pes e end.db')
    cursor1 = conexao.cursor()
    cursor1.execute(f'select * from dados_pessoais WHERE cpf = "{et_cpf.get()}"')
    dados_pessoas = cursor1.fetchall()
    lb_pessoasB = Label(lf_resultado, text='Leitura de Dados', justify='center')
    lb_pessoasB.grid(row=1, column=0)
    for dados_pessoa in dados_pessoas:
        lb_pessoasB['text'] += '\n' + str(dados_pessoa)
    cursor2 = conexao.cursor()
    cursor2.execute(f'select * from Dados_Enderecos where CPF_Pessoas = "{et_cpf.get()}"')
    dados_enderecos = cursor2.fetchall()
    lb_enderecosB = Label(lf_resultado, text='Leitura de Endereços', justify='center')
    lb_enderecosB.grid(row=1, column=1)
    for dados_endereco in dados_enderecos:
        lb_enderecosB['text'] += '\n' + str(dados_endereco)


def buscar():
    global lb_enderecos, lb_pessoas
    conexao = sqlite3.connect("Senac-Minas\Banco de Dados\Bancos_Dados\Dados pes e end.db")
    cursor1 = conexao.cursor()
    cursor1.execute("select * from Dados_Pessoas")
    dados_pessoas = cursor1.fetchall()
    lb_pessoas = Label(lf_pessoas, text='Leitura de Pessoas', justify='center')
    lb_pessoas.grid(row=1, column=0)
    for dados_pessoa in dados_pessoas:
        lb_pessoas['text'] += '\n' + str(dados_pessoa)
    
    cursor2 = conexao.cursor()
    cursor2.execute("select * from Dados_Enderecos")
    dados_enderecos = cursor2.fetchall()

    lb_enderecos = Label(lf_enderecos, text='Leitura de Endereço', justify='center')
    lb_enderecos.grid(row=1, column=0)

    for enderecos_pessoa in dados_enderecos:
        lb_enderecos['text'] += '\n' + str(enderecos_pessoa)
    conexao.close()

def limpar_janela():
    for widget in root.winfo_children():
        widget.destroy()


def main():
    limpar_janela()
    botoes = LabelFrame(root, text="Escolha uma opção!", labelanchor='n')
    botoes.grid(row=0, column=0, sticky='nswe')
    
    BT_registrar = Button(botoes, text="Registrer", anchor='center', command=registrar)
    BT_registrar.grid(row=0, column=0, sticky='we', padx=10, pady=10)
    BT_consultar = Button(botoes, text="Consultar", anchor='center', command=consultar)
    BT_consultar.grid(row=0, column=1, sticky='we', padx=10, pady=10)
    BT_atualizar = Button(botoes, text="Atualizar", anchor='center', command=atualizar)
    BT_atualizar.grid(row=0, column=2, sticky='we', padx=10, pady=10)


def registrar():
    global  enome, ecpf, etelefone, edata, ecep, erua, enumero, ebairro, ecidade, euf
    root_registrar = Tk()
    root_registrar.title('Cadastro')
    root_registrar.config(borderwidth=10)
    root_registrar.option_add('*Font', 'Arial 8 bold')

    dados = LabelFrame(root_registrar, text='Dados Pessoais', font='Arial 14 italic')
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

    endereco = LabelFrame(root_registrar, text='Endereço', font='Arial 14 italic')
    endereco.grid(row=1, column=0, sticky='we', columnspan=5)
    endereco.config(pady=10, padx=10)

    txcep = Label(endereco, text='CEP:', anchor='e')
    txcep.grid(row=0, column=0)
    ecep = Entry(endereco, width=35)
    ecep.grid(row=0, column=1, sticky='we')
    
    txrua = Label(endereco, text='Rua:', anchor='e')
    txrua.grid(row=0, column=2, sticky='we')
    erua = Entry(endereco, width=40)
    erua.grid(row=0, column=3, columnspan=2)
    
    txnumero = Label(endereco, text='Nº:', anchor='e')
    txnumero.grid(row=0, column=4, sticky='we')
    enumero = Entry(endereco, width=12)
    enumero.grid(row=0, column=5)
    
    txbairro = Label(endereco, text='Bairro:', anchor='e')
    txbairro.grid(row=1, column=0, sticky='we')
    ebairro = Entry(endereco, width=35)
    ebairro.grid(row=1, column=1)
    
    txcidade = Label(endereco, text='Cidade:', anchor='e')
    txcidade.grid(row=1, column=2, sticky='we')
    ecidade = Entry(endereco, width=40)
    ecidade.grid(row=1, column=3)
    
    txuf = Label(endereco, text='UF:', anchor='e')
    txuf.grid(row=1, column=4, sticky='we')
    euf = Entry(endereco, width=12)
    euf.grid(row=1, column=5)

    botoes = LabelFrame(root_registrar)
    botoes.grid(row=3, column=0, sticky='we', columnspan=5)
    botoes.config(borderwidth=0)

    gravar = Button(botoes, text='Gravar Dados', command=save)
    gravar.grid(row=3, column=0)

    cadastros = Button(botoes, text='Consultar', command=consultar)
    cadastros.grid(row=3, column=1)

    sair = Button(botoes, text='Sair', command=root_registrar.quit)
    sair.grid(row=3, column=2)

    root_registrar.mainloop()


def consultar():
    global et_cpf, lf_resultado, lf_pessoas, lf_enderecos
    root_consultar = Tk()
    root_consultar.title('Lista de Cadastros')
    root_consultar.configure(padx=10, pady=10)

    lf_busca = LabelFrame(root_consultar, text='Buscar CPF')
    lf_busca.grid(row=0, column=0, columnspan=2)
    lf_pessoas = LabelFrame(root_consultar, text='Pessoas CPF')
    lf_pessoas.grid(row=1, column=0, padx=10, pady=10)
    lf_enderecos = LabelFrame(root_consultar, text='Endereços')
    lf_enderecos.grid(row=1, column=1, padx=10, pady=10)
    
    lb_cpf = Label(lf_busca, text='CPF:', anchor='e')
    lb_cpf.grid(row=0, column=0, sticky='we', padx=10, pady=10, rowspan=2)
    et_cpf = Entry(lf_busca)
    et_cpf.grid(row=0, column=1, columnspan=2, sticky='we', rowspan=2)
    bt_buscar = Button(lf_busca, text='Buscar', anchor='w', command=search)
    bt_buscar.grid(row=0, column=3, padx=10, pady=10)
    bt_deletar = Button(lf_busca, text='Deletar', anchor='w')
    bt_deletar.grid(row=0, column=4, padx=10, pady=10)
    bt_atualizar = Button(lf_busca, text='Atualizar', anchor='w', command=atualizar)
    bt_atualizar.grid(row=0, column=5, padx=10, pady=10)
    
    lf_lista = LabelFrame(root_consultar, text='Lista de Cadastros')
    lf_lista.grid(row=0, column=0, columnspan=2)
    buscar()
    lf_resultado = LabelFrame(root_consultar, text='Resultado', labelanchor='n')
    lf_resultado.grid(row=1, column=0, columnspan=2, sticky='we')

    lf_pessoas = LabelFrame(root_consultar, text='Cadastros de Pessoas', labelanchor='n')
    lf_pessoas.grid(row=2, column=0)

    lf_enderecos = LabelFrame(root_consultar, text='Cadastros de Endereços', labelanchor='n')
    lf_enderecos.grid(row=2, column=1)
    
    lb_pessoas = Label(lf_pessoas, text='Leitura de Pessoas', justify='center')
    lb_pessoas.grid(row=1, column=0)
    lb_enderecos = Label(lf_enderecos, text='Leitura de Endereço', justify='center')
    lb_enderecos.grid(row=1, column=0)
    root_consultar.mainloop()


def atualizar():
    root_atualizar = Tk()
    dados_up = LabelFrame(root_atualizar, text='Dados Pessoais', font='Arial 14 italic')
    dados_up.grid(row=0, column=0, sticky='we', padx=10, pady=10)
    dados_up.config(padx=10, pady=10)

    txnome_up = Label(dados_up, text='Nome:', anchor='e')
    txnome_up.grid(row=0, column=0, sticky='we')
    txcpf_up = Label(dados_up, text='CPF:', anchor='e')
    txcpf_up.grid(row=1, column=0, sticky='we')
    txtelefone_up = Label(dados_up, text='Telefone:', anchor='e')
    txtelefone_up.grid(row=1, column=2, sticky='we')
    txdata_up = Label(dados_up, text='Data de Nasc:')
    txdata_up.grid(row=1, column=4, sticky='we')

    enome_up = Entry(dados_up, width=100)
    enome_up.grid(row=0, column=1, columnspan=5)
    ecpf_up = Label(dados_up, text=str(et_cpf.get()), width=25)
    ecpf_up.grid(row=1, column=1)
    etelefone_up = Entry(dados_up, width=25)
    etelefone_up.grid(row=1, column=3)
    edata_up = Entry(dados_up, width=25)
    edata_up.grid(row=1, column=5)

    endereco_up = LabelFrame(root_atualizar, text='Endereço', font='Arial 14 italic')
    endereco_up.grid(row=1, column=0, sticky='we', padx=10, pady=10)
    endereco_up.config(pady=10, padx=10)

    txrua_up = Label(endereco_up, text='Rua:', anchor='e')
    txrua_up.grid(row=0, column=0, sticky='we')
    txnumero_up = Label(endereco_up, text='Nº:', anchor='e')
    txnumero_up.grid(row=0, column=4, sticky='we')
    txbairro_up = Label(endereco_up, text='Bairro:', anchor='e')
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

    lf_botao = LabelFrame(root_atualizar, padx=10, pady=10)
    lf_botao.grid(row=2, column=0, sticky='e')
    bt_gravar = Button(lf_botao, text='Atualizar')
    bt_gravar.grid(row=0, column=1)
    
    root_atualizar.mainloop()


buscar()
BANCO()
main()
root.mainloop()