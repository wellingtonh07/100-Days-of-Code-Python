class QuizAnimal:
    def __init__(self):
        # Lista de perguntas e respostas
        self.perguntas_respostas = [
            {"pergunta": "Qual é o maior mamífero terrestre?", "resposta": "elefante"},
            {"pergunta": "Qual é o animal mais rápido do mundo?", "resposta": "guepardo"},
            {"pergunta": "Qual animal tem o coração maior em relação ao tamanho do corpo?", "resposta": "baleia"},
            {"pergunta": "Quantas patas tem um cavalo?", "resposta": "quatro"},
            {"pergunta": "Qual é o único mamífero que pode voar?", "resposta": "morcego"},
            {"pergunta": "Qual é o menor pássaro do mundo?", "resposta": "beija-flor"},
            {"pergunta": "Qual animal é conhecido por mudar de cor para se camuflar?", "resposta": "camaleão"},
            {"pergunta": "Qual é o animal mais pesado do mundo?", "resposta": "baleia-azul"},
            {"pergunta": "Qual é o animal mais venenoso do planeta?", "resposta": "medusa"},
            {"pergunta": "Qual é o único marsupial encontrado fora da Austrália?", "resposta": "coala"}
        ]
        # Contadores de acertos e erros
        self.acertos = 0
        self.erros = 0

    def fazer_perguntas(self):
        # Loop através de cada pergunta e coleta resposta do usuário
        for i, item in enumerate(self.perguntas_respostas):
            pergunta = item["pergunta"]
            resposta_correta = item["resposta"]
            resposta_usuario = input(f"Pergunta {i + 1}: {pergunta} ").strip().lower()
            
            # Verifica se a resposta do usuário está correta
            if resposta_usuario == resposta_correta:
                print("Resposta correta!")
                self.acertos += 1
            else:
                print(f"Resposta incorreta! A resposta correta é: {resposta_correta}")
                self.erros += 1

    def exibir_resultado(self):
        # Mostra o resultado final do quiz
        print(f"\nVocê teve {self.acertos} acertos e {self.erros} erros.")

# Criação de uma instância do quiz e execução
quiz = QuizAnimal()
quiz.fazer_perguntas()
quiz.exibir_resultado()
