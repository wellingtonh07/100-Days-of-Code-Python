from flask import Flask, render_template, request  # Importa as bibliotecas necessárias do Flask
import smtplib  # Importa o módulo para enviar e-mails
import requests  # Importa o módulo para fazer requisições HTTP

app = Flask(__name__)  # Cria uma instância do aplicativo Flask

# Faz uma requisição para obter os posts de um endpoint JSON
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# Defina seu e-mail e senha
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"  # Substitua pelo seu endereço de e-mail
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"  # Substitua pela sua senha de e-mail

@app.route('/')  # Define a rota para a página inicial
def get_all_posts():
    return render_template("index.html", all_posts=posts)  # Renderiza o template com todos os posts

@app.route("/about")  # Define a rota para a página "Sobre"
def about():
    return render_template("about.html")  # Renderiza o template da página "Sobre"

@app.route("/contact", methods=["GET", "POST"])  # Define a rota para a página de contato
def contact():
    if request.method == "POST":  # Se o método da requisição for POST
        data = request.form  # Obtém os dados do formulário
        send_email(data["name"], data["email"], data["phone"], data["message"])  # Envia o e-mail
        return render_template("contact.html", msg_sent=True)  # Renderiza o template com mensagem de sucesso
    return render_template("contact.html", msg_sent=False)  # Renderiza o template sem mensagem

def send_email(name, email, phone, message):
    # Cria a mensagem de e-mail
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Conecta ao servidor SMTP do Gmail
        connection.starttls()  # Inicia a criptografia TLS
        connection.login(OWN_EMAIL, OWN_PASSWORD)  # Faz login com as credenciais fornecidas
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)  # Envia o e-mail

@app.route("/post/<int:index>")  # Define a rota para exibir um post específico
def show_post(index):
    requested_post = None  # Inicializa a variável para armazenar o post solicitado
    for blog_post in posts:  # Itera pelos posts
        if blog_post["id"] == index:  # Se o ID do post corresponder ao índice solicitado
            requested_post = blog_post  # Armazena o post solicitado
    return render_template("post.html", post=requested_post)  # Renderiza o template do post

if __name__ == "__main__":  # Se o script for executado diretamente
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
