from tkinter import *
from PIL import Image, ImageTk
import os

contador_erradas = 0


def zerar_rank():
    # arquivo_rank = '/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/Rank.txt'
    arquivo_rank = 'Rank.txt'
    with open(arquivo_rank, "w") as file:
        file.write('')
    print('O Rank foi Zerado!')


def adicionar_letra_errada(letra):
    global contador_erradas
    contador_erradas += 1
    letras_erradas_var.set(f"{letras_erradas_var.get()} {letra}")
    if contador_erradas >= 7:
        pass


def verificar_letra():
    if letra.get() == "a":
        letra.set("b")
        letra.update()
        return


def mostrar_tela_nick():
    tela_new_game.destroy()
    tela_nick_name.place(relx=0.5, rely=0.5, anchor=CENTER)


def mostrar_tela_forca():
    tela_nick_name.destroy()
    tela_forca.place(relx=0.5, rely=0.5, anchor=CENTER)


def salvar_nick():
    nick_digitado = nick_entry.get()
    # arquivo_nick = "/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/Nick_Name.txt"
    arquivo_nick = "Nick_Name.txt"
    with open(arquivo_nick, "w") as file:
        file.write(nick_digitado)
    print("Nick salvo com sucesso!")
    nick_entry.delete(0, END)
    mostrar_tela_forca()


def abrir_rank():
    # arquivo_rank = "/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/Rank.txt"
    arquivo_rank = "Rank.txt"
    with open(arquivo_rank, "r") as file:
        conteudo_rank = file.read()
    return conteudo_rank


janela = Tk()
janela.title("Jogo da Forca")
janela.geometry("700x640")
janela.resizable(False, False)

tela_new_game = LabelFrame(janela)
tela_new_game.place(relx=0.5, rely=0.5, anchor=CENTER)

# imagem_new_game = Image.open("/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/New_Game.jpg")
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

salvar_nick = Button(tela_nick_name, text="AVANÇAR", anchor="center", command=salvar_nick)
salvar_nick.grid(row=2, columnspan=2)
salvar_nick.configure(background="black", foreground="white", activebackground="white", activeforeground="black")

tela_forca = LabelFrame(janela)

quadro_imagem_forca = LabelFrame(tela_forca)
quadro_imagem_forca.grid(row=0, column=0, sticky='nswe')

# imagem_forca = Image.open("/home/nkkara/Documentos/Repertorios/Senac Minas/Projeto Integrador/Tela_Game.png")
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

letras_erradas_var = StringVar()
letras_erradas_label = Label(quadro_letras_erradas, textvariable=letras_erradas_var, font=("Arial", 18, "bold"),
                             fg="red")
letras_erradas_label.grid(row=1, padx=10, pady=10, sticky='w')

quadro_palavra_secreta = LabelFrame(tela_forca)
quadro_palavra_secreta.grid(row=1, column=0, columnspan=2, sticky='nswe')

palavra_secreta = Label(quadro_palavra_secreta, text='Palavra Secreta')
palavra_secreta.grid(padx=10, pady=10)

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

ranked_labels = []
for i in range(1, 21):
    ranked_label = Label(quadro_rank, text=f'{i}º', anchor='e')
    ranked_label.grid(padx=1, pady=1, sticky='e')
    ranked_labels.append(ranked_label)

conteudo_rank = abrir_rank()
ranked_entries = []
for i in range(1, 21):
    ranked_entry = Entry(quadro_rank)
    ranked_entry.insert(END, conteudo_rank)
    ranked_entry.config(state='readonly')
    ranked_entry.grid(row=i, column=1, padx=5, pady=2.5)
    ranked_entries.append(ranked_entry)

janela.mainloop()
