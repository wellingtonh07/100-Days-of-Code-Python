from flask import Flask, render_template, redirect, url_for  # Importa as bibliotecas necessárias do Flask
from flask_bootstrap import Bootstrap5  # Importa a extensão Bootstrap5 para Flask
from flask_wtf import FlaskForm  # Importa o FlaskForm para criar formulários
from wtforms import StringField, SubmitField, SelectField  # Importa tipos de campos para o formulário
from wtforms.validators import DataRequired, URL  # Importa validadores para os campos
import csv  # Importa a biblioteca CSV para manipulação de arquivos CSV

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Define a chave secreta para sessões
Bootstrap5(app)  # Inicializa o Bootstrap5

# Define a classe do formulário de café
class CafeForm(FlaskForm):
    cafe = StringField('Nome do Café', validators=[DataRequired()])  # Campo para o nome do café
    location = StringField("Localização do Café no Google Maps (URL)", validators=[DataRequired(), URL()])  # Campo para a URL
    open = StringField("Horário de Abertura, ex: 8AM", validators=[DataRequired()])  # Campo para horário de abertura
    close = StringField("Horário de Fechamento, ex: 5:30PM", validators=[DataRequired()])  # Campo para horário de fechamento
    coffee_rating = SelectField("Avaliação do Café", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])  # Seleção de avaliação do café
    wifi_rating = SelectField("Avaliação da Força do Wifi", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])  # Seleção de força do Wifi
    power_rating = SelectField("Disponibilidade de Tomadas", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])  # Seleção de tomadas
    submit = SubmitField('Enviar')  # Botão de envio

# Rota principal da aplicação
@app.route("/")
def home():
    return render_template("index.html")  # Renderiza a página index.html

# Rota para adicionar um café
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()  # Cria uma instância do formulário de café
    if form.validate_on_submit():  # Verifica se o formulário foi submetido e é válido
        # Abre o arquivo CSV no modo de anexação
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            # Escreve os dados do formulário no arquivo CSV
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))  # Redireciona para a rota de cafés
    return render_template('add.html', form=form)  # Renderiza a página de adição com o formulário

# Rota para exibir os cafés
@app.route('/cafes')
def cafes():
    # Lê os dados do arquivo CSV
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')  # Lê o arquivo CSV
        list_of_rows = []  # Lista para armazenar as linhas
        for row in csv_data:  # Itera sobre as linhas do CSV
            list_of_rows.append(row)  # Adiciona cada linha à lista
    return render_template('cafes.html', cafes=list_of_rows)  # Renderiza a página de cafés com a lista

# Executa a aplicação se o script for chamado diretamente
if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Inicia o servidor em modo de depuração na porta 5002
