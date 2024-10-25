# Importa a classe Pergunta do módulo pergunta_modelo
from pergunta_modelo import Pergunta

# Importa os dados de perguntas do módulo dados
from dados import dados_perguntas

# Importa a classe ControleQuiz do módulo controle_quiz
from controle_quiz import ControleQuiz

# Importa a classe InterfaceQuiz do módulo interface_quiz
from interface_quiz import InterfaceQuiz

# Cria uma lista vazia para armazenar as perguntas
banco_perguntas = []

# Percorre cada item na lista de dados de perguntas
for pergunta in dados_perguntas:
    # Obtém o texto da pergunta
    texto_pergunta = pergunta["question"]
    # Obtém a resposta correta para a pergunta
    resposta_correta = pergunta["correct_answer"]
    # Cria uma nova instância da classe Pergunta com o texto e a resposta
    nova_pergunta = Pergunta(texto_pergunta, resposta_correta)
    # Adiciona a nova pergunta à lista banco_perguntas
    banco_perguntas.append(nova_pergunta)

# Cria uma instância da classe ControleQuiz, passando a lista de perguntas
controle_quiz = ControleQuiz(banco_perguntas)

# Cria uma instância da classe InterfaceQuiz, passando a instância do ControleQuiz
interface_quiz = InterfaceQuiz(controle_quiz)
