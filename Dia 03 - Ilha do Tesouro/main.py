# Exibe a arte inicial do jogo e o título
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')

# Mensagem de boas-vindas e introdução ao jogo
print("Bem vindos a ilha do Tesouro!")
print("Sua missão é encontrar o tesouro.")

# Primeira escolha do jogador
escolha1 = input("Você está em uma encruzilhada, para onde quer ir? DIREITA OU ESQUERDA? ").lower()

# Se a escolha for "ESQUERDA", o jogador é direcionado a uma segunda escolha
if escolha1 == "esquerda":
    # Segunda escolha: atravessar o lago ou esperar por um barco
    escolha2 = input("Você chegou a um lago. Há uma ilha no meio do lago. Digite ESPERAR para esperar por um barco. Digite NADAR para atravessar o lago. ").lower()

    # Se o jogador escolher esperar, há uma terceira escolha de portas
    if escolha2 == "esperar":
        escolha3 = input("Você chegou a ilha ileso. Há uma casa com 3 portas: 1 VERMELHA, 1 AMARELA e 1 AZUL. Qual delas você escolhe? ").lower()

        # Dependendo da porta escolhida, o jogo pode terminar ou o jogador pode vencer
        if escolha3 == "vermelha":
            print("É uma sala cheia de fogo. Você foi queimado. Fim de jogo.")
        elif escolha3 == "amarela":
            print("Você encontrou o tesouro. Você venceu!")
        elif escolha3 == "azul":
            print("Você entrou em uma sala de feras. Fim de jogo.")
        else:
            print("Você escolheu uma porta que nem existe. Fim de jogo.")
    else:
        # Se o jogador escolher nadar, ele será atacado por uma truta
        print("Você foi atacado por uma truta furiosa. Fim de jogo")
else:
    # Se o jogador escolher "DIREITA", ele cai em um buraco
    print("Você caiu em um buraco. Fim de jogo!")
