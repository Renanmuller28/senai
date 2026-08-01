import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Senai-Desenvolvimneto de Sistemas")
root.geometry("340x100")

def button_command():
    nome = entry.get()
    messagebox.showinfo('nome completo', nome)

label = tk.Label(root, text='usuario:')
button=tk.Button(root,text="usuario", command=button_command)

label.pack()
button.pack()
root.mainloop()

