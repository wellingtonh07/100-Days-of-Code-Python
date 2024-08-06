import random

# Dados fictícios de seguidores no Instagram
celebridades = [
    {"nome": "Cristiano Ronaldo", "seguidores": 400000000},
    {"nome": "Beyoncé", "seguidores": 250000000},
    {"nome": "Lionel Messi", "seguidores": 350000000},
    {"nome": "Taylor Swift", "seguidores": 300000000},
    {"nome": "Neymar Jr", "seguidores": 200000000},
    {"nome": "Ariana Grande", "seguidores": 280000000},
]

def jogo_maior_ou_menor():
    print("Bem-vindo ao jogo Maior ou Menor!")
    print("Você vai escolher quem tem mais seguidores no Instagram.")
    print("Vamos começar!\n")
    
    pontuacao = 0
    continuar_jogando = True
    
    while continuar_jogando:
        # Escolhe aleatoriamente duas celebridades
        celebridade1 = random.choice(celebridades)
        celebridade2 = random.choice(celebridades)
        
        # Garante que as duas celebridades escolhidas são diferentes
        while celebridade1 == celebridade2:
            celebridade2 = random.choice(celebridades)
        
        print(f"Quem tem mais seguidores no Instagram?")
        print(f"1. {celebridade1['nome']}")
        print(f"2. {celebridade2['nome']}")
        
        # Recebe a escolha do jogador
        escolha = input("Escolha 1 ou 2 (ou 'q' para sair): ").lower()
        
        if escolha == 'q':
            continuar_jogando = False
            print("Obrigado por jogar!")
            break
        
        if escolha == '1' or escolha == '2':
            celebridade_escolhida = celebridade1 if escolha == '1' else celebridade2
            outra_celebridade = celebridade2 if escolha == '1' else celebridade1
            
            if celebridade_escolhida['seguidores'] > outra_celebridade['seguidores']:
                print(f"Correto! {celebridade_escolhida['nome']} tem mais seguidores do que {outra_celebridade['nome']}.")
                pontuacao += 1
            else:
                print(f"Incorreto! {celebridade_escolhida['nome']} tem menos seguidores do que {outra_celebridade['nome']}.")
            
            print(f"Pontuação atual: {pontuacao}\n")
        else:
            print("Escolha inválida. Por favor, escolha 1 ou 2.")

# Iniciar o jogo
jogo_maior_ou_menor()
