from turtle import Turtle
import random

class Comida(Turtle):
    
    def __init__(self):
        # Inicializa o objeto pai (Turtle) e configura o objeto de comida
        super().__init__()
        self.shape("circle")  # Define a forma da comida como um círculo
        self.penup()  # Levanta o lápis para não desenhar linhas ao mover
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Define o tamanho da comida
        self.color("blue")  # Define a cor da comida como azul
        self.speed("fastest")  # Define a velocidade de desenho como a mais rápida
        self.atualizar()  # Posiciona a comida em uma posição inicial aleatória

    def atualizar(self):
        # Atualiza a posição da comida para uma nova posição aleatória
        x_aleatorio = random.randint(-280, 280)  # Gera uma coordenada x aleatória
        y_aleatorio = random.randint(-280, 280)  # Gera uma coordenada y aleatória
        self.goto(x_aleatorio, y_aleatorio)  # Move a comida para a nova posição
