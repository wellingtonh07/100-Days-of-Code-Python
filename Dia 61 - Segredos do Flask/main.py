# Importa as bibliotecas necessárias do Flask e do WTForms
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length  # Validações para os campos do formulário
from flask_bootstrap import Bootstrap5  # Para usar o Bootstrap com Flask

# Define a classe do formulário de login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])  # Campo de email, obrigatório
    password = PasswordField('Password', validators=[DataRequired()])  # Campo de senha, obrigatório
    submit = SubmitField(label="Log In")  # Botão de submissão

# Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"  # Chave secreta para sessões
bootstrap = Bootstrap5(app)  # Inicializa o Bootstrap5

# Rota principal da aplicação
@app.route("/")
def home():
    return render_template('index.html')  # Renderiza a página index.html

# Rota para o login
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()  # Cria uma instância do formulário de login
    if login_form.validate_on_submit():  # Verifica se o formulário foi submetido e é válido
        # Verifica as credenciais
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")  # Renderiza a página de sucesso
        else:
            return render_template("denied.html")  # Renderiza a página de acesso negado
    return render_template("login.html", form=login_form)  # Renderiza a página de login, passando o formulário

# Executa a aplicação se o script for chamado diretamente
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Inicia o servidor em modo de depuração na porta 5001
