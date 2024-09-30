import time
from turtle import Screen
from jogador import Jogador  # Importa a classe Jogador do arquivo jogador.py
from gerenciar_carro import GerenciadorDeCarros  # Importa a classe GerenciadorDeCarros do arquivo gerenciar_carro.py
from placar import Placar  # Importa a classe Placar do arquivo placar.py

# Configura a tela do jogo
tela = Screen()
tela.setup(width=600, height=600)  # Define o tamanho da tela como 600x600 pixels
tela.tracer(0)  # Desativa o traço automático para atualizações mais suaves

# Cria instâncias dos objetos do jogo
jogador = Jogador()  # Cria um objeto Jogador
gerenciador_de_carros = GerenciadorDeCarros()  # Cria um objeto GerenciadorDeCarros
placar = Placar()  # Cria um objeto Placar

# Configura o controle do teclado
tela.listen()  # Configura a tela para escutar eventos do teclado
tela.onkey(jogador.mover_para_cima, "Up")  # Define que a tecla "Up" (seta para cima) move o jogador para cima

# Variável que controla o loop do jogo
jogo_ativo = True
while jogo_ativo:
    time.sleep(0.1)  # Faz uma pausa de 0.1 segundos para controlar a velocidade do loop
    tela.update()  # Atualiza a tela

    # Cria e move os carros
    gerenciador_de_carros.criar_carro()  # Cria novos carros com base em uma chance aleatória
    gerenciador_de_carros.mover_carros()  # Move todos os carros na tela

    # Detecta colisão com os carros
    for carro in gerenciador_de_carros.todos_os_carros:
        if carro.distance(jogador) < 20:  # Verifica se a distância entre o jogador e o carro é menor que 20
            jogo_ativo = False  # Termina o loop do jogo
            placar.jogo_acabou()  # Exibe a mensagem de "JOGO ACABOU" no placar

    # Detecta se o jogador cruzou a linha de chegada
    if jogador.esta_na_linha_de_chegada():
        jogador.voltar_para_inicio()  # Posiciona o jogador de volta à posição inicial
        gerenciador_de_carros.aumentar_nivel()  # Aumenta a velocidade dos carros
        placar.aumenta_nivel()  # Atualiza o placar com o novo nível

# Fecha a tela quando o usuário clicar nela
tela.exitonclick()
