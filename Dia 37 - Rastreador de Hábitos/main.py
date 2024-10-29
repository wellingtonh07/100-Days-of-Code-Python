import requests
from datetime import datetime

# Substitua pelos seus dados
USUARIO = "SEU NOME DE USUÁRIO"
TOKEN = "SEU TOKEN GERADO"
ID_GRÁFICO = "SEU ID DO GRÁFICO"

# Endpoint da API Pixela para usuários
endpoint_pixela = "https://pixe.la/v1/users"

# Parâmetros para criar um novo usuário
parametros_usuario = {
    "token": TOKEN,
    "username": USUARIO,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## Criar um novo usuário
# resposta = requests.post(url=endpoint_pixela, json=parametros_usuario)
# print(resposta.text)

# Endpoint da API Pixela para gráficos
endpoint_grafico = f"{endpoint_pixela}/{USUARIO}/graphs"

# Configuração do gráfico
configuracao_grafico = {
    "id": ID_GRÁFICO,
    "name": "Gráfico de Ciclismo",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# Cabeçalhos para autenticação
cabecalhos = {
    "X-USER-TOKEN": TOKEN
}

## Criar um novo gráfico
# resposta = requests.post(url=endpoint_grafico, json=configuracao_grafico, headers=cabecalhos)
# print(resposta.text)

# Endpoint da API Pixela para criar um novo pixel
endpoint_pixel_criacao = f"{endpoint_pixela}/{USUARIO}/graphs/{ID_GRÁFICO}"

# Data de hoje
hoje = datetime.now()
# print(hoje.strftime("%Y%m%d"))

# Dados do pixel
dados_pixel = {
    "date": hoje.strftime("%Y%m%d"),  # Data no formato YYYYMMDD
    "quantity": input("Quantos quilômetros você ciclou hoje? "),  # Quantidade em quilômetros
}

# Criar um novo pixel
resposta = requests.post(url=endpoint_pixel_criacao, json=dados_pixel, headers=cabecalhos)
print(resposta.text)

# Endpoint para atualizar um pixel existente
endpoint_atualizacao = f"{endpoint_pixela}/{USUARIO}/graphs/{ID_GRÁFICO}/{hoje.strftime('%Y%m%d')}"

# Novos dados do pixel
novos_dados_pixel = {
    "quantity": "4.5"  # Novo valor da quantidade
}

## Atualizar um pixel existente
# resposta = requests.put(url=endpoint_atualizacao, json=novos_dados_pixel, headers=cabecalhos)
# print(resposta.text)

# Endpoint para excluir um pixel existente
endpoint_exclusao = f"{endpoint_pixela}/{USUARIO}/graphs/{ID_GRÁFICO}/{hoje.strftime('%Y%m%d')}"

## Excluir um pixel existente
# resposta = requests.delete(url=endpoint_exclusao, headers=cabecalhos)
# print(resposta.text)
