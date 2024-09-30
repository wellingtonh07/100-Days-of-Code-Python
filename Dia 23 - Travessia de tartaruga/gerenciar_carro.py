from turtle import Turtle
import random

# Define as cores disponíveis para os carros
CORES = ["red", "orange", "yellow", "green", "blue", "purple"]
DISTANCIA_INICIAL_MOVIMENTO = 5
INCREMENTO_MOVIMENTO = 10

class GerenciadorDeCarros:
    # Inicializa a classe GerenciadorDeCarros
    def __init__(self):
        self.todos_os_carros = []  # Lista que armazenará todos os carros
        self.velocidade_dos_carros = DISTANCIA_INICIAL_MOVIMENTO  # Define a velocidade inicial dos carros

    # Cria um novo carro com base em uma chance aleatória
    def criar_carro(self):
        chance_aleatoria = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
        if chance_aleatoria == 1:  # Há uma chance de 1 em 6 de criar um carro
            novo_carro = Turtle("square")  # Cria um novo carro com forma de quadrado
            novo_carro.shapesize(stretch_wid=1, stretch_len=2)  # Define o tamanho do carro
            novo_carro.penup()  # Levanta a caneta para não desenhar linhas
            novo_carro.color(random.choice(CORES))  # Define uma cor aleatória para o carro
            random_y = random.randint(-250, 250)  # Gera uma coordenada Y aleatória
            novo_carro.goto(300, random_y)  # Posiciona o carro na coordenada X = 300 e Y aleatória
            self.todos_os_carros.append(novo_carro)  # Adiciona o novo carro à lista de carros

    # Move todos os carros para trás com a velocidade atual
    def mover_carros(self):
        for carro in self.todos_os_carros:  # Itera sobre todos os carros na lista
            carro.backward(self.velocidade_dos_carros)  # Move o carro para trás pela distância da velocidade

    # Aumenta a velocidade dos carros
    def aumentar_nivel(self):
        self.velocidade_dos_carros += INCREMENTO_MOVIMENTO  # Incrementa a velocidade dos carros
