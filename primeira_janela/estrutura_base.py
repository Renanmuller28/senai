import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('67')
root.geometry('800x600')

label_1= tk.Label(root, text='Olá')
label_1.pack()

label_2 = tk.Label(root)
label_2.pack()
label_2.config(text="definido depois")

label_3 = tk.Label(root,text="OLÁ",
font=('helvertica',30))

label_3.pack(expand=True)

minha_imagem= tk.PhotoImage(fil='gremio.jpg')

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)
root.mainloop()