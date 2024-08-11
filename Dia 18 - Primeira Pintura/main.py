# Importando pacotes
import turtle as turtle_module      
import random

# Configurando a cor do módulo tartaruga
turtle_module.colormode(255)    

# Criando uma tartaruga e configurando suas propriedades
tim = turtle_module.Turtle()    
tim.speed("fastest")  # Define a velocidade da tartaruga
tim.penup()           # Levanta o lápis para não desenhar enquanto se move
tim.hideturtle()     # Oculta a tartaruga

# Lista de cores a serem usadas nos pontos
lista_de_cores = [
    (229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), 
    (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), 
    (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), 
    (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), 
    (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), 
    (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), 
    (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), 
    (46, 73, 62), (47, 66, 82)
]

# Inicializando a posição da tartaruga para começar a pintura no centro
tim.setheading(225)     # Define o cabeçalho para baixo à esquerda
tim.forward(300)        # Move a tartaruga para baixo
tim.setheading(0)       # Define o cabeçalho para a direita

numero_de_pontos = 100  # Número total de pontos a serem desenhados

# Loop para criar pontos
for contador_de_pontos in range(1, numero_de_pontos + 1):
    # Desenha um ponto com cor aleatória da lista de cores
    tim.dot(20, random.choice(lista_de_cores))
    tim.forward(50)  # Move a tartaruga para frente

    # Verifica a cada 10 pontos se precisa mover para uma nova linha
    if contador_de_pontos % 10 == 0:
        tim.setheading(90)   # Define o cabeçalho para cima
        tim.forward(50)      # Move a tartaruga para cima
        tim.setheading(180)  # Define o cabeçalho para a esquerda
        tim.forward(500)     # Move a tartaruga para a esquerda
        tim.setheading(0)    # Define o cabeçalho para a direita

# Cria uma tela que só será fechada quando clicar no 'x'
tela = turtle_module.Screen()
tela.exitonclick()
