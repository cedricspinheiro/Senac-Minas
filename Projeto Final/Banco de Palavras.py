import sqlite3
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Toplevel, Label, Button
from tkinter import messagebox



cadastro = Tk() 
cadastro.title("Cadastro de Palavras")
cadastro.geometry("900x750")


def BANCO_PALAVRAS():
    conexao = sqlite3.connect('Senac-Minas\Projeto Final\Banco\Banco_de_Palavras.db')
    cursor = conexao.cursor()
    cursor.execute("""
                   create table if not exists Palavras (
                       Palavra text primary key not null,
                       Dica text not null,
                       Autor text not null
                   )
                   """)
    conexao.close()
BANCO_PALAVRAS()


def salvar_conteudo():
    global txt_cadastro_palavras, txt_cadastro_dica, txt_cadastro_autor
    txt_cadastro_palavras = en_cadastro_palavras.get().upper()
    txt_cadastro_dica = en_cadastro_dica.get().upper()
    txt_cadastro_autor = en_cadastro_autor.get()
    
    if txt_cadastro_autor == "":
        txt_cadastro_autor = "Autor Anônimo"
    
    conexao = sqlite3.connect('Senac-Minas/Projeto Final/Banco/Banco_de_Palavras.db')
    cursor = conexao.cursor()
    cursor.execute("""
                   INSERT INTO Palavras (Palavra, Dica, Autor)
                   VALUES (?, ?, ?);
                   """, (txt_cadastro_palavras, txt_cadastro_dica, txt_cadastro_autor))
    conexao.commit()
    conexao.close()
    
    en_cadastro_palavras.delete(0, END)
    en_cadastro_dica.delete(0, END)
    en_cadastro_autor.delete(0, END)
    
    exibir_conteudo()
    print("Conteúdo salvo com sucesso!")


def limpar_janela():
    for widget in cadastro.winfo_children():
        widget.destroy()
        

def cadastro_palavras():
    global lf_tela_toda, im_cadastro, ft_cadastro, lb_im_foto, lf_BANCO, en_cadastro_palavras, en_cadastro_dica, en_cadastro_autor, lf_resumo
    
    lf_tela_toda = LabelFrame(cadastro)
    lf_tela_toda.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_cadastro_palavras = LabelFrame(lf_tela_toda, text='Cadastre uma palavra e descrição!', labelanchor='n', font=("Arial", 12, "bold"))
    lf_cadastro_palavras.grid(row=0, rowspan=2, column=0, sticky='nswe', padx=10, pady=10)
    lf_pesquisa = LabelFrame(lf_tela_toda, text='Consulta', labelanchor='n', font=("Arial", 12, "bold"))
    lf_pesquisa.grid(row=0, column=1, sticky='we', padx=10, pady=10)
    lf_resumo = LabelFrame(lf_tela_toda, text='Resumo', labelanchor='n', font=("Arial", 12, "bold"))
    lf_resumo.grid(row=0, column=2, sticky='nswe', padx=10, pady=10)
    lf_BANCO = LabelFrame(lf_tela_toda, text='Banco de Palavras e suas Descrições!', labelanchor='n', font=("Arial", 12, "bold"))
    lf_BANCO.grid(row=1,rowspan=3, column=1, sticky='nswe', padx=10, pady=10)
    lf_im_BANCO = LabelFrame(lf_tela_toda, text='Porque está tão sério?', labelanchor='n', font=("Arial", 12, "bold"))
    lf_im_BANCO.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)

    lb_cadastro_palavras = Label(lf_cadastro_palavras, text='Digite uma palavra:', anchor=CENTER, font=("Arial", 12, "bold"))
    lb_cadastro_palavras.grid(row=0,column=0, sticky='we')
    en_cadastro_palavras = Entry(lf_cadastro_palavras)
    en_cadastro_palavras.grid(row=0, column=1, sticky='we', padx=10, pady=10)
    lb_cadastro_dica = Label(lf_cadastro_palavras, text='Dica:', anchor=CENTER, font=("Arial", 12, "bold"))
    lb_cadastro_dica.grid(row=1, column=0, sticky='we', padx=10, pady=10)
    en_cadastro_dica = Entry(lf_cadastro_palavras)
    en_cadastro_dica.grid(row=1, column=1, sticky='we', padx=10, pady=10)
    lb_cadastro_autor = Label(lf_cadastro_palavras, text='Autor:', anchor=CENTER, font=("Arial", 12, "bold"))
    lb_cadastro_autor.grid(row=2, column=0, sticky='we', padx=10, pady=10)
    en_cadastro_autor = Entry(lf_cadastro_palavras)
    en_cadastro_autor.grid(row=2, column=1, sticky='we', padx=10, pady=10)

    bt_cadastro_conteudo = Button(lf_cadastro_palavras, text='Cadastrar', command=salvar_conteudo)
    bt_cadastro_conteudo.grid(row=3, column=1, sticky='we', padx=10, pady=10)

    lb_pesquisa = Label(lf_pesquisa, text='Pesquisa:', anchor='e', font=("Arial", 12, "bold"))
    lb_pesquisa.grid(row=0, column=0, sticky='we') 
    en_pesquisa = Entry(lf_pesquisa)
    en_pesquisa.grid(row=0, column=1, sticky='we')
    bt_pesquisa = tk.Button(lf_pesquisa, text='Pesquisar', command=lambda: atualizar_conteudo(en_pesquisa))
    bt_pesquisa.grid(row=0, column=2, sticky='we')   
    
    im_cadastro = Image.open("Senac-Minas\Projeto Final\Imagens\End.jpg").resize((241, 360))
    ft_cadastro = ImageTk.PhotoImage(im_cadastro)
    lb_im_foto = Label(lf_im_BANCO, image=ft_cadastro)
    lb_im_foto.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
cadastro_palavras()


def exibir_conteudo():
    global lb_dicas_salvas, lb_Palavras_salvas, lb_autor_salvas
    conexao = sqlite3.connect("Senac-Minas\Projeto Final/Banco/Banco_de_Palavras.db")
    
    cursor1 = conexao.cursor()
    cursor1.execute("SELECT palavra FROM Palavras ORDER BY rowid")
    lb_Palavras_salvas = Label(lf_BANCO, text='Palavras', justify='center')
    lb_Palavras_salvas.grid(row=0, column=0, sticky='we')
    palavras_salvas = cursor1.fetchall() 
    for palavras in palavras_salvas:
        lb_Palavras_salvas['text'] += '\n' + str(palavras).replace("'", "")   

    cursor2 = conexao.cursor()
    cursor2.execute("SELECT Dica FROM Palavras ORDER BY rowid")
    lb_dicas_salvas = Label(lf_BANCO, text='Dicas', justify='center')
    lb_dicas_salvas.grid(row=0, column=1, sticky='we')    
    dicas_salvas = cursor2.fetchall()
    for dicas in dicas_salvas:
        lb_dicas_salvas['text'] += '\n' + str(dicas).replace("'", "")

    cursor3 = conexao.cursor()
    cursor3.execute("SELECT Autor FROM Palavras ORDER BY rowid")
    lb_autor_salvas = Label(lf_BANCO, text='Autores', justify='center')
    lb_autor_salvas.grid(row=0, column=2, sticky='we')
    autores_salvos = cursor3.fetchall()
    for autor in autores_salvos:
        lb_autor_salvas['text'] += '\n' + str(autor).replace("'", "")

    conexao.close()
exibir_conteudo()


def atualizar_conteudo(en_pesquisa):
    palavra_pesquisada = en_pesquisa.get().upper()
    conexao = sqlite3.connect("Senac-Minas\Projeto Final\Banco\Banco_de_Palavras.db")
    cursor = conexao.cursor()
    cursor.execute(f"SELECT Palavra, Dica, Autor FROM Palavras WHERE Palavra = '{palavra_pesquisada}'")
    resultado = cursor.fetchone()
    if resultado:
        palavra, dica, autor = resultado
        conexao.close()
        atualizacao = tk.Toplevel()
        atualizacao.title("Atualizar Conteúdo")
        atualizacao.geometry("300x300")
        atualizacao.grab_set()
        atualizacao.transient(cadastro)

        nova_palavra = tk.StringVar(value=palavra)
        nova_dica = tk.StringVar(value=dica)
        novo_autor = tk.StringVar(value=autor)

        def salvar_edicao():
            nova_palavra_valor = nova_palavra.get().upper()
            nova_dica_valor = nova_dica.get().upper()
            novo_autor_valor = novo_autor.get()

            atualizacao.destroy()

            conexao = sqlite3.connect("Senac-Minas\Projeto Final\Banco\Banco_de_Palavras.db")
            cursor = conexao.cursor()
            cursor.execute(f"""
                UPDATE Palavras
                SET Palavra = '{nova_palavra_valor}',
                    Dica = '{nova_dica_valor}',
                    Autor = '{novo_autor_valor}'
                WHERE Palavra = '{palavra}'
            """)
            conexao.commit()
            conexao.close()
            atualizacao.destroy()
            en_pesquisa.delete(0, END)
            exibir_conteudo.destroy()
            exibir_conteudo()


        
        def deletar_edicao():
            conexao = sqlite3.connect("Senac-Minas\Projeto Final\Banco\Banco_de_Palavras.db")
            cursor = conexao.cursor()
            cursor.execute(f"""
                           DELETE FROM Palavras
                           where Palavra = '{palavra}'
                           """)
            conexao.commit()
            conexao.close()
            atualizacao.destroy()
            en_pesquisa.delete(0, END)
            exibir_conteudo.destroy()
            exibir_conteudo()



        
    elif resultado == None:
        messagebox.showinfo("Caixa de Pesquisa Vazia", "Por favor, digite a palavra desejada.")
        exibir_conteudo.destroy()
        exibir_conteudo()

    else:
        messagebox.showinfo("Palavra não encontrada", "A palavra não foi encontrada no banco de palavras.")
        exibir_conteudo.destroy()
        exibir_conteudo()
    lb_palavra = tk.Label(atualizacao, text="Palavra:")
    lb_palavra.pack()
    en_palavra = tk.Entry(atualizacao, textvariable=nova_palavra)
    en_palavra.pack()

    lb_dica = tk.Label(atualizacao, text="Dica:")
    lb_dica.pack()
    en_dica = tk.Entry(atualizacao, textvariable=nova_dica)
    en_dica.pack()

    lb_autor = tk.Label(atualizacao, text="Autor:")
    lb_autor.pack()
    en_autor = tk.Entry(atualizacao, textvariable=novo_autor)
    en_autor.pack()

    bt_salvar = tk.Button(atualizacao, text="Salvar", command=salvar_edicao)
    bt_salvar.pack()
    bt_deletar = tk.Button(atualizacao, text="Deletar", command=deletar_edicao)
    bt_deletar.pack()
    


cadastro.mainloop()