from tkinter import *  # Importa todos os widgets e funcionalidades do tkinter
import pandas  # Importa pandas para manipulação de dados
import random  # Importa random para selecionar cartões aleatoriamente

# Definindo a cor de fundo da interface
COR_FUNDO = "#B1DDC6"

# Inicializando variáveis globais
cartao_atual = {}  # Armazena o cartão atual exibido
para_aprender = {}  # Lista de palavras a aprender

# Tenta ler o arquivo de dados com palavras já aprendidas
try:
    dados = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Se o arquivo não for encontrado, carrega o arquivo original de palavras
    dados_originais = pandas.read_csv("data/french_words.csv")
    print(dados_originais)  # Imprime os dados originais no console para depuração
    # Converte os dados em uma lista de dicionários
    para_aprender = dados_originais.to_dict(orient="records")
else:
    # Se o arquivo de palavras a aprender existir, carrega os dados
    para_aprender = dados.to_dict(orient="records")

# Função para exibir o próximo cartão
def proximo_cartao():
    global cartao_atual, timer_inverter
    window.after_cancel(timer_inverter)  # Cancela o temporizador anterior
    cartao_atual = random.choice(para_aprender)  # Escolhe um cartão aleatório
    # Atualiza o texto do título e do corpo do cartão para o francês
    canvas.itemconfig(titulo_cartao, text="Francês", fill="black")
    canvas.itemconfig(palavra_cartao, text=cartao_atual["French"], fill="black")
    canvas.itemconfig(fundo_cartao, image=imagem_frente_cartao)  # Define a imagem da frente do cartão
    # Define um temporizador para inverter o cartão após 3 segundos
    timer_inverter = window.after(3000, func=inverter_cartao)

# Função para inverter o cartão e mostrar a tradução
def inverter_cartao():
    # Atualiza o texto do título e do corpo do cartão para o inglês
    canvas.itemconfig(titulo_cartao, text="Inglês", fill="white")
    canvas.itemconfig(palavra_cartao, text=cartao_atual["English"], fill="white")
    canvas.itemconfig(fundo_cartao, image=imagem_verso_cartao)  # Define a imagem do verso do cartão

# Função para marcar o cartão como conhecido
def conhecido():
    para_aprender.remove(cartao_atual)  # Remove o cartão atual da lista de aprendizado
    print(len(para_aprender))  # Imprime a quantidade de cartões restantes
    dados = pandas.DataFrame(para_aprender)  # Converte a lista em um DataFrame
    dados.to_csv("data/words_to_learn.csv", index=False)  # Salva os dados atualizados em um arquivo CSV
    proximo_cartao()  # Exibe o próximo cartão

# Configuração da interface gráfica com tkinter
window = Tk()
window.title("Flashy")  # Define o título da janela
window.config(padx=50, pady=50, bg=COR_FUNDO)  # Configura a margem e a cor de fundo da janela

# Configura um temporizador para inverter o cartão após 3 segundos
timer_inverter = window.after(3000, func=inverter_cartao)

# Cria um canvas para exibir o cartão
canvas = Canvas(width=800, height=526)
# Carrega as imagens dos cartões
imagem_frente_cartao = PhotoImage(file="images/card_front.png")
imagem_verso_cartao = PhotoImage(file="images/card_back.png")
# Adiciona a imagem de fundo no canvas
fundo_cartao = canvas.create_image(400, 263, image=imagem_frente_cartao)
# Adiciona o texto do título e do corpo do cartão no canvas
titulo_cartao = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
palavra_cartao = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# Configura o canvas
canvas.config(bg=COR_FUNDO, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Carrega as imagens dos botões
imagem_cruz = PhotoImage(file="images/wrong.png")
imagem_certo = PhotoImage(file="images/right.png")
# Cria os botões e os adiciona à janela
botao_desconhecido = Button(image=imagem_cruz, highlightthickness=0, command=proximo_cartao)
botao_desconhecido.grid(row=1, column=0)
botao_conhecido = Button(image=imagem_certo, highlightthickness=0, command=conhecido)
botao_conhecido.grid(row=1, column=1)

# Exibe o próximo cartão ao iniciar o aplicativo
proximo_cartao()

# Inicia o loop principal da interface gráfica
window.mainloop()
