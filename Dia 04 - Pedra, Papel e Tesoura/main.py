# Importa a biblioteca random para gerar a escolha do computador de forma aleatória
import random

# Representações visuais de Pedra, Papel e Tesoura
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lista que contém as representações das opções de Pedra, Papel e Tesoura
imagem_do_jogo = [pedra, papel, tesoura]

# Solicita ao usuário para escolher entre Pedra (0), Papel (1) ou Tesoura (2)
escolha_usuario = int(input("Qual você escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura \n>> "))

# Verifica se a escolha do usuário é válida (0, 1 ou 2)
if escolha_usuario >= 3 or escolha_usuario < 0:
    print("Você digitou um número inválido. Você perdeu!")
else:
    # Exibe a escolha do usuário
    print(imagem_do_jogo[escolha_usuario])

    # O computador faz uma escolha aleatória entre Pedra, Papel e Tesoura
    escolha_computador = random.randint(0, 2)
    print("Computador escolhe:")
    print(imagem_do_jogo[escolha_computador])

    # Verifica as condições de vitória, derrota ou empate
    if escolha_usuario == 0 and escolha_computador == 2:
        print("Você VENCEU!")
    elif escolha_computador == 0 and escolha_usuario == 2:
        print("VOCÊ PERDEU!")
    elif escolha_computador > escolha_usuario:
        print("Você PERDEU!")
    elif escolha_usuario > escolha_computador:
        print("Você VENCEU!")
    elif escolha_computador == escolha_usuario:
        print("É um EMPATE!")
