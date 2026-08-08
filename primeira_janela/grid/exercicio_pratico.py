import tkinter as tk
from tkinter import ttk, messagebox


root = tk.Tk()
root.title("SENAI")
root.resizable(False, False)

def mostrar_nome():
    nome = entry.get()
    cor_olhos = entry_cor.get()
    messagebox.showinfo("Dados", f"Nome completo: {nome}\nCor dos olhos: {cor_olhos}")

minha_imagem= tk.PhotoImage(file='profile.png').subsample(2,2)
label = tk.Label(root, image=minha_imagem)

label.grid(row=0,column=0,rowspan=5, sticky="e", padx=2,pady=2)
label=tk.Label(root,text="Nome").grid(row=0,column=1, sticky="e", padx=5,pady=5)

entry = tk.Entry(root) # Imposivel instanciar e posicionar na tela de forma conjunta
entry.grid(row=0, column=2)

#combo = ttk.Combobox(root,).grid(row=0,column=2)
label2=tk.Label(root,text="Gênero").grid(row=1,column=1, sticky="e", padx=5,pady=5)
combo2 = ttk.Combobox(root,values=["Feminino", "Masculino",], state="readonly").grid(row=1,column=2)

label3=tk.Label(root,text="Cor dos olhos").grid(row=2,column=1, sticky="e", padx=5,pady=5)

entry_cor = tk.Entry(root)
entry_cor.grid(row=2, column=2)

#combo3 = ttk.Combobox(root,).grid(row=2,column=2)

label4=tk.Label(root,text="Altura(cm)").grid(row=3,column=1, sticky="e", padx=5,pady=5)
combo4 = ttk.Combobox(root).grid(row=3,column=2)

label5=tk.Label(root,text="Peso(kg)").grid(row=4,column=1, sticky="e", padx=5,pady=5)
combo5 = ttk.Combobox(root).grid(row=4,column=2)

button=tk.Button(root,text="Enviar", command=mostrar_nome).grid(row=5,column=2,sticky="e", padx=5 , pady=5)

root.mainloop()