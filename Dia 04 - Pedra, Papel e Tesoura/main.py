import random

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

imagem_do_jogo = [pedra, papel, tesoura]
escolha_usuario = int(input("Qual você escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura \n>> "))
if escolha_usuario >= 3 or escolha_usuario < 0 :
    print("Você digitou um número inválido. Você perdeu!")
else:
    print(imagem_do_jogo[escolha_usuario])


    escolha_computador = random.randint(0, 2)
    print("Computador escolhe:")
    print(imagem_do_jogo[escolha_computador])


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
