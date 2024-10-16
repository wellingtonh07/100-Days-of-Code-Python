import turtle

# Função para adicionar o nome do estado no mapa
def adicionar_estado(nome, posicao):
    t.penup()  # Levanta o lápis para mover sem desenhar
    t.goto(posicao)  # Move a tartaruga para a posição especificada
    t.pendown()  # Abaixa o lápis para começar a desenhar
    t.write(nome, align="center", font=("Arial", 10, "normal"))  # Escreve o nome do estado na posição

# Função para mostrar uma mensagem temporária
def mensagem_temporaria(mensagem, posicao, tempo=2000):
    t_temp.penup()  # Levanta o lápis para mover sem desenhar
    t_temp.goto(posicao)  # Move a tartaruga para a posição especificada
    t_temp.pendown()  # Abaixa o lápis para começar a desenhar
    t_temp.write(mensagem, align="center", font=("Arial", 12, "normal"))  # Exibe a mensagem
    tela.ontimer(lambda: t_temp.clear(), tempo)  # Limpa a mensagem após o tempo especificado

# Configuração da tela
tela = turtle.Screen()
tela.title("Mapa do Brasil")  # Define o título da janela
tela.bgcolor("white")  # Define a cor de fundo da tela

# Ajusta o tamanho da tela para corresponder ao tamanho da imagem
tela.setup(width=800, height=600)  # Define o tamanho da tela para 800x600 pixels

# Registra a imagem para usar como fundo
tela.bgpic("mapa_brasil.gif")  # Define a imagem de fundo do mapa do Brasil

# Criação da tartaruga principal para desenhar sobre a imagem
t = turtle.Turtle()
t.speed(0)  # Define a velocidade máxima de desenho
t.hideturtle()  # Esconde a tartaruga para que a imagem de fundo seja visível

# Criação da tartaruga para mensagens temporárias
t_temp = turtle.Turtle()
t_temp.hideturtle()  # Esconde a tartaruga de mensagens temporárias
t_temp.penup()  # Levanta o lápis para mover sem desenhar

# Lista de estados e suas posições ajustadas para uma imagem de 800x600 pixels
estados = {
    "Acre": (-250, 70),
    "Alagoas": (280, 50),
    "Amapá": (40, 220),
    "Amazonas": (-140, 120),
    "Bahia": (190, 30),
    "Ceará": (220, 110),
    "Espírito Santo": (240, -90),
    "Goiás": (60, -30),
    "Maranhão": (130, 120),
    "Mato Grosso": (-30, 30),
    "Mato Grosso do Sul": (-30, -90),
    "Minas Gerais": (150, -60),
    "Pará": (20, 120),
    "Paraíba": (280, 90),
    "Paraná": (40, -160),
    "Pernambuco": (280, 70),
    "Piauí": (190, 110),
    "Rio de Janeiro": (220, -130),
    "Rio Grande do Norte": (310, 110),
    "Rio Grande do Sul": (60, -240),
    "Rondônia": (-140, 50),
    "Roraima": (-100, 220),
    "Santa Catarina": (60, -200),
    "São Paulo": (70, -130),
    "Sergipe": (270, 30),
    "Tocantins": (80, 30)
}

# Inicializa variáveis para controle de erros e estados acertados
erros = 0  # Contador de erros
estados_acertados = set(estados.keys())  # Conjunto de estados que ainda precisam ser acertados

# Mensagem inicial para o usuário
t.penup()  # Levanta o lápis para mover sem desenhar
t.goto(0, 250)  # Move a tartaruga para a posição inicial
t.write("Digite o nome de um estado para preenchê-lo no mapa!", align="center", font=("Arial", 16, "bold"))  # Exibe a mensagem inicial

# Loop para interação com o usuário
while estados_acertados:
    resposta = turtle.textinput("Adivinhe o Estado", "Digite o nome de um estado:").strip()  # Solicita a entrada do usuário e remove espaços extras
    if resposta:
        posicao = estados.get(resposta)  # Obtém a posição do estado digitado
        if posicao:
            adicionar_estado(resposta, posicao)  # Adiciona o nome do estado no mapa
            estados_acertados.discard(resposta)  # Remove o estado da lista de estados acertados
            if not estados_acertados:  # Verifica se todos os estados foram acertados
                t.penup()  # Levanta o lápis para mover sem desenhar
                t.goto(0, 0)  # Move a tartaruga para a posição central
                t.write("Você ganhou!", align="center", font=("Arial", 24, "bold"))  # Exibe a mensagem de vitória
                break  # Sai do loop
        else:
            erros += 1  # Incrementa o contador de erros
            mensagem_temporaria("Estado não encontrado. Tente novamente!", (0, -250))  # Exibe mensagem de erro temporária
            if erros >= 3:  # Verifica se o número de erros alcançou o limite
                t.penup()  # Levanta o lápis para mover sem desenhar
                t.goto(0, 0)  # Move a tartaruga para a posição central
                t.write("Fim de jogo!", align="center", font=("Arial", 24, "bold"))  # Exibe a mensagem de fim de jogo
                break  # Sai do loop

# Mantém a tela aberta até o usuário fechá-la
tela.mainloop()
