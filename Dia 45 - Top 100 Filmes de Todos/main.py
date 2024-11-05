import requests  # Importa o módulo requests para fazer requisições HTTP
from bs4 import BeautifulSoup  # Importa BeautifulSoup da biblioteca bs4 para fazer parsing do HTML

# URL do site a ser acessado
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Faz uma requisição GET para a URL especificada
resposta = requests.get(URL)

# Obtém o conteúdo HTML da resposta
html_do_site = resposta.text

# Cria um objeto BeautifulSoup para fazer parsing do HTML
soup = BeautifulSoup(html_do_site, "html.parser")

# Encontra todas as tags <h3> com a classe "title" no HTML
todos_os_filmes = soup.find_all(name="h3", class_="title")

# Extrai o texto de cada tag <h3> encontrada e armazena em uma lista
titulos_dos_filmes = [filme.getText() for filme in todos_os_filmes]

# Inverte a ordem da lista de títulos dos filmes
filmes = titulos_dos_filmes[::-1]

# Abre um arquivo chamado "filmes.txt" no modo de escrita
with open("filmes.txt", mode="w") as arquivo:
    # Para cada filme na lista de filmes
    for filme in filmes:
        # Escreve o título do filme no arquivo, seguido de uma quebra de linha
        arquivo.write(f"{filme}\n")
