import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry("400x600")
app.configure(bg="black")

tela = tk.Entry(app, font=("Consolas", 20), bg="#333333", fg="white", bd=0, justify="right")
tela.pack(fill="x", padx=10, pady=15, ipady=10)

def add(tecla):
    tela.insert(tk.END, tecla)

def limpar():
    tela.delete(0, tk.END)

def igual ():
    try:
        conta = tela.get()
        res = eval(conta)
        limpar()
        tela.insert(0, str(res))
    except:
        limpar()
        tela.insert(0, "Error")

frame_botoes =tk.Frame(app, bg="#222222")
frame_botoes.pack(expand=True, fill="both", padx=10, pady=5)

teclas = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

linha = 0
coluna = 0 

for t in teclas:
    if t == "=":
        btn = tk.Button(frame_botoes, text=t, bg="#ff9500", fg="white", font=("Arial", 14), bd=0, command=igual)
    elif t == "C":
        btn =tk.Button(frame_botoes, text=t, bg="#a6a6a6", fg="black", font=("Arial", 14), bd=0, command=limpar)
    else:
        btn = tk.Button(frame_botoes, text=t, bg="#505050", fg="white", font=("Arial", 14), bd=0, command=lambda x=t: add(x))

    btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

for i in range(4):
    frame_botoes.grid_rowconfigure(i, weight=1)
    frame_botoes.grid_columnconfigure(i, weight=1)

app.mainloop()


