import random

def criar_baralho():
    """Cria um baralho padrão de 52 cartas."""
    naipes = ['♠', '♣', '♥', '♦']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [{'valor': valor, 'naipe': naipe} for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

def calcular_total(mao):
    """Calcula o valor total de uma mão de cartas."""
    total = 0
    num_as = 0
    for carta in mao:
        if carta['valor'] in ['J', 'Q', 'K']:
            total += 10
        elif carta['valor'] == 'A':
            num_as += 1
            total += 11
        else:
            total += int(carta['valor'])
    
    while total > 21 and num_as > 0:
        total -= 10
        num_as -= 1
    
    return total

def imprimir_mao(mao, esconder_primeira_carta=False):
    """Imprime a mão de um jogador ou da casa."""
    if esconder_primeira_carta:
        print(f"Cartas: [{'??'}", end='')
        for carta in mao[1:]:
            print(f", {carta['valor']}{carta['naipe']}", end='')
    else:
        print(f"Cartas: [{mao[0]['valor']}{mao[0]['naipe']}", end='')
        for carta in mao[1:]:
            print(f", {carta['valor']}{carta['naipe']}", end='')
    print(f"], Total: {calcular_total(mao)}")

def jogar_blackjack():
    """Função principal para jogar blackjack."""
    baralho = criar_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_casa = [baralho.pop(), baralho.pop()]

    print("\nBem-vindo ao Blackjack!\n")
    print("Sua mão:")
    imprimir_mao(mao_jogador)
    print("\nMão da casa:")
    imprimir_mao(mao_casa, esconder_primeira_carta=True)

    if calcular_total(mao_jogador) == 21:
        print("\nVocê tem Blackjack! Você ganhou!")
        return

    while True:
        escolha = input("\nVocê quer 'pedir' mais uma carta ou 'ficar' com sua mão? (pedir/ficar): ").lower()
        if escolha == 'pedir':
            mao_jogador.append(baralho.pop())
            print("\nSua mão:")
            imprimir_mao(mao_jogador)
            if calcular_total(mao_jogador) > 21:
                print("\nVocê estourou! Você perdeu.")
                return
        elif escolha == 'ficar':
            break
        else:
            print("Escolha inválida! Por favor, escolha 'pedir' ou 'ficar'.")

    print("\nMão da casa:")
    imprimir_mao(mao_casa)

    while calcular_total(mao_casa) < 17:
        mao_casa.append(baralho.pop())
        print("\nMão da casa:")
        imprimir_mao(mao_casa)
        if calcular_total(mao_casa) > 21:
            print("\nA casa estourou! Você ganhou!")
            return

    total_jogador = calcular_total(mao_jogador)
    total_casa = calcular_total(mao_casa)

    print("\nSua mão:")
    imprimir_mao(mao_jogador)
    print("\nMão da casa:")
    imprimir_mao(mao_casa)

    if total_jogador > total_casa:
        print("\nVocê ganhou!")
    elif total_jogador < total_casa:
        print("\nVocê perdeu.")
    else:
        print("\nEmpate!")

if __name__ == "__main__":
    jogar_blackjack()
