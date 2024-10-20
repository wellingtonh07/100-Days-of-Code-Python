from tkinter import *  # Importa todos os widgets e funcionalidades do tkinter
import math  # Importa a biblioteca math para operações matemáticas

# Definindo cores e fontes
ROSA = "#e2979c"
VERMELHA = "#e7305b"
VERDE = "#9bdeac"
AMARELA = "#f7f5dd"
FONTE = "Courier"

# Definindo constantes para o temporizador
MIN_ESTUDADOS = 25  # Tempo em minutos para sessões de estudo
INTERVALO_MIN = 5  # Tempo em minutos para intervalos curtos
INTERVALO_MAX = 20  # Tempo em minutos para intervalos longos

# Variáveis globais
repeticoes = 0  # Contador de sessões de estudo e intervalos
cronometro = None  # Referência ao temporizador ativo

# Função para resetar o temporizador
def resetar():
    janela.after_cancel(cronometro)  # Cancela o temporizador ativo
    canvas.itemconfig(pomodoro_texto, text="00:00")  # Reseta o texto do temporizador para 00:00
    label_titulo.config(text="POMODORO")  # Reseta o título para "POMODORO"
    check_marca.config(text="")  # Limpa as marcas de sessões concluídas
    global repeticoes
    repeticoes = 0  # Reseta o contador de repetições

# Função para iniciar o temporizador
def iniciar():
    global repeticoes
    repeticoes += 1  # Incrementa o contador de repetições

    minutos_usados = MIN_ESTUDADOS  # Tempo padrão de estudo
    min_intervalo = INTERVALO_MIN  # Tempo padrão de intervalo curto
    max_intervalo = INTERVALO_MAX  # Tempo padrão de intervalo longo

    # Define o tipo de temporizador com base no número de repetições
    if repeticoes % 8 == 0:
        label_titulo.config(text="Intervalo", fg=VERMELHA)  # Intervalo longo
        contagem_regressiva(max_intervalo * 60)  # Converte minutos para segundos
    elif repeticoes % 2 == 0:
        label_titulo.config(text="Intervalo", fg=ROSA)  # Intervalo curto
        contagem_regressiva(min_intervalo * 60)  # Converte minutos para segundos
    else:
        label_titulo.config(text="Estudando", fg=VERDE)  # Sessão de estudo
        contagem_regressiva(minutos_usados * 60)  # Converte minutos para segundos

# Função para executar a contagem regressiva
def contagem_regressiva(contagem):
    contagem_minutos = math.floor(contagem / 60)  # Calcula os minutos restantes
    contagem_segundos = contagem % 60  # Calcula os segundos restantes
    if contagem_segundos < 10:
        contagem_segundos = f"0{contagem_segundos}"  # Adiciona um zero à frente dos segundos menores que 10

    canvas.itemconfig(pomodoro_texto, text=f"{contagem_minutos}:{contagem_segundos}")  # Atualiza o texto do temporizador
    if contagem > 0:
        global cronometro
        cronometro = janela.after(1000, contagem_regressiva, contagem - 1)  # Chama a função novamente após 1 segundo
    else:
        iniciar()  # Inicia o próximo ciclo (estudo ou intervalo)
        marcas = ""
        sessoes_estudadas = math.floor(repeticoes / 2)  # Calcula o número de sessões de estudo completas
        for _ in range(sessoes_estudadas):
            marcas += "✔"  # Adiciona uma marca para cada sessão concluída
        check_marca.config(text=marcas)  # Atualiza o rótulo com as marcas de sessões

# Configuração da interface gráfica com tkinter
janela = Tk()
janela.title("Pomodoro")  # Define o título da janela
janela.config(padx=100, pady=50, bg=AMARELA)  # Configura a margem e a cor de fundo da janela

# Cria e configura o rótulo do título
label_titulo = Label(text="POMODORO", fg=VERDE, bg=AMARELA, font=(FONTE, 50))
label_titulo.grid(column=1, row=0)

# Cria um canvas para exibir o temporizador
canvas = Canvas(width=200, height=224, bg=AMARELA, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")  # Carrega a imagem do tomate
canvas.create_image(103, 112, image=pomodoro_img)  # Adiciona a imagem ao canvas
pomodoro_texto = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONTE, 35, "bold"))
canvas.grid(column=1, row=1)

# Cria e configura o botão de iniciar
botao_iniciar = Button(text="Iniciar", highlightthickness=0, command=iniciar)
botao_iniciar.grid(column=0, row=2)

# Cria e configura o botão de resetar
botao_resetar = Button(text="Resetar", highlightthickness=0, command=resetar)
botao_resetar.grid(column=2, row=2)

# Cria o rótulo para exibir as marcas de sessões concluídas
check_marca = Label(fg=VERDE, bg=AMARELA)
check_marca.grid(column=1, row=3)

# Inicia o loop principal da interface gráfica
janela.mainloop()
