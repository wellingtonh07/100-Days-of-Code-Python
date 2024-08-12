from turtle import Turtle

# Posições iniciais da cobra
POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]
# Distância que a cobra se move a cada vez
DISTANCIA_MOVIMENTO = 20
# Direções em graus
CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0

class Cobra:

    def __init__(self):
        # Lista para armazenar os segmentos da cobra
        self.segmentos = []
        # Cria a cobra com os segmentos iniciais
        self.criar_cobra()
        # Define a cabeça da cobra como o primeiro segmento
        self.cabeca = self.segmentos[0]

    def criar_cobra(self):
        # Cria a cobra a partir das posições iniciais
        for posicao in POSICOES_INICIAIS:
            self.adicionar_segmento(posicao)

    def adicionar_segmento(self, posicao):
        # Cria um novo segmento da cobra
        novo_segmento = Turtle("square")
        novo_segmento.color("white")
        novo_segmento.penup()
        novo_segmento.goto(posicao)
        self.segmentos.append(novo_segmento)

    def estender(self):
        # Adiciona um novo segmento ao final da cobra
        self.adicionar_segmento(self.segmentos[-1].position())

    def mover(self):
        # Move os segmentos da cobra, começando do último até o segundo
        for num_seg in range(len(self.segmentos) - 1, 0, -1):
            novo_x = self.segmentos[num_seg - 1].xcor()
            novo_y = self.segmentos[num_seg - 1].ycor()
            self.segmentos[num_seg].goto(novo_x, novo_y)
        # Move a cabeça da cobra para frente
        self.cabeca.forward(DISTANCIA_MOVIMENTO)

    def cima(self):
        # Define a direção da cabeça para cima, se não estiver indo para baixo
        if self.cabeca.heading() != BAIXO:
            self.cabeca.setheading(CIMA)

    def baixo(self):
        # Define a direção da cabeça para baixo, se não estiver indo para cima
        if self.cabeca.heading() != CIMA:
            self.cabeca.setheading(BAIXO)

    def esquerda(self):
        # Define a direção da cabeça para esquerda, se não estiver indo para a direita
        if self.cabeca.heading() != DIREITA:
            self.cabeca.setheading(ESQUERDA)

    def direita(self):
        # Define a direção da cabeça para direita, se não estiver indo para a esquerda
        if self.cabeca.heading() != ESQUERDA:
            self.cabeca.setheading(DIREITA)
