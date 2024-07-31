import random
from forca_visual import forca_visual


palavras = ['Corinthians', 'Flamengo', 'Palmeiras', 'Fluminense', 'Gremio', 'Inter', 'Botafogo']


def escolher_palavra(palavras):
    """ Escolhe aleatoriamente uma palavra da lista """
    return random.choice(palavras)

def jogar_forca(palavra):
    """ Função principal para jogar o jogo da Forca """
    palavra = palavra.lower()  # Converte a palavra para minúsculas
    tentativas_restantes = 6   # Número de tentativas antes de perder o jogo
    letras_corretas = []       # Lista para armazenar letras corretas adivinhadas
    letras_incorretas = []     # Lista para armazenar letras incorretas adivinhadas

    # Loop principal do jogo. Só para de rodar quando ou o usuário ganhar, ou se errar todas.
    while tentativas_restantes > 0:
        # Mostra a arte visual da forca
        print(forca_visual[6 - tentativas_restantes])

        # Mostra o estado atual da palavra com letras adivinhadas. 
        #Vai aparecer _ enquanto não adicionar uma letra.
        palavra_escondida = ''.join(letra if letra in letras_corretas else '_' for letra in palavra)
        print(f'Palavra: {palavra_escondida}')

        # Mostra letras incorretas
        if letras_incorretas:
            print(f'Tentativas erradas: {", ".join(letras_incorretas)}')

        # Recebe uma tentativa do jogador
        tentativa = input('Digite uma letra: ').lower()

        # Verifica se a tentativa é válida
        if len(tentativa) != 1 or not tentativa.isalpha():
            print('Por favor, digite apenas uma letra válida.')
            continue

        # Verifica se a letra já foi tentada
        if tentativa in letras_corretas or tentativa in letras_incorretas:
            print('Você já tentou essa letra. Tente outra.')
            continue

        # Verifica se a letra está na palavra. Se não tiver, é 1 tentativa a menos.
        if tentativa in palavra:
            letras_corretas.append(tentativa)
        else:
            letras_incorretas.append(tentativa)
            tentativas_restantes -= 1

        # Verifica se o jogador ganhou
        if all(letra in letras_corretas for letra in palavra):
            print(f'Parabéns! Você ganhou! A palavra era "{palavra}".')
            break

    # Se as tentativas acabarem
    else:
        print(f'Você perdeu! A palavra era "{palavra}".')

# Função principal para iniciar o jogo
def main():
    print('Jogo da Forca')
    print('==============')
    palavra = escolher_palavra(palavras)
    jogar_forca(palavra)

if __name__ == "__main__":
    main()