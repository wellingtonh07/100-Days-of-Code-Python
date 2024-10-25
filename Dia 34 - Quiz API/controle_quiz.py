# Define a classe ControleQuiz
class ControleQuiz:

    def __init__(self, lista_perguntas):
        # Inicializa uma nova instância da classe ControleQuiz
        self.numero_pergunta = 0
        self.pontuacao = 0
        self.lista_perguntas = lista_perguntas
        self.pergunta_atual = None

    def ainda_tem_perguntas(self):
        # Verifica se ainda há perguntas na lista
        return self.numero_pergunta < len(self.lista_perguntas)

    def proxima_pergunta(self):
        # Obtém a próxima pergunta e avança o contador
        self.pergunta_atual = self.lista_perguntas[self.numero_pergunta]
        self.numero_pergunta += 1
        texto_pergunta = self.pergunta_atual.texto
        return f"Q.{self.numero_pergunta}: {texto_pergunta}"

    def verificar_resposta(self, resposta_usuario):
        # Verifica se a resposta do usuário está correta
        resposta_correta = self.pergunta_atual.resposta
        if resposta_usuario.lower() == resposta_correta.lower():
            self.pontuacao += 1
            return True
        else:
            return False
