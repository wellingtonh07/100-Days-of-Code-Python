from turtle import Screen
from cobra import Cobra
from comida import Comida
from pontuação import Placar
import time

# Configuração da tela
tela = Screen()
tela.setup(width=600, height=600)  # Define o tamanho da tela
tela.bgcolor("black")  # Define a cor de fundo da tela como preto
tela.title("Meu Jogo da Cobrinha")  # Define o título da janela do jogo
tela.tracer(0)  # Desativa o desenho automático da tela para melhor desempenho

# Criação dos objetos do jogo
cobra = Cobra()  # Cria uma instância da classe Cobra
comida = Comida()  # Cria uma instância da classe Comida
placar = Placar()  # Cria uma instância da classe Placar

# Configuração dos controles do teclado
tela.listen()  # Começa a ouvir os eventos do teclado
tela.onkey(cobra.cima, "Up")  # Define a tecla "Up" para mover a cobra para cima
tela.onkey(cobra.baixo, "Down")  # Define a tecla "Down" para mover a cobra para baixo
tela.onkey(cobra.esquerda, "Left")  # Define a tecla "Left" para mover a cobra para a esquerda
tela.onkey(cobra.direita, "Right")  # Define a tecla "Right" para mover a cobra para a direita

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    tela.update()  # Atualiza a tela
    time.sleep(0.1)  # Faz uma pausa para controlar a velocidade do jogo
    cobra.mover()  # Move a cobra

    # Detecta colisão com a comida
    if cobra.cabeca.distance(comida) < 15:
        comida.atualizar()  # Move a comida para uma nova posição aleatória
        cobra.estender()  # Adiciona um segmento ao corpo da cobra
        placar.aumentar_pontuacao()  # Incrementa a pontuação

    # Detecta colisão com as paredes
    if (cobra.cabeca.xcor() > 280 or cobra.cabeca.xcor() < -280 or 
        cobra.cabeca.ycor() > 280 or cobra.cabeca.ycor() < -280):
        jogo_ativo = False  # Encerra o jogo
        placar.fim_de_jogo()  # Exibe a mensagem de "Game Over"

    # Detecta colisão com o próprio corpo
    for segmento in cobra.segmentos:
        if segmento == cobra.cabeca:
            pass  # Ignora a própria cabeça
        elif cobra.cabeca.distance(segmento) < 10:
            jogo_ativo = False  # Encerra o jogo
            placar.fim_de_jogo()  # Exibe a mensagem de "Game Over"

# Fecha a tela ao clicar
tela.exitonclick()
