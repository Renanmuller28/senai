import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("senai")
root.geometry("300x300+50+100")

valores = {
    "BRL": 5.20,
    "USD": 1,
    "EUR": 0.87
}

def calculo_moeda():
    valor =float(entry_valor.get())
    origem =(combo2.get())
    destino=(combo3.get())

    valor_usd= valor / valores[origem]
    valor_convertidos = valor_usd * valores[destino]
    messagebox.showinfo('Seu valor', f"{valor_convertidos:.2f}") # Formata com duas casas decimais

label=tk.Label(root, text="Valor:").grid(row=0,column=0, sticky="e", padx=5,pady=5)

entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1)


label2=tk.Label(root,text="Moeda de origem").grid(row=1,column=0, sticky="e", padx=5,pady=5)
combo2 = ttk.Combobox(root,values=["BRL", "USD" , "EUR",], state="readonly")
combo2.grid(row=1,column=1)

label3=tk.Label(root,text="Moeda de Destino").grid(row=2,column=0, sticky="e", padx=5,pady=5)
combo3 = ttk.Combobox(root,values=["BRL", "USD" , "EUR",], state="readonly")
combo3.grid(row=2,column=1)

button=tk.Button(root,text="Converter", command=calculo_moeda).grid(row=4,column=1,columnspan=3)

root.mainloop()