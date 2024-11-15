from flask import Flask
import random

# Gera um número aleatório entre 0 e 9
random_number = random.randint(0, 9)
print(random_number)  # Imprime o número aleatório no console

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    # Retorna uma mensagem de boas-vindas e uma imagem
    return "<h1>Adivinhe um número entre 0 e 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

# Rota para receber o palpite do usuário
@app.route("/<int:guess>")
def guess_number(guess):
    # Compara o palpite do usuário com o número aleatório
    if guess > random_number:
        # Se o palpite for maior que o número aleatório
        return "<h1 style='color: purple'>Muito alto, tente novamente!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    
    elif guess < random_number:
        # Se o palpite for menor que o número aleatório
        return "<h1 style='color: red'>Muito baixo, tente novamente!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    
    else:
        # Se o palpite estiver correto
        return "<h1 style='color: green'>Você me encontrou!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

# Executa o aplicativo se este arquivo for o principal
if __name__ == "__main__":
    app.run(debug=True)  # O aplicativo roda em modo de depuração
