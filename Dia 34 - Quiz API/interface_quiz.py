from tkinter import *
from controle_quiz import ControleQuiz

# Define a cor do tema da interface
COR_TEMA = "#375362"

class InterfaceQuiz:

    def __init__(self, controle_quiz: ControleQuiz):
        # Inicializa uma nova instância da interface de quiz
        self.quiz = controle_quiz

        # Cria a janela principal da interface
        self.tela = Tk()
        self.tela.title("Quizzler")  # Define o título da janela
        self.tela.config(padx=20, pady=20, bg=COR_TEMA)  # Define o preenchimento e a cor de fundo

        # Cria um rótulo para mostrar a pontuação
        self.rotulo_pontuacao = Label(text="Pontuação: 0", fg="white", bg=COR_TEMA)
        self.rotulo_pontuacao.grid(row=0, column=1)  # Posiciona o rótulo na grid

        # Cria um canvas para exibir as perguntas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Cria um texto no canvas para mostrar a pergunta
        self.texto_pergunta = self.canvas.create_text(
            150,  # Posição horizontal do texto
            125,  # Posição vertical do texto
            width=280,  # Largura do texto
            text="Texto da Pergunta",  # Texto padrão inicial
            fill=COR_TEMA,  # Cor do texto
            font=("Arial", 20, "italic")  # Fonte do texto
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # Posiciona o canvas na grid

        # Carrega a imagem para o botão "Verdadeiro"
        imagem_verdadeiro = PhotoImage(file="images/true.png")
        # Cria o botão "Verdadeiro" e associa a função verdadeiro_pressionado
        self.botao_verdadeiro = Button(image=imagem_verdadeiro, highlightthickness=0, command=self.verdadeiro_pressionado)
        self.botao_verdadeiro.grid(row=2, column=0)  # Posiciona o botão na grid

        # Carrega a imagem para o botão "Falso"
        imagem_falso = PhotoImage(file="images/false.png")
        # Cria o botão "Falso" e associa a função falso_pressionado
        self.botao_falso = Button(image=imagem_falso, highlightthickness=0, command=self.falso_pressionado)
        self.botao_falso.grid(row=2, column=1)  # Posiciona o botão na grid

        # Obtém a primeira pergunta para exibir
        self.obter_proxima_pergunta()

        # Inicia o loop principal da interface
        self.tela.mainloop()

    def obter_proxima_pergunta(self):
        # Atualiza o fundo do canvas para branco
        self.canvas.config(bg="white")
        # Verifica se ainda há perguntas para mostrar
        if self.quiz.ainda_tem_perguntas():
            # Atualiza o rótulo da pontuação com o valor atual
            self.rotulo_pontuacao.config(text=f"Pontuação: {self.quiz.pontuacao}")
            # Obtém a próxima pergunta
            texto_pergunta = self.quiz.proxima_pergunta()
            # Atualiza o texto da pergunta no canvas
            self.canvas.itemconfig(self.texto_pergunta, text=texto_pergunta)
        else:
            # Se não houver mais perguntas, exibe uma mensagem de fim de quiz
            self.canvas.itemconfig(self.texto_pergunta, text="Você chegou ao fim do quiz.")
            # Desativa os botões "Verdadeiro" e "Falso"
            self.botao_verdadeiro.config(state="disabled")
            self.botao_falso.config(state="disabled")

    def verdadeiro_pressionado(self):
        # Verifica se a resposta "Verdadeiro" está correta e dá feedback
        self.dar_feedback(self.quiz.verificar_resposta("True"))

    def falso_pressionado(self):
        # Verifica se a resposta "Falso" está correta e dá feedback
        resultado_correto = self.quiz.verificar_resposta("False")
        self.dar_feedback(resultado_correto)

    def dar_feedback(self, resposta_correta):
        # Atualiza a cor de fundo do canvas com base na resposta
        if resposta_correta:
            self.canvas.config(bg="green")  # Cor verde para resposta correta
        else:
            self.canvas.config(bg="red")  # Cor vermelha para resposta incorreta
        # Após 1 segundo, obtém a próxima pergunta
        self.tela.after(1000, self.obter_proxima_pergunta)
