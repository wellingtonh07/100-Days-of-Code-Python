from turtle import Turtle

# Alinhamento e fonte para a pontuação
ALINHAMENTO = "center"
FONTE = ("Courier", 24, "normal")

class Placar(Turtle):
    
    def __init__(self):
        # Inicializa o objeto pai (Turtle) e configura o placar
        super().__init__()
        self.pontuacao = 0  # Inicializa a pontuação com 0
        self.color("white")  # Define a cor do texto como branco
        self.penup()  # Levanta o lápis para não desenhar linhas ao mover
        self.goto(0, 270)  # Posiciona o placar no topo da tela
        self.hideturtle()  # Esconde o cursor da tartaruga
        self.atualizar_placar()  # Atualiza o placar com a pontuação inicial

    def atualizar_placar(self):
        # Atualiza a exibição da pontuação no placar
        self.write(f"Pontuação: {self.pontuacao}", align=ALINHAMENTO, font=FONTE)

    def fim_de_jogo(self):
        # Exibe a mensagem de "Game Over" no centro da tela
        self.goto(0, 0)
        self.write("GAME OVER", align=ALINHAMENTO, font=FONTE)

    def aumentar_pontuacao(self):
        # Incrementa a pontuação em 1 e atualiza o placar
        self.pontuacao += 1
        self.clear()  # Limpa o texto antigo do placar
        self.atualizar_placar()  # Atualiza o placar com a nova pontuação
