import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("senai")
root.geometry("300x300+50+100")

def mostrar_nome():
    nome = entry_valor.get()
    valor_origem = entry_valor.get()
    messagebox.showinfo("Dados", f"Nome completo: {nome}\nCor dos olhos: {valor_origem}")

label=tk.Label(root, text="Valor:").grid(row=0,column=0, sticky="e", padx=5,pady=5)

entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1)


label2=tk.Label(root,text="Moeda de origem").grid(row=1,column=1, sticky="e", padx=5,pady=5)
combo2 = ttk.Combobox(root,values=["BRL", "USD" , "EUR",], state="readonly").grid(row=3,column=2)

label3=tk.Label(root,text="Moeda de Destino").grid(row=2,column=1, sticky="e", padx=5,pady=5)
combo3 = ttk.Combobox(root,values=["GBP", "JPY" , "(CNY",], state="readonly").grid(row=3,column=2)

root.mainloop()