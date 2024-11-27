from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
class Base(DeclarativeBase):
    pass

# Define a URI de conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# Inicializa o SQLAlchemy com a classe base definida
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Criação da tabela "Cafés"
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Identificador único do café
    nome: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Nome do café
    url_mapa: Mapped[str] = mapped_column(String(500), nullable=False)  # URL do mapa
    url_imagem: Mapped[str] = mapped_column(String(500), nullable=False)  # URL da imagem
    localizacao: Mapped[str] = mapped_column(String(250), nullable=False)  # Localização do café
    lugares: Mapped[str] = mapped_column(String(250), nullable=False)  # Número de lugares
    tem_banheiro: Mapped[bool] = mapped_column(Boolean, nullable=False)  # Se tem banheiro
    tem_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)  # Se tem Wi-Fi
    tem_tomadas: Mapped[bool] = mapped_column(Boolean, nullable=False)  # Se tem tomadas
    pode_atender_chamadas: Mapped[bool] = mapped_column(Boolean, nullable=False)  # Se pode atender chamadas
    preco_cafe: Mapped[str] = mapped_column(String(250), nullable=True)  # Preço do café

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rota principal que renderiza a página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Rota para obter um café aleatório
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))  # Seleciona todos os cafés
    todos_os_cafes = result.scalars().all()  # Obtém todos os cafés como uma lista
    cafe_aleatorio = random.choice(todos_os_cafes)  # Seleciona um café aleatório
    return jsonify(cafe=cafe_aleatorio.to_dict())  # Retorna o café em formato JSON

# Rota para obter todos os cafés ordenados pelo nome
@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.nome))  # Seleciona todos os cafés ordenados
    todos_os_cafes = result.scalars().all()  # Obtém todos os cafés como uma lista
    return jsonify(cafes=[cafe.to_dict() for cafe in todos_os_cafes])  # Retorna a lista de cafés em formato JSON

# Rota para buscar cafés em uma localização específica
@app.route("/search")
def get_cafe_at_location():
    localizacao_query = request.args.get("loc")  # Obtém a localização da query string
    result = db.session.execute(db.select(Cafe).where(Cafe.localizacao == localizacao_query))  # Busca cafés pela localização
    todos_os_cafes = result.scalars().all()  # Obtém os cafés encontrados
    if todos_os_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in todos_os_cafes])  # Retorna os cafés encontrados
    else:
        return jsonify(error={"Not Found": "Desculpe, não temos um café naquela localização."}), 404  # Retorna erro 404 se não encontrar

# Rota para adicionar um novo café via POST
@app.route("/add", methods=["POST"])
def post_new_cafe():
    novo_cafe = Cafe(
        nome=request.form.get("name"),
        url_mapa=request.form.get("map_url"),
        url_imagem=request.form.get("img_url"),
        localizacao=request.form.get("loc"),
        tem_tomadas=bool(request.form.get("sockets")),
        tem_banheiro=bool(request.form.get("toilet")),
        tem_wifi=bool(request.form.get("wifi")),
        pode_atender_chamadas=bool(request.form.get("calls")),
        lugares=request.form.get("seats"),
        preco_cafe=request.form.get("coffee_price"),
    )
    db.session.add(novo_cafe)  # Adiciona o novo café à sessão
    db.session.commit()  # Salva as alterações no banco de dados
    return jsonify(response={"success": "Café adicionado com sucesso."})

# Rota para atualizar o preço de um café pelo ID
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    novo_preco = request.args.get("new_price")  # Obtém o novo preço da query string
    cafe = db.get_or_404(Cafe, cafe_id)  # Obtém o café pelo ID ou retorna 404 se não encontrado
    if cafe:
        cafe.preco_cafe = novo_preco  # Atualiza o preço
        db.session.commit()  # Salva as alterações
        return jsonify(response={"success": "Preço atualizado com sucesso."}), 200
    else:
        return jsonify(error={"Not Found": "Desculpe, um café com esse id não foi encontrado."}), 404

# Rota para deletar um café pelo ID
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")  # Obtém a chave da API da query string
    if api_key == "TopSecretAPIKey":  # Verifica se a chave está correta
        cafe = db.get_or_404(Cafe, cafe_id)  # Obtém o café pelo ID
        if cafe:
            db.session.delete(cafe)  # Deleta o café
            db.session.commit()  # Salva as alterações
            return jsonify(response={"success": "Café deletado com sucesso."}), 200
        else:
            return jsonify(error={"Not Found": "Desculpe, um café com esse id não foi encontrado."}), 404
    else:
        return jsonify(error={"Forbidden": "Desculpe, isso não é permitido. Verifique a chave da API."}), 403

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
