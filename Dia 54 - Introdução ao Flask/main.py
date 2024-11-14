# Importa a classe Flask do pacote flask. A classe Flask é a base do seu aplicativo web.
from flask import Flask

# Cria uma instância da classe Flask. Essa instância representa o aplicativo web.
app = Flask(__name__)

# Define uma rota para a URL raiz ('/'). Quando um usuário acessa essa URL, a função hello_world será chamada.
@app.route('/')
def hello_world():
    # Retorna a string 'Hello, World!' quando a URL raiz é acessada.
    return 'Hello, World!'

# Define uma nova rota para a URL '/bye'. Quando um usuário acessa essa URL, a função say_bye será chamada.
@app.route('/bye')
def say_bye():
    # Retorna a string 'Bye' quando a URL '/bye' é acessada.
    return 'Bye'

# Este bloco verifica se o arquivo está sendo executado diretamente (não importado como um módulo).
# Se estiver sendo executado diretamente, ele chama a função app.run().
if __name__ == "__main__":
    # Inicia o servidor Flask. Por padrão, ele escuta na porta 5000 e permite acesso de qualquer endereço IP (0.0.0.0).
    app.run()
