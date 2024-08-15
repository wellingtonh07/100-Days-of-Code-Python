from turtle import Turtle

class Bola(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_movimento = 0.5  # Velocidade inicial horizontal reduzida
        self.y_movimento = 0.5  # Velocidade inicial vertical reduzida
        self.velocidade_movimento = 0.2  # Velocidade de movimento geral

    def mover(self):
        novo_x = self.xcor() + self.x_movimento
        novo_y = self.ycor() + self.y_movimento
        self.goto(novo_x, novo_y)

    def quicar_y(self):
        self.y_movimento *= -1  # Inverte a direção vertical

    def quicar_x(self):
        self.x_movimento *= -1  # Inverte a direção horizontal
        self.velocidade_movimento *= 0.99  # Diminuição mais lenta

    def resetar_posicao(self):
        self.goto(0, 0)
        self.velocidade_movimento = 0.2  # Resetando a velocidade de movimento
        self.quicar_x()  # Faz a bola quicar na direção horizontal
