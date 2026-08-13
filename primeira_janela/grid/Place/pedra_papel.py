from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

cor0= "#FFFFFF"
cor1= "#333333"
cor2= "#fcc058"
cor3= "#fff873"
cor4= "#34eb3d"
cor5= "#e85151"
fundo= "#3d3b3b"





janela= Tk()
janela.title("Pedra,papel,tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)


frame_cima = Frame(janela,width=260,height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame (janela, width=260, height=300,bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky =NW)

app_pessoa = Label(frame_cima, text="Jogador", height=1, anchor="center",
                   bg=cor1, fg=cor0 , font=("ivy 10 bold"))
app_pessoa.place(x=10, y=70)

app_pessoa_linha = Label(frame_cima, text="", height=1, anchor="center",
                   bg=cor4, fg=cor0 , font=("ivy 10 bold"))

app_pessoa.place(x=0, y=0)


app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                   bg=cor4, fg=cor0 , font=("ivy 30 bold"))

app_pessoa_pontos.place(x=0, y=0)

app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                   bg=cor1, fg=cor0 , font=("ivy 30 bold"))

app_pessoa_pontos.place(x=50, y=20)

app_pessoa_pontos = Label(frame_cima, text=":", height=1, anchor="center",
                   bg=cor4, fg=cor0 , font=("ivy 30 bold"))

app_pessoa_pontos.place(x=125, y=20)

app_pc = Label(frame_cima, text="PC", height=1,anchor="center", bg=cor1,fg=cor0, font =("ivy 10 bold"))
app_pc.place(x=205 , y=70)


app_pc_linha = Label(frame_cima, text="", height=1,anchor="center", bg=cor4,fg=cor0, font =("ivy 10 bold"))
app_pc_linha.place(x=255 , y=0)

app_pc_pontos = Label(frame_cima, text="0", height=1,anchor="center", bg=cor4,fg=cor0, font =("ivy 30 bold"))
app_pc_pontos.place(x=170 , y=20)

app_empate = Label(frame_cima, text="", width=255,anchor="center", bg=cor3,fg=cor0, font =("ivy 1 bold"))
app_empate.place(x=0 , y=95)

icone_pedra = Image.open("./imagens/pedra.png")
icone_pedra = icone_pedra.resize((50,50),Image.Resampling.LANCZOS)
icone_pedra = Image.tk


janela.mainloop()