from flask import Flask, render_template  # Importa as bibliotecas Flask e render_template
import requests  # Importa a biblioteca requests para fazer requisições HTTP

# Faz uma requisição GET para uma API e armazena o resultado em 'posts'
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)  # Cria uma instância da aplicação Flask

# Rota principal que exibe todos os posts
@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)  # Renderiza o template index.html e passa os posts

# Rota que exibe informações sobre a aplicação
@app.route("/about")
def about():
    return render_template("about.html")  # Renderiza o template about.html

# Rota de contato
@app.route("/contact")
def contact():
    return render_template("contact.html")  # Renderiza o template contact.html

# Rota que exibe um post específico com base no índice
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None  # Inicializa a variável para armazenar o post solicitado
    for blog_post in posts:  # Itera sobre todos os posts
        if blog_post["id"] == index:  # Verifica se o ID do post corresponde ao índice solicitado
            requested_post = blog_post  # Armazena o post solicitado
    return render_template("post.html", post=requested_post)  # Renderiza o template post.html e passa o post encontrado

# Executa a aplicação Flask se o script for chamado diretamente
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Inicia o servidor Flask em modo debug na porta 5001
