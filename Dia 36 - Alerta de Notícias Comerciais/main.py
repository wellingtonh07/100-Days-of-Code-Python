import requests
from twilio.rest import Client

# Números de telefone
NUMERO_TWILIO_VIRTUAL = "seu número virtual do Twilio"
NUMERO_VERIFICADO = "seu número de telefone verificado com o Twilio"

# Nome da ação e da empresa
NOME_ACAO = "TSLA"
NOME_EMPRESA = "Tesla Inc"

# Endpoints para as APIs
ENDPOINT_ACAO = "https://www.alphavantage.co/query"
ENDPOINT_NOTICIAS = "https://newsapi.org/v2/everything"

# Chaves das APIs
CHAVE_API_ACAO = "SUA CHAVE API DO ALPHAVANTAGE"
CHAVE_API_NOTICIAS = "SUA CHAVE API DO NEWSAPI"
SID_TWILIO = "SEU SID DA CONTA TWILIO"
TOKEN_AUTENTICACAO_TWILIO = "SEU TOKEN DE AUTENTICAÇÃO DO TWILIO"

## PASSO 1: Usar https://www.alphavantage.co/documentation/#daily
# Quando o preço da ação aumentar/diminuir mais de 5% entre ontem e anteontem, então imprimir ("Obter Notícias").

# Obter o preço de fechamento da ação de ontem
parametros_acao = {
    "function": "TIME_SERIES_DAILY",
    "symbol": NOME_ACAO,
    "apikey": CHAVE_API_ACAO,
}

resposta = requests.get(ENDPOINT_ACAO, params=parametros_acao)
dados = resposta.json()["Time Series (Daily)"]
lista_dados = [valor for (chave, valor) in dados.items()]
dados_ontem = lista_dados[0]
preco_fechamento_ontem = dados_ontem["4. close"]
print(preco_fechamento_ontem)

# Obter o preço de fechamento da ação de anteontem
dados_anteontem = lista_dados[1]
preco_fechamento_anteontem = dados_anteontem["4. close"]
print(preco_fechamento_anteontem)

# Encontrar a diferença positiva entre 1 e 2. Exemplo: 40 - 20 = -20, mas a diferença positiva é 20.
diferenca = float(preco_fechamento_ontem) - float(preco_fechamento_anteontem)
variacao = None
if diferenca > 0:
    variacao = "🔺"
else:
    variacao = "🔻"

# Calcular a diferença percentual no preço entre o fechamento de ontem e o fechamento de anteontem.
percentual_diff = round((diferenca / float(preco_fechamento_ontem)) * 100)
print(percentual_diff)

## PASSO 2: Em vez de imprimir ("Obter Notícias"), realmente obter as 3 primeiras notícias sobre o NOME_EMPRESA.

# Em vez de imprimir ("Obter Notícias"), use a News API para obter artigos relacionados ao NOME_EMPRESA.
# Se a diferença percentual for maior que 5, então imprimir ("Obter Notícias").
if abs(percentual_diff) > 5:
    parametros_noticias = {
        "apiKey": CHAVE_API_NOTICIAS,
        "qInTitle": NOME_EMPRESA,
    }

    resposta_noticias = requests.get(ENDPOINT_NOTICIAS, params=parametros_noticias)
    artigos = resposta_noticias.json()["articles"]

    # Usar a notação de fatiamento do Python para criar uma lista contendo os 3 primeiros artigos.
    tres_artigos = artigos[:3]
    print(tres_artigos)

    ## PASSO 3: Usar o Twilio para enviar uma mensagem separada com o título e a descrição de cada artigo para seu número de telefone.

    # Criar uma nova lista dos primeiros 3 artigos com título e descrição usando compreensão de lista.
    artigos_formatados = [f"{NOME_ACAO}: {variacao}{percentual_diff}%\nTítulo: {artigo['title']}. \nResumo: {artigo['description']}" for artigo in tres_artigos]
    print(artigos_formatados)

    # Enviar cada artigo como uma mensagem separada via Twilio.
    cliente = Client(SID_TWILIO, TOKEN_AUTENTICACAO_TWILIO)

    # Enviar cada artigo como uma mensagem separada via Twilio.
    for artigo in artigos_formatados:
        mensagem = cliente.messages.create(
            body= artigo,
            from_=NUMERO_TWILIO_VIRTUAL,
            to=NUMERO_VERIFICADO
        )
