from tkinter import *
from PIL import Image, ImageTk

pontos = 0

def def_nicks():
    arquivo_nick = 'Nick_Name.txt'
    with open(arquivo_nick, 'r') as arquivo:
        conteudo_nick = arquivo.read()
    return conteudo_nick

janela = Tk()
janela.geometry('700x640')

end_game = LabelFrame(janela)
end_game.place(rely=0.5, relx=0.5, anchor=CENTER)

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

pontuação = Label(end_game, text=str(pontos), font=("Arial", 18, "bold"))
pontuação.place(relx=0.8, rely=0.5, anchor=CENTER)

janela.mainloop()
