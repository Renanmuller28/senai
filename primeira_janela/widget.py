import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry('400x300')

def button_command():
    messagebox.showinfo(
        "infotmações",
        "eu falei o de baixo!"
    )
button = tk.Button(
    root, text="clique o de baixo",
    command=button_command
)
button.pack()


def button_commando():
    messagebox.showinfo(
        "informações",
        "Você é Lindo!")

button2 = tk.Button(
    root, text="Toque aqui",
    command=button_commando)
button2.pack()

root.mainloop()