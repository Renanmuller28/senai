import tkinter as tk
import random

# -----------------------------
# Configuração da janela
# -----------------------------
janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("500x450")
janela.resizable(False, False)
janela.configure(bg="#1e1e2e")

# -----------------------------
# Variáveis do jogo
# -----------------------------
jogador_pontos = 0
computador_pontos = 0

opcoes = ["Pedra", "Papel", "Tesoura"]


# -----------------------------
# Função para jogar
# -----------------------------
def jogar(escolha_jogador):
    global jogador_pontos, computador_pontos

    escolha_computador = random.choice(opcoes)

    # Mostra as escolhas
    label_jogador.config(text=f"Você escolheu: {escolha_jogador}")
    label_computador.config(text=f"Computador escolheu: {escolha_computador}")

    # Verifica o vencedor
    if escolha_jogador == escolha_computador:
        resultado = "EMPATE! 🤝"

    elif (
        (escolha_jogador == "Pedra" and escolha_computador == "Tesoura")
        or
        (escolha_jogador == "Papel" and escolha_computador == "Pedra")
        or
        (escolha_jogador == "Tesoura" and escolha_computador == "Papel")
    ):
        jogador_pontos += 1
        resultado = "VOCÊ GANHOU! 🎉"

    else:
        computador_pontos += 1
        resultado = "COMPUTADOR GANHOU! 🤖"

    # Atualiza resultado e placar
    label_resultado.config(text=resultado)

    label_placar.config(
        text=f"Você: {jogador_pontos}   x   {computador_pontos} : Computador"
    )


# -----------------------------
# Função para reiniciar
# -----------------------------
def reiniciar():
    global jogador_pontos, computador_pontos

    jogador_pontos = 0
    computador_pontos = 0

    label_jogador.config(text="Você escolheu: -")
    label_computador.config(text="Computador escolheu: -")
    label_resultado.config(text="Faça sua escolha!")
    label_placar.config(text="Você: 0   x   0 : Computador")


# -----------------------------
# Título
# -----------------------------
titulo = tk.Label(
    janela,
    text="PEDRA, PAPEL E TESOURA",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#1e1e2e"
)
titulo.pack(pady=20)


# -----------------------------
# Placar
# -----------------------------
label_placar = tk.Label(
    janela,
    text="Você: 0   x   0 : Computador",
    font=("Arial", 16, "bold"),
    fg="#00ff99",
    bg="#1e1e2e"
)
label_placar.pack(pady=10)


# -----------------------------
# Escolhas
# -----------------------------
label_jogador = tk.Label(
    janela,
    text="Você escolheu: -",
    font=("Arial", 13),
    fg="white",
    bg="#1e1e2e"
)
label_jogador.pack(pady=5)

label_computador = tk.Label(
    janela,
    text="Computador escolheu: -",
    font=("Arial", 13),
    fg="white",
    bg="#1e1e2e"
)
label_computador.pack(pady=5)


# -----------------------------
# Resultado
# -----------------------------
label_resultado = tk.Label(
    janela,
    text="Faça sua escolha!",
    font=("Arial", 18, "bold"),
    fg="#ffd700",
    bg="#1e1e2e"
)
label_resultado.pack(pady=20)


# -----------------------------
# Botões
# -----------------------------
frame_botoes = tk.Frame(janela, bg="#1e1e2e")
frame_botoes.pack(pady=10)

botao_pedra = tk.Button(
    frame_botoes,
    text="🪨 Pedra",
    font=("Arial", 13, "bold"),
    width=12,
    height=2,
    bg="#555577",
    fg="white",
    command=lambda: jogar("Pedra")
)
botao_pedra.grid(row=0, column=0, padx=5)

botao_papel = tk.Button(
    frame_botoes,
    text="📄 Papel",
    font=("Arial", 13, "bold"),
    width=12,
    height=2,
    bg="#555577",
    fg="white",
    command=lambda: jogar("Papel")
)
botao_papel.grid(row=0, column=1, padx=5)

botao_tesoura = tk.Button(
    frame_botoes,
    text="✂️ Tesoura",
    font=("Arial", 13, "bold"),
    width=12,
    height=2,
    bg="#555577",
    fg="white",
    command=lambda: jogar("Tesoura")
)
botao_tesoura.grid(row=0, column=2, padx=5)


# -----------------------------
# Botão reiniciar
# -----------------------------
botao_reiniciar = tk.Button(
    janela,
    text="🔄 Reiniciar",
    font=("Arial", 12, "bold"),
    width=15,
    bg="#ff5555",
    fg="white",
    command=reiniciar
)
botao_reiniciar.pack(pady=25)


# -----------------------------
# Inicia o programa
# -----------------------------
janela.mainloop()