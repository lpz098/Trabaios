import tkinter as tk

def clicar(valor):
    if valor == "C":
        entrada.set("")
    elif valor == "⌫":
        entrada.set(entrada.get()[:-1])
    elif valor == "=":
        try:
            resultado = eval(entrada.get())
            entrada.set(str(resultado))
        except Exception:
            entrada.set("Erro")
    else:
        entrada.set(entrada.get() + valor)

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")

entrada = tk.StringVar()

visor = tk.Entry(
    janela, textvariable=entrada, font=("Arial", 24),
    justify="right", bd=0, bg="#2d2d2d", fg="white",
    insertbackground="white"
)
visor.grid(row=0, column=0, columnspan=4, ipady=20, sticky="we", padx=10, pady=10)

botoes = [
    "C", "⌫", "%", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "="
]

linha = 1
coluna = 0

for b in botoes:
    def comando(x=b):
        clicar(x)

    largura_colunas = 2 if b == "0" else 1

    botao = tk.Button(
        janela, text=b, font=("Arial", 18), command=comando,
        bg="#3d3d3d", fg="white", activebackground="#4d4d4d",
        bd=0, width=5, height=2
    )
    botao.grid(row=linha, column=coluna, columnspan=largura_colunas, sticky="we", padx=2, pady=2)

    coluna += largura_colunas
    if coluna > 3:
        coluna = 0
        linha += 1

janela.mainloop()