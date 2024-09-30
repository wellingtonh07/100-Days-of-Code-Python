from turtle import Turtle

# Define a posição inicial, a distância de movimento e a linha de chegada
POSICAO_INICIAL = (0, -280)
DISTANCIA_MOVIMENTO = 10
LINHA_DE_CHEGADA_Y = 280

class Jogador(Turtle):
    # Inicializa a classe Jogador
    def __init__(self):
        super().__init__()  # Chama o inicializador da classe base Turtle
        self.shape("turtle")  # Define a forma da tartaruga como "turtle"
        self.penup()  # Levanta a caneta para não desenhar linhas
        self.voltar_para_inicio()  # Posiciona o jogador na posição inicial
        self.setheading(90)  # Define a direção inicial para cima (90 graus)

    # Move o jogador para cima na tela
    def mover_para_cima(self):
        self.forward(DISTANCIA_MOVIMENTO)  # Move o jogador para frente pela distância definida

    # Posiciona o jogador na posição inicial
    def voltar_para_inicio(self):
        self.goto(POSICAO_INICIAL)  # Move o jogador para a posição inicial

    # Verifica se o jogador chegou à linha de chegada
    def esta_na_linha_de_chegada(self):
        if self.ycor() > LINHA_DE_CHEGADA_Y:  # Compara a coordenada Y atual com a linha de chegada
            return True  # Retorna True se o jogador estiver acima da linha de chegada
        else:
            return False  # Retorna False se o jogador não tiver chegado
