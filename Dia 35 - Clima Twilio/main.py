import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Endpoint da API do OpenWeatherMap
ENDPOINT_Owm = "https://api.openweathermap.org/data/2.5/forecast"
# Chave da API do OpenWeatherMap obtida das variáveis de ambiente
chave_api = os.environ.get("OWM_API_KEY")
# SID da conta e token de autenticação do Twilio obtidos das variáveis de ambiente
sid_conta = "YOUR ACCOUNT SID"
token_autenticacao = os.environ.get("AUTH_TOKEN")

# Parâmetros para a requisição da API do OpenWeatherMap
parametros_meteorologicos = {
    "lat": 46.947975,  # Latitude do local
    "lon": 7.447447,   # Longitude do local
    "appid": chave_api, # Chave da API
    "cnt": 4,          # Número de previsões horárias
}

# Realiza a requisição para a API do OpenWeatherMap
resposta = requests.get(ENDPOINT_Owm, params=parametros_meteorologicos)
# Verifica se a requisição foi bem sucedida
resposta.raise_for_status()
# Converte a resposta para formato JSON
dados_meteorologicos = resposta.json()
# print(dados_meteorologicos["list"][0]["weather"][0]["id"])

# Variável para verificar se vai chover
vai_chover = False
# Verifica as condições meteorológicas para cada hora
for dados_hora in dados_meteorologicos["list"]:
    codigo_condicao = dados_hora["weather"][0]["id"]
    # Se o código da condição for menor que 700, significa que pode chover
    if int(codigo_condicao) < 700:
        vai_chover = True
        
# Se vai chover, envia uma mensagem de texto
if vai_chover:
    # Configura o cliente HTTP para o Twilio com proxy, se necessário
    cliente_proxy = TwilioHttpClient()
    cliente_proxy.session.proxies = {'https': os.environ['https_proxy']}

    # Cria um cliente do Twilio com as credenciais
    cliente = Client(sid_conta, token_autenticacao, http_client=cliente_proxy)

    # Envia a mensagem de texto
    mensagem = cliente.messages \
        .create(
        body="Vai chover hoje. Lembre-se de trazer um ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",  # Número virtual do Twilio
        to="YOUR TWILIO VERIFIED REAL NUMBER"  # Número real verificado do Twilio
    )
    # Imprime o status da mensagem enviada
    print(mensagem.status)
