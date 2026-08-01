import tkinter as tk

root = tk.Tk()
root.title("Senai-Desenvolvimneto de Sistemas")
root.geometry("340x100")

tk.Button(root, text="Top Button!").pack()
tk.Label(root, text="Hello, Left!").pack(side="left")
tk.Label(root, text="Hello,right!").pack(side="right")
tk.Checkbutton(root, text="uma opção na parte inferior!").pack(side=tk.BOTTOM)

root.mainloop()