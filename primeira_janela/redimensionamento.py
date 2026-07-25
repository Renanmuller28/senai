import tkinter as tk
root = tk.Tk()
root.geometry('400x300')
root.resizable(False, True)

root.minsize(600, 200)
root.maxsize(800, 600)

message = tk.Label(root, text="Amo o Armandinho!")
root.attributes('-alpha', 1)

message.pack()
root.mainloop()