from turtle import Turtle

# Define a fonte usada para escrever no painel de placar
FONTE = ("Courier", 24, "normal")

class Placar(Turtle):
    # Inicializa a classe Placar
    def __init__(self):
        super().__init__()  # Chama o inicializador da classe base Turtle
        self.nivel = 1  # Define o nível inicial como 1
        self.hideturtle()  # Oculta a tartaruga (o cursor de desenho)
        self.penup()  # Levanta a caneta para não desenhar linhas
        self.goto(-280, 250)  # Posiciona o texto no canto superior esquerdo da tela
        self.atualiza_placar()  # Atualiza o placar ao iniciar

    # Atualiza o placar com o nível atual
    def atualiza_placar(self):
        self.clear()  # Limpa o texto anterior
        # Escreve o nível atual no painel
        self.write(f"Nível: {self.nivel}", align="left", font=FONTE)

    # Incrementa o nível e atualiza o placar
    def aumenta_nivel(self):
        self.nivel += 1  # Aumenta o nível em 1
        self.atualiza_placar()  # Atualiza o placar com o novo nível

    # Exibe a mensagem de "GAME OVER" no centro da tela
    def jogo_acabou(self):
        self.goto(0, 0)  # Move a tartaruga para o centro da tela
        self.write(f"FIM DE JOGO", align="center", font=FONTE)
