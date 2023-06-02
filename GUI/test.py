import tkinter as tk

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if escolha.get() == 1:
        resultado = num1 + num2
    elif escolha.get() == 2:
        resultado = num1 - num2
    elif escolha.get() == 3:
        resultado = num1 * num2
    elif escolha.get() == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero!"

    label_resultado.config(text="Resultado: {}".format(resultado))


# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criação dos elementos da interface
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(janela)
entry_num1.pack()

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(janela)
entry_num2.pack()

escolha = tk.IntVar()
escolha.set(1)

radio_soma = tk.Radiobutton(janela, text="Soma", variable=escolha, value=1)
radio_soma.pack()

radio_subtracao = tk.Radiobutton(janela, text="Subtração", variable=escolha, value=2)
radio_subtracao.pack()

radio_multiplicacao = tk.Radiobutton(janela, text="Multiplicação", variable=escolha, value=3)
radio_multiplicacao.pack()

radio_divisao = tk.Radiobutton(janela, text="Divisão", variable=escolha, value=4)
radio_divisao.pack()

button_calcular = tk.Button(janela, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack()

# Loop principal da interface gráfica
janela.mainloop()
