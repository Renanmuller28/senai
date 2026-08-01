import tkinter as tk

root = tk.Tk()
root.title("Senai-Desenvolvimneto de Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=500,height=500)
frame.pack(padx=50, pady=50)

a_frame = tk.Frame(frame, width=190, heigth=190, dg="red")
a_frame.pack(side="left", padx =10,pady=10)

b_frame = tk.Frame(frame, width=190, heigth=190, dg="red")
b_frame.pack(side="right", padx =10,pady=10)

root.mainloop()