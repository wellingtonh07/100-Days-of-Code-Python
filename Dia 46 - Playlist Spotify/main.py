import requests  # Importa o módulo requests para fazer requisições HTTP
import spotipy  # Importa o módulo spotipy para interagir com a API do Spotify
from spotipy.oauth2 import SpotifyOAuth  # Importa SpotifyOAuth para autenticação com o Spotify

# Scraping Billboard 100
# Solicita ao usuário a data para buscar as músicas da Billboard 100
data = input("Para qual ano você quer viajar? Digite a data no formato AAAA-MM-DD: ")

# Faz uma requisição GET para a página da Billboard 100 com a data fornecida
resposta = requests.get("https://www.billboard.com/charts/hot-100/" + data)

# Cria um objeto BeautifulSoup para fazer parsing do HTML da resposta
sopa = BeautifulSoup(resposta.text, 'html.parser')

# Encontra todos os nomes das músicas na página usando seletores CSS
nomes_das_musicas_spans = sopa.select("li ul li h3")

# Extrai o texto de cada elemento e remove espaços em branco desnecessários
nomes_das_musicas = [musica.getText().strip() for musica in nomes_das_musicas_spans]

# Autenticação no Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Permissão para modificar playlists privadas
        redirect_uri="http://example.com",  # URI de redirecionamento após autenticação
        client_id=YOUR CLIENT ID,  # Substitua pelo seu ID do cliente Spotify
        client_secret=YOUR CLIENT SECRET,  # Substitua pelo seu segredo do cliente Spotify
        show_dialog=True,  # Exibe o diálogo de autenticação
        cache_path="token.txt"  # Caminho do arquivo para armazenar o token de acesso
    )
)

# Obtém o ID do usuário autenticado
id_do_usuario = sp.current_user()["id"]
print(id_do_usuario)

# Busca as músicas no Spotify pelo título
uris_das_musicas = []
ano = data.split("-")[0]  # Extrai o ano da data fornecida
for musica in nomes_das_musicas:
    resultado = sp.search(q=f"track:{musica} year:{ano}", type="track")  # Pesquisa a música no Spotify
    print(resultado)
    try:
        uri = resultado["tracks"]["items"][0]["uri"]  # Obtém o URI da primeira música encontrada
        uris_das_musicas.append(uri)  # Adiciona o URI à lista
    except IndexError:
        print(f"{musica} não existe no Spotify. Pulado.")  # Caso a música não seja encontrada

# Cria uma nova playlist privada no Spotify
playlist = sp.user_playlist_create(user=id_do_usuario, name=f"{data} Billboard 100", public=False)
print(playlist)

# Adiciona as músicas encontradas na nova playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=uris_das_musicas)
