from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# Chave da API do Movie DB
MOVIE_DB_API_KEY = "USE_YOUR_OWN_CODE"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# Criação da aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Criação do Banco de Dados
class Base(DeclarativeBase):
    pass

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Definição do modelo de tabela para os filmes
class Filme(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # ID do filme
    titulo: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Título do filme
    ano: Mapped[int] = mapped_column(Integer, nullable=False)  # Ano de lançamento
    descricao: Mapped[str] = mapped_column(String(500), nullable=False)  # Descrição do filme
    avaliacao: Mapped[float] = mapped_column(Float, nullable=True)  # Avaliação do filme
    classificacao: Mapped[int] = mapped_column(Integer, nullable=True)  # Classificação (ranking)
    comentario: Mapped[str] = mapped_column(String(250), nullable=True)  # Comentário do usuário
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # URL da imagem do filme

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Formulário para buscar filmes
class FormBuscarFilme(FlaskForm):
    titulo = StringField("Título do Filme", validators=[DataRequired()])
    submit = SubmitField("Adicionar Filme")

# Formulário para avaliar filmes
class FormAvaliarFilme(FlaskForm):
    avaliacao = StringField("Sua Avaliação (0 a 10, ex: 7.5)")
    comentario = StringField("Seu Comentário")
    submit = SubmitField("Concluído")

# Rota principal
@app.route("/")
def home():
    # Obtendo todos os filmes do banco de dados e ordenando pela avaliação
    resultado = db.session.execute(db.select(Filme).order_by(Filme.avaliacao))
    todos_filmes = resultado.scalars().all()  # Convertendo para uma lista Python

    # Atualizando a classificação de cada filme
    for i in range(len(todos_filmes)):
        todos_filmes[i].classificacao = len(todos_filmes) - i
    db.session.commit()  # Salvando as alterações

    return render_template("index.html", filmes=todos_filmes)

# Rota para adicionar um filme
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FormBuscarFilme()
    if form.validate_on_submit():  # Verifica se o formulário foi submetido corretamente
        titulo_filme = form.titulo.data
        # Fazendo a requisição à API para buscar o filme
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
            "api_key": MOVIE_DB_API_KEY, "query": titulo_filme})
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            dados = response.json()
            # Verifica se existe a chave "results" na resposta da API
            if "results" in dados:
                filmes_encontrados = dados["results"]
                return render_template("select.html", opcoes=filmes_encontrados)
            else:
                # Caso a chave "results" não seja encontrada
                return render_template("add.html", form=form, error="Nenhum filme encontrado.")
        else:
            # Caso a requisição não tenha sido bem-sucedida
            return render_template("add.html", form=form, error="Erro ao buscar filme na API.")
    
    return render_template("add.html", form=form)  # Renderiza o formulário

# Rota para encontrar um filme específico
@app.route("/find")
def find_movie():
    id_api_filme = request.args.get("id")
    if id_api_filme:
        # Fazendo a requisição à API para obter informações detalhadas do filme
        url_api_filme = f"{MOVIE_DB_INFO_URL}/{id_api_filme}"
        response = requests.get(url_api_filme, params={
            "api_key": MOVIE_DB_API_KEY, "language": "pt-BR"})
        dados = response.json()
        # Criando um novo objeto Filme e adicionando ao banco de dados
        novo_filme = Filme(
            titulo=dados["title"],
            ano=int(dados["release_date"].split("-")[0]),
            img_url=f"{MOVIE_DB_IMAGE_URL}{dados['poster_path']}",
            descricao=dados["overview"]
        )
        db.session.add(novo_filme)
        db.session.commit()
        return redirect(url_for("rate_movie", id=novo_filme.id))  # Redireciona para a página de avaliação

# Rota para editar (avaliar) um filme
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = FormAvaliarFilme()
    id_filme = request.args.get("id")
    filme = db.get_or_404(Filme, id_filme)  # Busca o filme no banco de dados
    if form.validate_on_submit():
        filme.avaliacao = float(form.avaliacao.data)
        filme.comentario = form.comentario.data
        db.session.commit()  # Salva as alterações
        return redirect(url_for('home'))  # Redireciona para a página principal
    return render_template("edit.html", filme=filme, form=form)  # Renderiza o formulário de avaliação

# Rota para deletar um filme
@app.route("/delete")
def delete_movie():
    id_filme = request.args.get("id")
    filme = db.get_or_404(Filme, id_filme)  # Busca o filme no banco de dados
    db.session.delete(filme)  # Remove o filme
    db.session.commit()  # Salva as alterações
    return redirect(url_for("home"))  # Redireciona para a página principal

# Execução da aplicação
if __name__ == '__main__':
    app.run(debug=True)
