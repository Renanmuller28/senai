import tkinter as tk


root = tk.Tk()
root.title("Login")
#root.geometry("340x100")


labelu = tk.Label(root, text= 'Faça seu login',font=('helvertica',20))
label = tk.Label(root, text='Usuário:')
entry = tk.Entry(root)
entre = tk.Entry(root)
labele = tk.Label(root, text='Senha:')
button=tk.Button(root,text="entrar")
checkbox = tk.Checkbutton(root, text="Aceito os termos")
minha_imagem= tk.PhotoImage(file='profile.png').subsample(2,2)
labeli = tk.Label(root, image=minha_imagem)
labelo = tk.Label(root, text="Esqueci minha senha!",fg="blue")

labelu.pack(fill="x",padx =30,pady=10)
labeli.pack()
label.pack(anchor="w",padx =10,pady=10)
entry.pack()
labele.pack(anchor="w", padx =10,pady=10)
entre.pack()
button.pack(fill="x", padx =10,pady=10)
checkbox.pack(side="left")
labelo.pack(side="right")

root.mainloop()