import turtle
import random

# Função para configurar a tartaruga
def configurar_tartaruga(tartaruga, cor, posicao_x, posicao_y):
    tartaruga.shape("turtle")  # Define a forma da tartaruga como uma tartaruga
    tartaruga.color(cor)  # Define a cor da tartaruga
    tartaruga.penup()  # Levanta o lápis para que a tartaruga não desenhe ao se mover
    tartaruga.goto(posicao_x, posicao_y)  # Posiciona a tartaruga nas coordenadas especificadas

# Função para a corrida
def corrida(tartarugas):
    # Move cada tartaruga aleatoriamente
    while True:
        for tartaruga in tartarugas:
            movimento = random.randint(1, 10)  # Gera um movimento aleatório entre 1 e 10
            tartaruga.forward(movimento)  # Move a tartaruga para frente

            # Verifica se alguma tartaruga cruzou a linha de chegada
            if tartaruga.xcor() >= 250:  # A linha de chegada está na coordenada x = 250
                return tartaruga  # Retorna a tartaruga vencedora

# Configuração da tela
tela = turtle.Screen()
tela.title("Corrida de Tartarugas")
tela.setup(width=600, height=400)  # Configura o tamanho da tela

# Lista para armazenar as tartarugas
tartarugas = []

# Cores e posições iniciais das tartarugas
cores = ["red", "green", "blue", "orange", "purple"]  # Cores em inglês
posicoes_x = [-250] * 5  # Todas as tartarugas começam na mesma posição x
posicoes_y = [-100, -50, 0, 50, 100]  # Posições y diferentes para as tartarugas

# Criação e configuração das tartarugas
for i in range(5):
    nova_tartaruga = turtle.Turtle()
    configurar_tartaruga(nova_tartaruga, cores[i], posicoes_x[i], posicoes_y[i])
    tartarugas.append(nova_tartaruga)

# Inicia a corrida
vencedora = corrida(tartarugas)

# Exibe o resultado no console
print(f"A tartaruga {vencedora.color()[0]} venceu!")

# Fecha a janela
tela.bye()
