from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

contador_erradas = 0
pontuacao = 0
pontos = 0

def BANCO():
    conexao = sqlite3.connect('Banco_pontuacao.db')
    cursor1 = conexao.cursor()
    cursor1.execute("""
            create table if not exists Pontuação (
                id integer primary key autoincrement,
                nome text,
                pontos integer
            )
            """)
    conexao.close()


def zerar_rank():
    conexao = sqlite3.connect('Banco_pontuacao.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Pontuação")
    conexao.commit()
    conexao.close()
    print('Rank Zerado!')

def adicionar_letra_errada():
    global contador_erradas
    contador_erradas += 1
    def adicionar_letra_certa():
        global contador_certas
        contador_certas += 1
        return adicionar_letra_certa
    return adicionar_letra_certa

def adicionar_letra_certa():
    global contador_certas
    contador_certas += 1
    return adicionar_letra_certa

    pass


def verificar_letra():
    pass

def mostrar_tela_nick():
    tela_new_game.destroy()
    tela_nick_name.place(relx=0.5, rely=0.5, anchor=CENTER)

def mostrar_tela_forca():
    et_nick = nick_entry.get()  # Definir et_nick antes de utilizá-lo
    tela_nick_name.destroy()
    tela_forca.place(relx=0.5, rely=0.5, anchor=CENTER)
    lb_nick = Label(janela, text='Nick:', anchor=CENTER)
    lb_nick.place(relx=0.20, rely=0.015)
    nick = Label(janela, text=et_nick, anchor=CENTER)
    nick.place(relx=0.40, rely=0.015)
    pontos = Label(janela, text='Pontuação', anchor=CENTER)
    pontos.place(relx=0.60, rely=0.015)
    lb_pontos = Label(janela, text=pontuacao, anchor=CENTER)
    lb_pontos.place(relx=0.80, rely=0.015)
def abrir_rank():
    conexao = sqlite3.connect('Banco_pontuacao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Pontuação")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def restart():
    end_game.destroy()
    tela_new_game.place(relx=0.5, rely=0.5, anchor=CENTER)

def def_nicks():
    arquivo_nick = 'Nick_Name.txt'
    with open(arquivo_nick, 'r') as arquivo:
        conteudo_nick = arquivo.read()
    return conteudo_nick



janela = Tk()
janela.title("Jogo da Forca")
janela.geometry("700x640")
janela.resizable(False, False)

tela_new_game = LabelFrame(janela)
tela_new_game.place(relx=0.5, rely=0.5, anchor=CENTER)

#imagem_new_game = Image.open("/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/New_Game.jpg")
imagem_new_game = Image.open("New_Game.jpg")
imagem_new_game = imagem_new_game.resize((200, 200))
foto_new_game = ImageTk.PhotoImage(imagem_new_game)
label_new_game = Label(tela_new_game, image=foto_new_game)
label_new_game.grid(row=0, column=0, padx=10, pady=10)

new_game = Button(tela_new_game, text='New Game', anchor='center', command=mostrar_tela_nick)
new_game.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
new_game.configure(background="black", foreground="white", activebackground="white", activeforeground="black")

zerar_Rank = Button(tela_new_game, text='clear game', anchor='center', command=zerar_rank)
zerar_Rank.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

tela_nick_name = LabelFrame(janela)

imagem_nick_name = ImageTk.PhotoImage(imagem_new_game)
label_nick_name = Label(tela_nick_name, image=imagem_nick_name)
label_nick_name.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

nick_name_label = Label(tela_nick_name, text="Digite seu Nick:", anchor='e')
nick_name_label.grid(row=1, column=0, sticky='we')
nick_entry = Entry(tela_nick_name)
nick_entry.grid(row=1, column=1, padx=10, pady=10)
nick_entry.focus()

salvar_nick = Button(tela_nick_name, text="AVANÇAR", anchor="center", command=mostrar_tela_forca)
salvar_nick.grid(row=2, columnspan=2)
salvar_nick.configure(background="black", foreground="white", activebackground="white", activeforeground="black")

tela_forca = LabelFrame(janela)

quadro_imagem_forca = LabelFrame(tela_forca)
quadro_imagem_forca.grid(row=0, column=0, sticky='nswe')

#imagem_forca = Image.open("/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/Tela_Game.png")
imagem_forca = Image.open("Tela_Game.png")
imagem_forca = imagem_forca.resize((200, 200))
foto_forca = ImageTk.PhotoImage(imagem_forca)
label_forca = Label(quadro_imagem_forca, image=foto_forca)
label_forca.grid(padx=10, pady=10)

quadro_letras_erradas = LabelFrame(tela_forca)
quadro_letras_erradas.grid(row=0, column=1, sticky='nswe')

quadro_letras_erradas = LabelFrame(tela_forca)
quadro_letras_erradas.grid(row=0, column=1, sticky='nswe')

letras_erradas = Label(quadro_letras_erradas, text='Letras Erradas:')
letras_erradas.grid(row=0, padx=10, pady=10, sticky='w')

letras_erradas_label = Label(quadro_letras_erradas, text='', font=("Arial", 18, "bold"), fg="red")
letras_erradas_label.grid(row=1, padx=10, pady=10, sticky='w')

quadro_palavra_secreta = LabelFrame(tela_forca)
quadro_palavra_secreta.grid(row=1, column=0, columnspan=2, sticky='nswe')

palavra_secreta = Label(quadro_palavra_secreta, text='Palavra Secreta')
palavra_secreta.grid(padx=10, pady=10)

segredo = Label(quadro_palavra_secreta, text= 'PARALELEPÍPEDO', anchor=CENTER)
segredo.place(relx=0.3, rely=0.5)

quadro_entrada_letra = LabelFrame(tela_forca)
quadro_entrada_letra.grid(row=2, column=0, columnspan=2, sticky='nswe')

entrada_letra = Label(quadro_entrada_letra, text='Entre com uma letra:')
entrada_letra.grid(padx=10, pady=10)

entrada_letra_entry = Entry(quadro_entrada_letra)
entrada_letra_entry.grid(padx=10, pady=10)
entrada_letra_entry.focus()

salvar_letra = Button(quadro_entrada_letra, text="Verificar", anchor="center", command=verificar_letra)
salvar_letra.grid(padx=10, pady=10)
salvar_letra.configure(background="black", foreground="white", activebackground="white", activeforeground="black")

quadro_entrada_letra.grid_columnconfigure(0, weight=1)

quadro_rank = LabelFrame(tela_forca)
quadro_rank.grid(row=0, column=2, rowspan=3, sticky='nswe', padx=10, pady=10)

rank = Label(quadro_rank, text='Rank')
rank.grid(padx=10, pady=10)
BANCO()
dados = abrir_rank()

ranked_labels = []
for i in range(1, 21):
    ranked_label = Label(quadro_rank, text=f'{i}º', anchor='e')
    ranked_label.grid(padx=1, pady=1, sticky='e')
    ranked_labels.append(ranked_label)


abrir_rank()

ranked_entries = []
for i in range(1, 21):
    if i <= len(dados):
        ranked_entry = Entry(quadro_rank)
        ranked_entry.insert(END, dados[i-1])
    else:
        ranked_entry = Entry(quadro_rank, state='readonly')
    ranked_entry.config(state='readonly')
    ranked_entry.grid(row=i, column=1, padx=5, pady=2.5)
    ranked_entries.append(ranked_entry)


end_game = LabelFrame(janela)
#end_game.place(rely=0.5, relx=0.5, anchor=CENTER)

imagem_end_game = Image.open("Game_Over.png")
foto_end_game = ImageTk.PhotoImage(imagem_end_game)
label_new_game = Label(end_game, image=foto_end_game)
label_new_game.grid(row=0, column=0, padx=10, pady=10)

conteudo_nick = def_nicks()

lb_nick = Label(end_game, text='Nick:', font=("Arial", 18, "bold"))
lb_nick.place(relx=0.2, rely=0.5, anchor=CENTER)

def_nick = Label(end_game, text=conteudo_nick, font=("Arial", 18))
def_nick.place(relx=0.4, rely=0.5, anchor=CENTER)

lb_pontos = Label(end_game, text='Total:', font=("Arial", 18, "bold"))
lb_pontos.place(relx=0.6, rely=0.5, anchor=CENTER)

pontuacao = Label(end_game, text=str(pontos), font=("Arial", 18, "bold"))
pontuacao.place(relx=0.8, rely=0.5, anchor=CENTER)

restart_game = Button(end_game, text='Restart', anchor=CENTER, command=restart)
restart_game.place(relx=0.5, rely=0.7)


janela.mainloop()
