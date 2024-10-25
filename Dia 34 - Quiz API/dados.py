import requests

# Define os parâmetros para obter perguntas do API
parametros = {
    "amount": 10,
    "type": "boolean",
}

# Faz uma requisição para obter dados do API
resposta = requests.get("https://opentdb.com/api.php", params=parametros)
# Garante que a requisição foi bem-sucedida
resposta.raise_for_status()
# Converte a resposta em JSON
dados = resposta.json()
# Obtém a lista de perguntas do JSON
dados_perguntas = dados["results"]
