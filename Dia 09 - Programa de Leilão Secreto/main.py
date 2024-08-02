from logo import logo  # Importa o logo do leilão (supondo que haja um arquivo 'logo.py' com a variável 'logo')
import os

# Função para limpar a tela do console
def limpar_tela():
    # Verifica o sistema operacional para determinar o comando de limpeza adequado
    if os.name == 'posix':  # Se o sistema for Unix/Linux/MacOS/BSD/etc
        _ = os.system('clear')  # Usa 'clear' para limpar a tela
    elif os.name in ('nt', 'dos', 'ce'):  # Se o sistema for Windows
        _ = os.system('cls')  # Usa 'cls' para limpar a tela

print(logo)  # Imprime o logo do leilão

lances = {}  # Dicionário para armazenar os lances dos participantes
lance_concluído = False  # Variável de controle para indicar se o leilão foi concluído

def encontrar_maior_lance(registro_de_lance):
    # Função para encontrar o maior lance e determinar o vencedor
    lance_mais_alto = 0
    for licitante in registro_de_lance:  # Itera sobre cada licitante no registro de lances
        valor_lance = registro_de_lance[licitante]  # Obtém o valor do lance do licitante atual
        if valor_lance > lance_mais_alto:  # Verifica se o lance atual é maior que o maior lance registrado
            lance_mais_alto = valor_lance  # Atualiza o maior lance registrado
            vencedor = licitante  # Atualiza o licitante vencedor
    print(f"O vencedor é {vencedor}, com o lance de R${lance_mais_alto}!")  # Imprime o vencedor e o maior lance

# Loop que só vai parar quando lance_concluído for True.
while not lance_concluído: 
    nome = input("Qual é seu nome? ")  # Solicita o nome do participante
    lance = int(input("Qual é seu lance? R$"))  # Solicita o lance do participante e converte para inteiro
    lances[nome] = lance    # Adiciona o lance ao dicionário 'lances' com chave sendo o nome do participante
    
    deve_continuar = input("Há quem queira fazer outro lance? S ou N? \n").lower()  # Pergunta se há mais lances a serem feitos
    if deve_continuar == "n":
        lance_concluído = True  # Se a resposta for 'n', marca que o leilão está concluído

limpar_tela()  # Limpa a tela do console antes de exibir o resultado
encontrar_maior_lance(lances)  # Determina e exibe o vencedor do leilão com o maior lance registrado
