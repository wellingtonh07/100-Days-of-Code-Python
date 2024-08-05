import random

def jogo_adivinhacao():
    # Escolhe um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10  # Definimos um máximo de 10 tentativas para o jogador
    
    print("Olá! Vamos jogar o jogo da adivinhação.")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    # Loop principal do jogo.
    #Vai rodar até chegar a 10 tentativas.
    while tentativas < max_tentativas:
        # Solicita um palpite ao jogador
        tentativa = int(input("\nDigite o seu palpite: "))

        tentativas += 1  # Incrementa o número de tentativas

        # Verifica se o palpite é maior, menor ou igual ao número secreto
        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            # Se o palpite for correto, mostra uma mensagem de parabéns e encerra o jogo
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativa(s).")
            break
    
    # Caso o jogador não tenha acertado após todas as tentativas
    if tentativa != numero_secreto:
        print(f"\nSuas {max_tentativas} tentativas acabaram. O número secreto era {numero_secreto}. Tente novamente!")

    # Pergunta se o jogador deseja jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's' or jogar_novamente == 'sim':
        jogo_adivinhacao()  # Reinicia o jogo
    else:
        print("\nObrigado por jogar!")  # Encerra o programa

# Início do jogo
jogo_adivinhacao()
