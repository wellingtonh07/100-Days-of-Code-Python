import requests
from datetime import datetime
import os

# Definindo variáveis de usuário
GENERO = "masculino"  # Gênero do usuário
PESO_KG = 84  # Peso do usuário em quilogramas
ALTURA_CM = 180  # Altura do usuário em centímetros
IDADE = 32  # Idade do usuário

# Obtendo as credenciais da API a partir das variáveis de ambiente
ID_APP = os.environ["ENV_NIX_APP_ID"]
CHAVE_API = os.environ["ENV_NIX_API_KEY"]

# Endpoint da API para consulta de exercícios
endpoint_exercicio = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Solicitando ao usuário para inserir o texto com os exercícios realizados
texto_exercicio = input("Diga quais exercícios você fez: ")

# Definindo os cabeçalhos para a requisição da API
cabecalhos = {
    "x-app-id": ID_APP,
    "x-app-key": CHAVE_API,
}

# Definindo os parâmetros da requisição para a API de exercícios
parametros = {
    "query": texto_exercicio,
    "gender": GENERO,
    "weight_kg": PESO_KG,
    "height_cm": ALTURA_CM,
    "age": IDADE
}

# Enviando a requisição POST para a API de exercícios
resposta = requests.post(endpoint_exercicio, json=parametros, headers=cabecalhos)
resultado = resposta.json()
print(f"Resposta da API Nutritionix: \n {resultado} \n")

# Obtendo a data e hora atuais
data_atual = datetime.now().strftime("%d/%m/%Y")
hora_atual = datetime.now().strftime("%X")

# Nome da planilha do Google Sheets e endpoint para o Sheety
NOME_PLANILHA = "workout"
endpoint_planilha = os.environ["ENV_SHEETY_ENDPOINT"]

# Iterando sobre cada exercício retornado pela API
for exercicio in resultado["exercises"]:
    # Preparando os dados para serem enviados para o Google Sheets
    entradas_planilha = {
        NOME_PLANILHA: {
            "data": data_atual,
            "hora": hora_atual,
            "exercicio": exercicio["name"].title(),  # Capitalizando o nome do exercício
            "duracao": exercicio["duration_min"],  # Duração do exercício em minutos
            "calorias": exercicio["nf_calories"]  # Calorias queimadas durante o exercício
        }
    }

    # Enviando os dados para o Google Sheets através do Sheety
    resposta_planilha = requests.post(
        endpoint_planilha,
        json=entradas_planilha,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )

    # Comentado: Envio com autenticação Bearer (não utilizado no momento)
    """
    cabecalhos_bearer = {
        "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    }
    resposta_planilha = requests.post(
        endpoint_planilha,
        json=entradas_planilha,
        headers=cabecalhos_bearer
    )
    """

    # Exibindo a resposta da requisição para a planilha
    print(f"Resposta do Sheety: \n {resposta_planilha.text}")
