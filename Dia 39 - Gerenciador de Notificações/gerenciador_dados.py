import requests

# Endpoint da API Sheety para preços de voos
ENDPOINT_PRECOS_SHEETY = "https://api.sheety.co/*************************/flightDeals/prices/"

class GerenciadorDeDados:

    def __init__(self):
        # Inicializa um dicionário para armazenar os dados dos destinos
        self.dados_destinos = {}

    def obter_dados_dos_destinos(self):
        # Faz uma requisição GET para obter os dados dos destinos
        resposta = requests.get(url=ENDPOINT_PRECOS_SHEETY)
        dados = resposta.json()
        # Armazena os dados dos destinos no atributo da instância
        self.dados_destinos = dados["prices"]
        return self.dados_destinos

    def atualizar_codigos_dos_destinos(self):
        # Itera sobre cada cidade nos dados dos destinos
        for cidade in self.dados_destinos:
            # Prepara os dados para atualização com o novo código IATA
            novos_dados = {
                "price": {
                    "iataCode": cidade["iataCode"]
                }
            }
            # Envia uma requisição PUT para atualizar o código IATA da cidade
            resposta = requests.put(
                url=f"{ENDPOINT_PRECOS_SHEETY}/{cidade['id']}",
                json=novos_dados
            )
            # Exibe a resposta da requisição
            print(resposta.text)
