from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Chave secreta para formulários seguros
ckeditor = CKEditor(app)  # Inicializa o CKEditor para edição de texto
Bootstrap5(app)  # Inicializa o Bootstrap para estilização

# CRIA O BANCO DE DADOS
class Base(DeclarativeBase):
    pass

# Configura a URI do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# Inicializa o SQLAlchemy com a classe base definida
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURA A TABELA
class PostagemBlog(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Identificador único da postagem
    titulo: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Título da postagem
    subtitulo: Mapped[str] = mapped_column(String(250), nullable=False)  # Subtítulo da postagem
    data: Mapped[str] = mapped_column(String(250), nullable=False)  # Data da postagem
    corpo: Mapped[str] = mapped_column(Text, nullable=False)  # Conteúdo da postagem
    autor: Mapped[str] = mapped_column(String(250), nullable=False)  # Nome do autor
    url_imagem: Mapped[str] = mapped_column(String(250), nullable=False)  # URL da imagem

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

# FORMULÁRIO WTForms
class CriarPostagemForm(FlaskForm):
    titulo = StringField("Título da Postagem", validators=[DataRequired()])  # Campo para o título
    subtitulo = StringField("Subtítulo", validators=[DataRequired()])  # Campo para o subtítulo
    autor = StringField("Seu Nome", validators=[DataRequired()])  # Campo para o autor
    url_imagem = StringField("URL da Imagem do Blog", validators=[DataRequired(), URL()])  # Campo para a URL da imagem
    corpo = CKEditorField("Conteúdo do Blog", validators=[DataRequired()])  # Campo para o conteúdo com editor de texto
    submit = SubmitField("Enviar Postagem")  # Botão de envio

# Rota para obter todas as postagens
@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(PostagemBlog))  # Seleciona todas as postagens
    postagens = result.scalars().all()  # Obtém todas as postagens como uma lista
    return render_template("index.html", all_posts=postagens)  # Renderiza o template com as postagens

# Rota para exibir uma postagem específica
@app.route("/post/<int:post_id>")
def show_post(post_id):
    postagem_desejada = db.get_or_404(PostagemBlog, post_id)  # Obtém a postagem ou retorna 404 se não encontrada
    return render_template("post.html", post=postagem_desejada)  # Renderiza o template da postagem

# Rota para adicionar uma nova postagem
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CriarPostagemForm()  # Cria uma instância do formulário
    if form.validate_on_submit():  # Verifica se o formulário foi enviado e é válido
        nova_postagem = PostagemBlog(
            titulo=form.titulo.data,
            subtitulo=form.subtitulo.data,
            corpo=form.corpo.data,
            url_imagem=form.url_imagem.data,
            autor=form.autor.data,
            data=date.today().strftime("%B %d, %Y")  # Define a data atual
        )
        db.session.add(nova_postagem)  # Adiciona a nova postagem à sessão
        db.session.commit()  # Salva as alterações no banco de dados
        return redirect(url_for("get_all_posts"))  # Redireciona para a página de todas as postagens
    return render_template("make-post.html", form=form)  # Renderiza o formulário para nova postagem

# Rota para editar uma postagem existente
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    postagem = db.get_or_404(PostagemBlog, post_id)  # Obtém a postagem ou retorna 404 se não encontrada
    formulario_edicao = CriarPostagemForm(
        titulo=postagem.titulo,
        subtitulo=postagem.subtitulo,
        url_imagem=postagem.url_imagem,
        autor=postagem.autor,
        corpo=postagem.corpo
    )
    if formulario_edicao.validate_on_submit():  # Verifica se o formulário de edição foi enviado e é válido
        postagem.titulo = formulario_edicao.titulo.data  # Atualiza o título
        postagem.subtitulo = formulario_edicao.subtitulo.data  # Atualiza o subtítulo
        postagem.url_imagem = formulario_edicao.url_imagem.data  # Atualiza a URL da imagem
        postagem.autor = formulario_edicao.autor.data  # Atualiza o autor
        postagem.corpo = formulario_edicao.corpo.data  # Atualiza o corpo
        db.session.commit()  # Salva as alterações
        return redirect(url_for("show_post", post_id=postagem.id))  # Redireciona para a postagem editada
    return render_template("make-post.html", form=formulario_edicao, is_edit=True)  # Renderiza o formulário com os dados da postagem

# Rota para deletar uma postagem
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    postagem_para_deletar = db.get_or_404(PostagemBlog, post_id)  # Obtém a postagem ou retorna 404 se não encontrada
    db.session.delete(postagem_para_deletar)  # Deleta a postagem
    db.session.commit()  # Salva as alterações
    return redirect(url_for('get_all_posts'))  # Redireciona para a página de todas as postagens

# Rota para a página "Sobre"
@app.route("/about")
def about():
    return render_template("about.html")  # Renderiza o template "about.html"

# Rota para a página "Contato"
@app.route("/contact")
def contact():
    return render_template("contact.html")  # Renderiza o template "contact.html"

# Executa o aplicativo Flask
if __name__ == "__main__":
    app.run(debug=True, port=5002)  # Inicia o servidor em modo de depuração na porta 5002
