contador_erradas = 0
pontuacao = 0
pontos = 0
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
