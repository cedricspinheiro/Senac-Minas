contador_erradas = 0
pontuacao = 0
pontos = 0


def abrir_rank():
    conexao = sqlite3.connect('Banco_pontuacao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Pontuação")
    dados = cursor.fetchall()
    conexao.close()
    return dados


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
