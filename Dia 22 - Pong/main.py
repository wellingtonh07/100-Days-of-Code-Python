from turtle import Screen
from raquete import Raquete
from bola import Bola
from pontuação import Placar
import time

# Configuração da tela
tela = Screen()
tela.bgcolor("black")  # Define a cor de fundo da tela como preta
tela.setup(width=800, height=600)  # Define o tamanho da tela (800x600 pixels)
tela.title("Pong")  # Define o título da janela
tela.tracer(0)  # Desativa a atualização automática da tela para melhorar o desempenho

# Criação das raquetes
raquete_direita = Raquete((350, 0))  # Raquete da direita
raquete_esquerda = Raquete((-350, 0))  # Raquete da esquerda

# Criação da bola
bola = Bola()

# Criação do placar
placar = Placar()

# Configuração dos controles do teclado
tela.listen()  # Habilita a captura de eventos do teclado
tela.onkeypress(raquete_direita.sobe, "Up")  # Configura a tecla "Up" para mover a raquete da direita para cima
tela.onkeypress(raquete_direita.desce, "Down")  # Configura a tecla "Down" para mover a raquete da direita para baixo
tela.onkeypress(raquete_esquerda.sobe, "w")  # Configura a tecla "w" para mover a raquete da esquerda para cima
tela.onkeypress(raquete_esquerda.desce, "s")  # Configura a tecla "s" para mover a raquete da esquerda para baixo
tela.onkeyrelease(raquete_direita.parar, "Up")  # Configura o evento de soltar a tecla "Up" para parar o movimento da raquete da direita
tela.onkeyrelease(raquete_direita.parar, "Down")  # Configura o evento de soltar a tecla "Down" para parar o movimento da raquete da direita
tela.onkeyrelease(raquete_esquerda.parar, "w")  # Configura o evento de soltar a tecla "w" para parar o movimento da raquete da esquerda
tela.onkeyrelease(raquete_esquerda.parar, "s")  # Configura o evento de soltar a tecla "s" para parar o movimento da raquete da esquerda

jogo_ativo = True  # Inicializa a variável de controle do jogo

while jogo_ativo:
    tela.update()  # Atualiza a tela
    bola.mover()  # Move a bola
    raquete_direita.mover()  # Move a raquete da direita se necessário
    raquete_esquerda.mover()  # Move a raquete da esquerda se necessário

    # Detecta colisão com a parede superior ou inferior
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.quicar_y()  # Faz a bola quicar verticalmente

    # Detecta colisão com as raquetes
    if (bola.distance(raquete_direita) < 50 and bola.xcor() > 320) or (bola.distance(raquete_esquerda) < 50 and bola.xcor() < -320):
        bola.quicar_x()  # Faz a bola quicar horizontalmente

    # Detecta se a raquete da direita (raquete_direita) não conseguiu alcançar a bola
    if bola.xcor() > 380:
        bola.resetar_posicao()  # Reseta a posição da bola para o centro
        placar.ponto_esquerda()  # Adiciona um ponto ao placar da esquerda

    # Detecta se a raquete da esquerda (raquete_esquerda) não conseguiu alcançar a bola
    if bola.xcor() < -380:
        bola.resetar_posicao()  # Reseta a posição da bola para o centro
        placar.ponto_direita()  # Adiciona um ponto ao placar da direita

# Mantém a janela aberta até que o usuário clique nela
tela.exitonclick()
