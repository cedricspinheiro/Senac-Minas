from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import random
import tkinter as tk
from tkinter import Tk, Toplevel, Label, Button
from tkinter import messagebox
import tkinter.messagebox as messagebox
import logging

# Configuração do módulo de logging
logging.basicConfig(filename='Log/error.log', level=logging.ERROR)

### VARIAVES ###
PONTOS = 0
ERROS = 0
row = 1
col_name = 1
col_points = 2
lb_segredo = None  # Variável global para armazenar o widget Label lb_segredo
### FIM DAS VARIAVEIS ###

### TELA E TAMANHO DEFINIDA ###
menu_game = Tk()
menu_game.title("Jogo da Forca")
menu_game.geometry("750x750")
menu_game.resizable(False, False)


# Função para registrar logs de erro
def log_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Erro na função {func.__name__}: {str(e)}')
    return wrapper


### NÃO MEXER AQUI ###

@log_error
def BANCO():
    conexao = sqlite3.connect('Banco\\Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute("""
            create table if not exists Pontuação (
                id integer primary key autoincrement,
                nome text,
                pontos integer
            )
            """)
    cursorP = conexao.cursor()
    cursorP.execute("""
                   create table if not exists Palavras (
                       Palavra text primary key not null,
                       Dica text not null,
                       Autor text not null
                   )
                   """)
    conexao.close()


@log_error
def salvar_conteudo():
    global txt_cadastro_palavras, txt_cadastro_dica, txt_cadastro_autor
    txt_cadastro_palavras = en_cadastro_palavras.get().upper()
    txt_cadastro_dica = en_cadastro_dica.get().upper()
    txt_cadastro_autor = en_cadastro_autor.get()

    if txt_cadastro_autor == "":
        txt_cadastro_autor = "Autor Anônimo"

    conexao = sqlite3.connect('Banco/Banco_de_Dados.db')
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


@log_error
def limpar_janela():
    for widget in menu_game.winfo_children():
        widget.destroy()


@log_error
def atualizar_conteudo(en_pesquisa):
    palavra_pesquisada = en_pesquisa.get().upper()
    conexao = sqlite3.connect("Banco\Banco_de_Dados.db")
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
        atualizacao.transient(menu_game)

        nova_palavra = tk.StringVar(value=palavra)
        nova_dica = tk.StringVar(value=dica)
        novo_autor = tk.StringVar(value=autor)

        @log_error
        def salvar_edicao():
            nova_palavra_valor = nova_palavra.get().upper()
            nova_dica_valor = nova_dica.get().upper()
            novo_autor_valor = novo_autor.get()

            atualizacao.destroy()

            conexao = sqlite3.connect("Banco\Banco_de_Dados.db")
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

        @log_error
        def deletar_edicao():
            conexao = sqlite3.connect("Banco\Banco_de_Dados.db")
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


@log_error
def cadastro_palavras():
    global lf_tela_toda, im_cadastro, ft_cadastro, lb_im_foto, lf_BANCO, en_cadastro_palavras, en_cadastro_dica, en_cadastro_autor, lf_resumo
    limpar_janela()
    lf_tela_toda = LabelFrame(menu_game)
    lf_tela_toda.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_cadastro_palavras = LabelFrame(lf_tela_toda, text='Cadastre uma palavra e descrição!', labelanchor='n',
                                      font=("Arial", 12, "bold"))
    lf_cadastro_palavras.grid(row=0, rowspan=2, column=0, sticky='nswe', padx=10, pady=10)
    lf_pesquisa = LabelFrame(lf_tela_toda, text='Consulta', labelanchor='n', font=("Arial", 12, "bold"))
    lf_pesquisa.grid(row=0, column=1, sticky='we', padx=10, pady=10)

    lf_BANCO = LabelFrame(lf_tela_toda, text='Banco de Palavras e suas Descrições!', labelanchor='n',
                          font=("Arial", 12, "bold"))
    lf_BANCO.grid(row=1, rowspan=2, column=1, sticky='nswe', padx=10, pady=10)
    lf_im_BANCO = LabelFrame(lf_tela_toda, text='Porque está tão sério?', labelanchor='n', font=("Arial", 12, "bold"))
    lf_im_BANCO.grid(row=2, rowspan=2, column=0, sticky='nswe', padx=10, pady=10)
    bt_voltar = Button(lf_tela_toda, text='Voltar', command=menu)
    bt_voltar.grid(row=3, column=1, padx=10, pady=10)
    lb_cadastro_palavras = Label(lf_cadastro_palavras, text='Digite uma palavra:', anchor=CENTER,
                                 font=("Arial", 12, "bold"))
    lb_cadastro_palavras.grid(row=0, column=0, sticky='we')
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

    im_cadastro = Image.open("Imagens\End.jpg").resize((241, 360))
    ft_cadastro = ImageTk.PhotoImage(im_cadastro)
    lb_im_foto = Label(lf_im_BANCO, image=ft_cadastro)
    lb_im_foto.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
    exibir_conteudo()


@log_error
def exibir_conteudo():
    global lb_dicas_salvas, lb_Palavras_salvas, lb_autor_salvas, lf_BANCO
    conexao = sqlite3.connect("Banco/Banco_de_Dados.db")

    cursor1 = conexao.cursor()
    cursor1.execute("SELECT palavra FROM Palavras ORDER BY rowid")
    lb_Palavras_salvas = Label(lf_BANCO, text='Palavras', justify='center')
    lb_Palavras_salvas.grid(row=0, column=0, sticky='we')
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


@log_error
def exibir_rank():
    global lb_nome, lb_pontos

    conexao = sqlite3.connect('Banco\Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute("""
            select * from Pontuação
            order by pontos desc
            """)
    resultado = cursor.fetchall()
    conexao.close()

    resultado_classificado = sorted(resultado, key=lambda x: x[2], reverse=True)

    row = 1

    for posicao in resultado_classificado[:20]:
        nome = posicao[1]
        pontos = posicao[2]

        lb_nome = Label(lf_rank, text=nome, anchor='center')
        lb_nome.grid(row=row, column=1, padx=10, pady=2.5)

        lb_pontos = Label(lf_rank, text=pontos, anchor='center')
        lb_pontos.grid(row=row, column=2, padx=10, pady=2.5)

        row += 1


@log_error
def zerar_rank():
    conexao = sqlite3.connect('Banco\Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute('drop table Pontuação')
    conexao.commit()
    conexao.close()
    messagebox.showinfo('Rank Zerado', 'O ranking foi zerado com sucesso!')


@log_error
def menu():
    limpar_janela()
    global ft_menu_game, ERROS
    ERROS = 0
    im_menu_game = Image.open("Imagens\Menu Game.jpg")
    ft_menu_game = ImageTk.PhotoImage(im_menu_game)

    lf_menu_game = LabelFrame(menu_game, text='Você está REALMENTE pronto?', labelanchor='n', font=("Arial", 9, "bold"))
    lf_menu_game.place(relx=0.5, rely=0.5, anchor=CENTER)

    lb_menu_game = Label(lf_menu_game, image=ft_menu_game)
    lb_menu_game.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    bt_new_game = Button(lf_menu_game, text='New Game', anchor='center', command=tela_nick)
    bt_new_game.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
    bt_new_game.configure(background="black", foreground="white", activebackground="white", activeforeground="black")

    bt_zerar_rank = Button(lf_menu_game, text='clear game', anchor='center', command=zerar_rank)
    bt_zerar_rank.grid(row=1, column=1, padx=10, pady=10, sticky='nswe')

    bt_cadastro = Button(menu_game, text='Cadastrar palavra', anchor='center', command=cadastro_palavras)
    bt_cadastro.grid(row=0, column=0, padx=10, pady=10)
    bt_teste = Button(menu_game, text="Testar LFrames", anchor='center', command=test_do_testando)
    bt_teste.grid(row=1, column=0, padx=10, pady=10)

    lf_top3 = LabelFrame(menu_game, text="Top 3 Rank", labelanchor='n', font=("Arial", 9, "bold"))
    lf_top3.place(relx=0.35, rely=0.7)

    conexao = sqlite3.connect('Banco\Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute("""
            select * from Pontuação
            order by pontos desc
            """)
    resultado = cursor.fetchall()
    conexao.close()

    resultado_classificado = sorted(resultado, key=lambda x: x[2], reverse=True)

    column = 1

    for posicao in resultado_classificado[:3]:
        nome = posicao[1]
        pontos = posicao[2]

        lb_nome = Label(lf_top3, text=nome, anchor='center')
        lb_nome.grid(row=1, column=column, padx=10, pady=2.5)

        lb_pontos = Label(lf_top3, text=pontos, anchor='center')
        lb_pontos.grid(row=2, column=column, padx=10, pady=2.5)

        column += 1


@log_error
def tela_nick():
    global en_nick
    limpar_janela()
    lf_tela_nick = LabelFrame(menu_game, text='Aqui você DIGITA o seu nick de preferencia!', labelanchor='n',
                              font=("Arial", 9, "bold"))
    lf_tela_nick.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_tela_nick.configure(padx=10, pady=10)

    lb_tela_nick = Label(lf_tela_nick, image=ft_menu_game)
    lb_tela_nick.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

    lb_nick = Label(lf_tela_nick, text="Digite seu NICK:", anchor='e')
    lb_nick.grid(row=1, column=0, sticky='we')
    en_nick = Entry(lf_tela_nick)
    en_nick.grid(row=1, column=1)
    en_nick.bind("<Return>", lambda event: tela_forca(en_nick.get()))
    bt_nick = Button(lf_tela_nick, text="AVANÇAR", anchor="center", command=lambda: tela_forca(en_nick.get()))
    bt_nick.grid(row=1, column=2)
    bt_nick.configure(background="black", foreground="white", activebackground="white", activeforeground="black")


@log_error
def verificar():
    global texto_oculto, PONTOS, pontos_value, ERROS

    letra = en_entrada_letra.get().upper()
    nova_palavra = ""

    # Verificar se a variável PONTOS já foi definida globalmente
    if 'PONTOS' not in globals():
        PONTOS = 0

    for i in range(len(texto_original)):
        if texto_original == nova_palavra:
            PONTOS += 100
        elif texto_original[i] == letra:
            nova_palavra += letra
            PONTOS += 10
        else:
            nova_palavra += texto_oculto[i]

    if texto_original == nova_palavra:
        PONTOS += 100
        pontos_value.set(str(PONTOS))  # Atualizar a pontuação na interface gráfica
        tela_win()  # Chamar a função win_game se todas as letras foram acertadas

    texto_oculto = nova_palavra
    lb_segredo.config(text=texto_oculto)
    en_entrada_letra.delete(0, END)

    # Incrementar a variável ERROS se a letra não estiver na palavra
    if letra not in texto_original:
        ERROS += 1
        lb_letras_erradas.config(text=lb_letras_erradas.cget('text') + letra + '\n')

    # Verificar se o número de erros é igual a 7
    if ERROS == 7:
        end_game()

@log_error
def palavra_secreta():
    global texto_oculto, texto_original, dica_palavra

    conexao = sqlite3.connect('Banco/Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT Palavra, Dica FROM Palavras")
    palavras = cursor.fetchall()

    # Selecionar uma palavra aleatória
    palavra, dica = random.choice(palavras)

    # Verificar se a palavra contém espaços ou hífens
    if ' ' in palavra:
        texto_original = palavra
    else:
        texto_original = palavra.upper()
        palavra = ''.join(['*' if c != '-' else '-' for c in texto_original])

    dica_palavra = dica

    conexao.close()

    texto_oculto = palavra

palavra_secreta()

pontos_value = StringVar()
pontos_value.set(str(PONTOS))
nick_value = StringVar()


@log_error
def tela_forca(nick):
    global im_forca, lf_tela_toda, ft_forca, lb_forca, nick_value, lf_rank, en_entrada_letra, lb_segredo, pontos_value, texto_oculto, lb_letras_erradas
    nick_value.set(nick)

    pontos_value = StringVar()
    pontos_value.set(str(PONTOS))

    limpar_janela()

    lf_tela_toda = LabelFrame(menu_game)
    lf_tela_toda.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_pontuacao = LabelFrame(lf_tela_toda, text='Pontuação', labelanchor='n', font=("Arial", 9, "bold"))
    lf_pontuacao.grid(row=0, column=0, columnspan=3, sticky='nswe')
    lf_im_forca = LabelFrame(lf_tela_toda, text='Pegue o Fredd!', labelanchor='n', font=("Arial", 9, "bold"))
    lf_im_forca.grid(row=1, column=0, sticky='nswe')
    lf_letra_errada = LabelFrame(lf_tela_toda, text='7 Tentativas', labelanchor='n', font=("Arial", 9, "bold"))
    lf_letra_errada.grid(row=1, column=1, sticky='nswe')
    lf_rank = LabelFrame(lf_tela_toda, text='Top Rank', labelanchor='n', font=("Arial", 9, "bold"))
    lf_rank.grid(row=1, column=2, rowspan=3, sticky='nswe', padx=10, pady=10)
    exibir_rank()
    lf_palavra_secreta = LabelFrame(lf_tela_toda, text='Adivinhe qual é a Palavra Secreta!', font=("Arial", 9, "bold"))
    lf_palavra_secreta.grid(row=2, column=0, columnspan=2, sticky='nswe')
    lf_entrada_letra = LabelFrame(lf_tela_toda, text='Entre com UMA LETRA ou com a PALAVRA SECRETA', labelanchor='n',
                                  font=("Arial", 9, "bold"))
    lf_entrada_letra.grid(row=3, column=0, columnspan=2, sticky='nswe')

    lf_pontuacao.grid_columnconfigure(0, weight=1)
    lf_pontuacao.grid_columnconfigure(1, weight=1)
    lf_pontuacao.grid_columnconfigure(2, weight=1)
    lf_pontuacao.grid_columnconfigure(3, weight=1)

    lb_nick = Label(lf_pontuacao, text='Nick:', anchor='center')
    lb_nick.grid(row=0, column=0, sticky='we')
    nick = Label(lf_pontuacao, textvariable=nick_value, anchor='center')
    nick.grid(row=0, column=1, sticky='we')
    lb_pontuacao = Label(lf_pontuacao, text="Pontuação:", anchor='center')
    lb_pontuacao.grid(row=0, column=2, sticky='we')
    lb_pontos = Label(lf_pontuacao, textvariable=pontos_value, anchor='center')
    lb_pontos.grid(row=0, column=3, sticky='we')

    im_forca = Image.open("Imagens/Tela_Game.png")
    im_forca = im_forca.resize((250, 250))
    ft_forca = ImageTk.PhotoImage(im_forca)
    lb_forca = Label(lf_im_forca, image=ft_forca)
    lb_forca.grid(row=0, column=0, padx=10, pady=10)

    lb_letra_errada = Label(lf_letra_errada, text='Letras Erradas:')
    lb_letra_errada.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    lb_letras_erradas = Label(lf_letra_errada, text='', font=("Arial", 17, "bold"), fg="red")
    lb_letras_erradas.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

    lb_palavra_secreta = Label(lf_palavra_secreta, text='Palavra Secreta:', anchor=CENTER)
    lb_palavra_secreta.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    lb_dica = Label(lf_palavra_secreta, text="Dica:", anchor=CENTER)
    lb_dica.grid(row=0, column=2, padx=10, pady=10)
    lb_dica_palavra = Label(lf_palavra_secreta, text=dica_palavra, anchor=CENTER)
    lb_dica_palavra.grid(row=0, column=3, padx=10, pady=10)
    lb_dica_palavra.config(font=("Arial", 12, "bold"))
    lb_segredo = Label(lf_palavra_secreta, text=texto_oculto, anchor=CENTER)
    lb_segredo.place(relx=0.5, rely=0.5)
    lb_segredo.config(font=("Arial", 18, "bold"))

    lb_entrada_letra = Label(lf_entrada_letra, text='Entre com uma letra:', anchor='e')
    lb_entrada_letra.grid(row=0, rowspan=3, column=0, padx=10, pady=10, sticky='we')
    en_entrada_letra = Entry(lf_entrada_letra)
    en_entrada_letra.grid(row=0, column=1, padx=10, pady=10)
    en_entrada_letra.bind("<Return>", lambda event: verificar())  # Adiciona a associação do evento
    bt_entrada_letra = Button(lf_entrada_letra, text="Verificar", command=verificar)
    bt_entrada_letra.grid(row=0, column=2, padx=10, pady=10)
    bt_entrada_letra.configure(background="black", foreground="white", activebackground="white",
                               activeforeground="black")

    lb_ranked = Label(lf_rank, text="Ranking", anchor=CENTER)
    lb_ranked.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky='we')

    for i in range(1, 21):
        lb_rank = Label(lf_rank, text=f'{i}º - ', anchor='e')
        lb_rank.grid(row=i, column=0, padx=1, pady=1, sticky='we')

    bt_Trolagem = Button(lf_tela_toda, text="Desistir", command=Trolagem)
    bt_Trolagem.grid(row=4, column=2, padx=10, pady=10)


@log_error
def enfrentar(nick_value):
    global ERROS
    palavra_secreta()
    tela_forca(nick_value)
    ERROS = 0


@log_error
def tela_win():
    global nick_value, pontos_value, im_win_game, ft_win_game, lb_win_game

    limpar_janela()
    lf_win_game = LabelFrame(menu_game, text="O fredd foi pego! SERÁ?", labelanchor='n')
    lf_win_game.place(relx=0.5, rely=0.5, anchor=CENTER)

    lb_vitoria = Label(lf_win_game, text="Parabéns, você acertou a palavra: {}".format(texto_original),
                       font=("Arial", 16, "bold"))
    lb_vitoria.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    im_win_game = Image.open("Imagens\Win_Game.jpg")
    ft_win_game = ImageTk.PhotoImage(im_win_game)
    lb_win_game = Label(lf_win_game, image=ft_win_game)
    lb_win_game.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    bt_continuar = Button(lf_win_game, text='Enfrentar SEUS MEDOS', command=lambda: enfrentar(nick_value.get()))
    bt_continuar.grid(row=2, column='0', padx=10, pady=10)
    bt_game_over = Button(lf_win_game, text='Sucumbir AO MEDO!', command=end_game)
    bt_game_over.grid(row=2, column='1', padx=10, pady=10)

    lb_nick = Label(lf_win_game, text="Nick: " + nick_value.get(), font=("Arial", 12))
    lb_nick.place(relx=0.2, rely=0.1)

    lb_pontos = Label(lf_win_game, text="Pontuação: " + pontos_value.get(), font=("Arial", 12))
    lb_pontos.place(relx=0.6, rely=0.1)


@log_error
def end_game():
    global im_end_game, ft_end_game, lb_end_game
    limpar_janela
    end_game = LabelFrame(menu_game)
    end_game.place(rely=0.5, relx=0.5, anchor=CENTER)

    im_end_game = Image.open("Imagens\Game_Over.png")
    ft_end_game = ImageTk.PhotoImage(im_end_game)
    lb_end_game = Label(end_game, image=ft_end_game)
    lb_end_game.grid(row=0, column=0, padx=10, pady=10)

    lb_nick = Label(end_game, text="Nick: " + nick_value.get(), font=("Arial", 18, "bold"))
    lb_nick.place(relx=0.3, rely=0.5, anchor=CENTER)

    lb_pontos = Label(end_game, text="Pontuação: " + pontos_value.get(), font=("Arial", 18, "bold"))
    lb_pontos.place(relx=0.7, rely=0.5, anchor=CENTER)

    restart_game = Button(end_game, text='Restart', anchor=CENTER, command=menu)
    restart_game.place(relx=0.45, rely=0.7)

    conexao = sqlite3.connect("Banco/Banco_de_Dados.db")
    cursor = conexao.cursor()
    cursor.execute("""
                   INSERT INTO Pontuação
                   (nome, pontos) values (?, ?)""",
                   (nick_value.get(), pontos_value.get())
                   )

    conexao.commit()
    conexao.close()
    palavra_secreta()


@log_error
def test_do_testando():
    teste = Tk()
    teste.title('TESTANDO')
    lb_teste = Label(teste, text="Teste de telas", anchor='n')
    lb_teste.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    lb_test = Label(teste, text="Aperte o botão para testar a mudança de tela!", anchor='n')
    lb_test.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    btzerar_rank = Button(teste, text='Test zerar_rank', command=zerar_rank)
    btzerar_rank.grid(row=1, column=0, sticky='we')
    btmenu = Button(teste, text='Test menu', command=menu)
    btmenu.grid(row=1, column=1, sticky='we')
    bttela_nick = Button(teste, text='Test tela_nick', command=tela_nick)
    bttela_nick.grid(row=1, column=2, sticky='we')
    bttela_forca = Button(teste, text='Test tela_forca', command=tela_forca)
    bttela_forca.grid(row=2, column=0, sticky='we')
    btfechar_janela = Button(teste, text='Test fechar_janela')
    btfechar_janela.grid(row=2, column=1, sticky='we')
    bttest_do_testando = Button(teste, text='test_do_testando', command=teste.destroy)
    bttest_do_testando.grid(row=2, column=2, sticky='we')


@log_error
def Trolagem():
    global im_troll, ft_troll, lb_troll, im_troll1, ft_troll1, lb_troll1

    lf_tela_toda.forget()
    lf_troll = LabelFrame(menu_game, text='"Nunca pare de sonhar" - Freddy Krueger', labelanchor='n')
    lf_troll.grid(row=0, column=0, padx=10, pady=10)

    im_troll = Image.open("Imagens/End_Game.jpg")
    im_troll = im_troll.resize((580, 395))
    ft_troll = ImageTk.PhotoImage(im_troll)
    lb_troll = Label(lf_troll, image=ft_troll)
    lb_troll.grid(row=0, column=0, padx=10, pady=10)

    im_troll1 = Image.open("Imagens/remake.jpg")
    im_troll1 = im_troll1.resize((580, 265))
    ft_troll1 = ImageTk.PhotoImage(im_troll1)
    lb_troll1 = Label(lf_troll, image=ft_troll1)
    lb_troll1.grid(row=1, column=0, padx=10, pady=10)

    @log_error
    def on_enter(event):
        global moved

        moved = False

        if not moved:
            x = random.randint(0,
                               lf_troll.winfo_width() - button.winfo_width())  # Gera uma coordenada X aleatória dentro da largura da janela
            y = random.randint(0,
                               lf_troll.winfo_height() - button.winfo_height())  # Gera uma coordenada Y aleatória dentro da altura da janela
            button.place(x=x, y=y)  # Define as novas coordenadas quando o mouse entra
            moved = True

    @log_error
    def on_leave(event):
        global moved
        moved = False

    button = tk.Button(lf_troll, text="DESISTIR!", )
    button.place(x=200, y=400)  # Define as coordenadas iniciais do botão
    bt_nao = Button(lf_troll, text="NÃO DESISTIR!", command=lf_troll.destroy)
    bt_nao.place(x=300, y=400)

    button.bind("<Enter>", on_enter)  # Associa a função on_enter ao evento de mouse 'Enter'
    button.bind("<Leave>", on_leave)  # Associa a função on_leave ao evento de mouse 'Leave'


BANCO()
limpar_janela()
menu()

menu_game.mainloop()
