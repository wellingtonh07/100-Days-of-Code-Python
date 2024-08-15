from turtle import Turtle

class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")  # Define a cor do texto como branca
        self.penup()  # Levanta o lápis para que não desenhe linhas
        self.hideturtle()  # Esconde a tartaruga (cursor) do desenho
        self.pontos_esquerda = 0  # Inicializa os pontos da esquerda
        self.pontos_direita = 0  # Inicializa os pontos da direita
        self.atualiza_placar()  # Atualiza o placar na tela

    def atualiza_placar(self):
        self.clear()  # Limpa o texto anterior
        self.goto(-100, 200)  # Move a tartaruga para a posição (-100, 200)
        self.write(self.pontos_esquerda, align="center", font=("Courier", 80, "normal"))  # Escreve os pontos da esquerda
        self.goto(100, 200)  # Move a tartaruga para a posição (100, 200)
        self.write(self.pontos_direita, align="center", font=("Courier", 80, "normal"))  # Escreve os pontos da direita

    def ponto_esquerda(self):
        self.pontos_esquerda += 1  # Adiciona um ponto para a esquerda
        self.atualiza_placar()  # Atualiza o placar

    def ponto_direita(self):
        self.pontos_direita += 1  # Adiciona um ponto para a direita
        self.atualiza_placar()  # Atualiza o placar
