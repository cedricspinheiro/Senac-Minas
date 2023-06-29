from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

### VARIAVES ###

### FIM DAS VARIAVEIS ###

### TELA E TAMANHO DEFINIDA ###
menu_game = Tk()
menu_game.title("Jogo da Forca")
menu_game.geometry("700x640")
menu_game.resizable(False, False)


### NÃO MEXER AQUI ###

def BANCO():
    conexao = sqlite3.connect('Banco/Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute("""
            create table if not exists Pontuação (
                id integer primary key autoincrement,
                nome text,
                pontos integer
            )
            """)
    conexao.close()


def zerar_rank():
    conexao = sqlite3.connect('Banco/Banco_de_Dados.db')
    cursor = conexao.cursor()
    cursor.execute('drop table Pontuação')
    conexao.commit()
    conexao.close()
    print('Rank Zerado!')


def limpar_janela():
    for widget in menu_game.winfo_children():
        widget.destroy()


def menu():
    limpar_janela()
    global ft_menu_game
    # im_menu_game = Image.open("/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Final/Imagens/Menu Game.jpg")
    im_menu_game = Image.open("Imagens/Menu Game.jpg")
    ft_menu_game = ImageTk.PhotoImage(im_menu_game)

    lf_menu_game = LabelFrame(menu_game, text='Você está REALMENTE pronto?', labelanchor='n')
    lf_menu_game.place(relx=0.5, rely=0.5, anchor=CENTER)

    lb_menu_game = Label(lf_menu_game, image=ft_menu_game)
    lb_menu_game.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    bt_new_game = Button(lf_menu_game, text='New Game', anchor='center', command=tela_nick)
    bt_new_game.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
    bt_new_game.configure(background="black", foreground="white", activebackground="white", activeforeground="black")

    bt_zerar_rank = Button(lf_menu_game, text='clear game', anchor='center')
    bt_zerar_rank.grid(row=1, column=1, padx=10, pady=10, sticky='nswe')

def tela_nick():
    global en_nick
    limpar_janela()
    lf_tela_nick = LabelFrame(menu_game, text='Aqui você DIGITA o seu nick de preferencia!', labelanchor='n')
    lf_tela_nick.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_tela_nick.configure(padx=10, pady=10)

    lb_tela_nick = Label(lf_tela_nick, image=ft_menu_game)
    lb_tela_nick.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

    lb_nick = Label(lf_tela_nick, text="Digite seu NICK:", anchor='e')
    lb_nick.grid(row=1, column=0, sticky='we')
    en_nick = Entry(lf_tela_nick)
    en_nick.grid(row=1, column=1)
    bt_nick = Button(lf_tela_nick, text="AVANÇAR", anchor="center", command=tela_forca)
    bt_nick.grid(row=1, column=2)
    bt_nick.configure(background="black", foreground="white", activebackground="white", activeforeground="black")


def tela_forca():
    limpar_janela()

    global im_forca, ft_forca, lb_forca

    lf_tela_toda = LabelFrame(menu_game)
    lf_tela_toda.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_im_forca = LabelFrame(lf_tela_toda, text='Pegue o Fredd!', labelanchor='n', font=("Arial", 12, "bold"))
    lf_im_forca.grid(row=0, column=0, sticky='nswe')
    lf_letra_errada = LabelFrame(lf_tela_toda, text='7 Tentativas', labelanchor='n', font=("Arial", 12, "bold"))
    lf_letra_errada.grid(row=0, column=1, sticky='nswe')
    lf_palavra_secreta = LabelFrame(lf_tela_toda, text='Adivinhe qual é a Palavra Secreta!', font=("Arial", 12, "bold"))
    lf_palavra_secreta.grid(row=1, column=0, columnspan=2, sticky='nswe')
    lf_entrada_letra = LabelFrame(lf_tela_toda, text='Entre com UMA LETRA ou com a PALAVRA SECRETA', labelanchor='n', font=("Arial", 12, "bold"))
    lf_entrada_letra.grid(row=2, column=0, columnspan=2, sticky='nswe')

    im_forca = Image.open("Imagens/Tela_Game.png")
    im_forca = im_forca.resize((250, 250))
    ft_forca = ImageTk.PhotoImage(im_forca)
    lb_forca = Label(lf_im_forca, image=ft_forca)
    lb_forca.grid(row=0, column=0, padx=10, pady=10)

    lb_letra_errada = Label(lf_letra_errada, text='Letras Erradas:')
    lb_letra_errada.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    lb_letras_erradas = Label(lf_letra_errada, text='A\nb\nc\nd\ne\nf\ng\n', font=("Arial", 18, "bold"), fg="red")
    lb_letras_erradas.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

    lb_palavra_secreta = Label(lf_palavra_secreta, text='Palavra Secreta:')
    lb_palavra_secreta.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    lb_segredo = Label(lf_palavra_secreta, text='PARALELEPIPEDO', anchor=CENTER)
    lb_segredo.place(relx=0.4, rely=0.3)

    lb_entrada_letra = Label(lf_entrada_letra, text='Entre com uma letra:', anchor='e')
    lb_entrada_letra.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    en_entrada_letra = Entry(lf_entrada_letra)
    en_entrada_letra.grid(row=0, column=1, padx=10, pady=10)
    bt_entrada_letra = Button(lf_entrada_letra, text="Verificar")
    bt_entrada_letra.grid(row=0, column=2, padx=10, pady=10)
    bt_entrada_letra.configure(background="black", foreground="white", activebackground="white", activeforeground="black")


BANCO()
limpar_janela()
menu()

menu_game.mainloop()
