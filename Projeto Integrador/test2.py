import tkinter as tk
import random

def on_enter(event):
    global moved
    if not moved:
        x = random.randint(0, root.winfo_width() - button.winfo_width())  # Gera uma coordenada X aleatória dentro da largura da janela
        y = random.randint(0, root.winfo_height() - button.winfo_height())  # Gera uma coordenada Y aleatória dentro da altura da janela
        button.place(x=x, y=y)  # Define as novas coordenadas quando o mouse entra
        moved = True

def on_leave(event):
    global moved
    moved = False

button = tk.Button(lf_troll, text="Me mova!", width=10, height=2)
button.place(x=100, y=100)  # Define as coordenadas iniciais do botão

moved = False

button.bind("<Enter>", on_enter)  # Associa a função on_enter ao evento de mouse 'Enter'
button.bind("<Leave>", on_leave)  # Associa a função on_leave ao evento de mouse 'Leave'

root.mainloop()
