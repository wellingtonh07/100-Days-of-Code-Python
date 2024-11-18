from flask import Flask, render_template  # Importa Flask para criar a aplicação e render_template para renderizar arquivos HTML
from post import Post  # Importa a classe Post do arquivo post.py, que representa um post de blog
import requests  # Importa a biblioteca requests para fazer requisições HTTP

# Faz uma requisição GET para a API e armazena a resposta em formato JSON
response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
print(response)  # Imprime a resposta da API no console para verificar seu conteúdo

post_objects = []  # Inicializa uma lista vazia que armazenará objetos Post

# Verifica se a resposta é um dicionário e se contém a chave 'job_posting'
if isinstance(response, dict) and 'job_posting' in response:
    # Se 'job_posting' é uma string, cria um objeto Post com um ID fixo e adiciona à lista
    post_obj = Post(1, "Anúncio de Emprego", "Subtítulo", response['job_posting'])
    post_objects.append(post_obj)  # Adiciona o objeto Post à lista post_objects
else:
    # Se a resposta não está no formato esperado, imprime o tipo de dado retornado
    print("Formato inesperado:", type(response))

app = Flask(__name__)  # Cria uma instância da aplicação Flask

# Define a rota para a página inicial
@app.route('/')
def get_all_posts():
    # Renderiza o template "index.html" e passa a lista de todos os posts para ele
    return render_template("index.html", all_posts=post_objects)

# Define a rota para mostrar um post específico com base no índice
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None  # Inicializa a variável para armazenar o post solicitado
    # Itera sobre os objetos de post para encontrar o que corresponde ao índice fornecido
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post  # Se encontrado, armazena o post solicitado
    # Renderiza o template "post.html" e passa o post solicitado para ele
    return render_template("post.html", post=requested_post)

# Inicia a aplicação Flask se o arquivo for executado diretamente
if __name__ == "__main__":
    app.run(debug=True)  # Executa o servidor Flask em modo de debug para facilitar o desenvolvimento
