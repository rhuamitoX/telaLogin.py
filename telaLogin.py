import tkinter as tk
from tkinter import messagebox

def login():
    email = input_email.get()
    senha = input_senha.get()
    if email=="admin" and senha=="1234":
        print("sucesso")
    else:
        print("falha")    
    
app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")

label_email = tk.Label(app, text="Email:")
label_email.pack(pady=5)

input_email = tk.Entry(app)
input_email.pack()

label_senha = tk.Label(app, text="Senha:")
label_senha.pack(pady=5)

input_senha = tk.Entry(app)
input_senha.pack()

btn_enviar = tk.Button(app, text="Enviar", command=login)
btn_enviar.pack()

app.mainloop()