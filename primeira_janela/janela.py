import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("SENAI - Desenvolvimento de sistemas")
root.geometry("400x200+50+250") # Define o tamanho da janela (largura x altura + posição X + posição Y)

# Cria um rótulo (label) com o texto "Hello, World!"
message = tk.Label(root, text="Hello, World!")

# Posiciona o rótulo na janela
message.pack()

# Inicia o loop principal da interface grafica
root.mainloop()