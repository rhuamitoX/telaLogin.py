import tkinter as tk
from conta import Conta
import json
def cadastrar():
    agencia = input_agencia.get()
    titular = input_titular.get()
    cpf = input_cpf.get()
    nova_conta = Conta(agencia, titular, cpf)
    with open("clientes.json","r") as clientes_leitura:
        clientes = json.load(clientes_leitura)
    # adicionar o novo cliente
    clientes.append({
        "titular": nova_conta.titular,
        "agencia": nova_conta.agencia,
        "numero": nova_conta.numero,
        "cpf": nova_conta.cpf,
        "saldo": nova_conta.saldo,
        "senha": nova_conta.senha,
        "chavepix": nova_conta.chavepix       
    })
    # salvar no arquivo
    with open("clientes.json" , "w") as clientes_escrita:
        json.dump(clientes, clientes_escrita, indent=4)
    # resposta de sucesso na tela
    label_resposta.configure(
        text=f"Conta: {nova_conta.numero} Titular:{nova_conta.titular} cadastrado com sucesso!",
        fg="green")


app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")
# agencia
label_agencia = tk.Label(app, text="agencia:")
label_agencia.pack(pady=5)
input_agencia = tk.Entry(app)
input_agencia.pack()

# titular
label_titular = tk.Label(app, text="titular:")
label_titular.pack(pady=5)
input_titular = tk.Entry(app)
input_titular.pack()

# cpf
label_cpf = tk.Label(app, text="cpf:")
label_cpf.pack(pady=5)
input_cpf = tk.Entry(app)
input_cpf.pack()

btn_enviar = tk.Button(app, text="cadastrar conta", command=cadastrar)
btn_enviar.pack()

label_resposta = tk.Label(app, text="")
label_resposta.pack(pady=5)

app.mainloop()