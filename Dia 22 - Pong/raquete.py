from turtle import Turtle

class Raquete(Turtle):
    
    def __init__(self, posicao):
        super().__init__()
        self.shape("square")  # Define a forma da raquete como quadrado
        self.color("white")  # Define a cor da raquete como branca
        self.shapesize(stretch_wid=5, stretch_len=1)  # Define o tamanho da raquete
        self.penup()  # Levanta o lápis para que não desenhe linhas
        self.goto(posicao)  # Move a raquete para a posição inicial fornecida
        self.movendo = False  # Flag para verificar se a raquete está se movendo
        self.velocidade = 3  # Velocidade de movimento da raquete (ajustado para ser mais lento)

    def sobe(self):
        self.movendo = "sobe"

    def desce(self):
        self.movendo = "desce"

    def parar(self):
        self.movendo = False

    def mover(self):
        if self.movendo == "sobe":
            nova_y = self.ycor() + self.velocidade  # Calcula a nova posição y ao mover para cima
            # Verifica se a nova posição está dentro dos limites da tela
            if nova_y < 250:  # Limite superior
                self.goto(self.xcor(), nova_y)
        elif self.movendo == "desce":
            nova_y = self.ycor() - self.velocidade  # Calcula a nova posição y ao mover para baixo
            # Verifica se a nova posição está dentro dos limites da tela
            if nova_y > -240:  # Limite inferior
                self.goto(self.xcor(), nova_y)
