from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# CONFIGURAÇÃO DO BANCO DE DADOS
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///livros.db"  # URI para o banco de dados SQLite
# Criar a extensão
db = SQLAlchemy(model_class=Base)
# Inicializa o aplicativo com a extensão
db.init_app(app)

# DEFINIÇÃO DA TABELA
class Livro(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # ID do livro, chave primária
    titulo: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Título do livro
    autor: Mapped[str] = mapped_column(String(250), nullable=False)  # Autor do livro
    avaliacao: Mapped[float] = mapped_column(Float, nullable=False)  # Avaliação do livro

# Cria o esquema da tabela no banco de dados. Necessita do contexto do aplicativo.
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # LER TODOS OS REGISTROS
    # Realiza uma consulta para selecionar todos os livros do banco de dados, ordenados pelo título
    resultado = db.session.execute(db.select(Livro).order_by(Livro.titulo))
    # Usa .scalars() para obter os elementos em vez de linhas inteiras do banco de dados
    todos_livros = resultado.scalars().all()
    return render_template("index.html", livros=todos_livros)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        # CRIAR UM NOVO REGISTRO
        novo_livro = Livro(
            titulo=request.form["titulo"],
            autor=request.form["autor"],
            avaliacao=request.form["avaliacao"]
        )
        db.session.add(novo_livro)  # Adiciona o novo livro à sessão
        db.session.commit()  # Salva as alterações no banco de dados
        return redirect(url_for('home'))  # Redireciona para a página inicial
    return render_template("add.html")  # Retorna o formulário de adição

@app.route("/editar", methods=["GET", "POST"])
def editar():
    if request.method == "POST":
        # ATUALIZAR UM REGISTRO
        livro_id = request.form["id"]  # Obtém o ID do livro a ser atualizado
        livro_para_atualizar = db.get_or_404(Livro, livro_id)  # Busca o livro ou retorna 404 se não encontrado
        livro_para_atualizar.avaliacao = request.form["avaliacao"]  # Atualiza a avaliação
        db.session.commit()  # Salva as alterações no banco de dados
        return redirect(url_for('home'))  # Redireciona para a página inicial
    livro_id = request.args.get('id')  # Obtém o ID do livro a partir da URL
    livro_selecionado = db.get_or_404(Livro, livro_id)  # Busca o livro ou retorna 404 se não encontrado
    return render_template("edit_rating.html", livro=livro_selecionado)  # Retorna o formulário de edição

@app.route("/deletar")
def deletar():
    livro_id = request.args.get('id')  # Obtém o ID do livro a ser deletado

    # DELETAR UM REGISTRO PELO ID
    livro_para_deletar = db.get_or_404(Livro, livro_id)  # Busca o livro ou retorna 404 se não encontrado
    db.session.delete(livro_para_deletar)  # Remove o livro da sessão
    db.session.commit()  # Salva as alterações no banco de dados
    return redirect(url_for('home'))  # Redireciona para a página inicial

if __name__ == "__main__":
    app.run(debug=True)  # Inicia o aplicativo em modo de depuração
