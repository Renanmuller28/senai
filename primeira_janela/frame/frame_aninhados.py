import tkinter as tk

root = tk.Tk()
root.title("Senai-Desenvolvimneto de Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=500,height=500)
frame.pack(padx=50, pady=50)

nested_frame = tk.Frame(frame, width=190, height=190, bg="black")
nested_frame.pack(padx=10,pady=10)

root.mainloop()