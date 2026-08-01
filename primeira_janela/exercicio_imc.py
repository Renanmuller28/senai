import tkinter as tk
from tkinter import ttk,messagebox

# Cria a JANELA PRINIPAL
root = tk.Tk()
root.title('SENAI - SISTEMAS') # Nome da janela
root.geometry('800x600') # Tamanho da janela

# Método para calcular o Índice de Massa Corporal (IMC)
def calculo():
    # Pega os valores armazenados no Entry
    peso =float(entry_peso.get())
    altura = float(entry_altura.get())

    # Fórmula do IMC
    imc=  peso / (altura * altura) 

    # Imprime na tela o resultado
    messagebox.showinfo('Seu IMC', f"{imc:.2f}") # Formata com duas casas decimais
    

# Criação dos elementos da tela
label_peso = tk.Label(root, text='Digite seu peso(KG)')
label_altura = tk.Label(root, text='Digite sua altura(M):')

entry_peso= tk.Entry(root)
entry_altura=tk.Entry(root)

button=tk.Button(root,text="CALCULAR", command=calculo) # "command=" faz a chamada da função

# Posiciona os elementos na JANELA PRINCIPAL
label_peso.pack()
entry_peso.pack()
label_altura.pack()
entry_altura.pack()
button.pack()



root.mainloop()