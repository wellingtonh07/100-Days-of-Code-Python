import requests

# Endpoints da API do Sheety para acessar dados de preços e usuários
ENDPOINT_PRECOS = "https://api.sheety.co/********************************/flightDeals/prices/"
ENDPOINT_USUARIOS = "https://api.sheety.co/*********************************/flightDeals/users"

class GerenciadorDeDados:
    def __init__(self):
        """
        Inicializa uma instância da classe GerenciadorDeDados.

        Instância Variáveis:
        destination_data (dict): Dicionário para armazenar os dados dos destinos.
        customer_data (dict): Dicionário para armazenar os dados dos clientes.
        """
        self.destination_data = {}

    def obter_dados_destinos(self):
        """
        Obtém os dados dos destinos do endpoint SHEETY_PRICES_ENDPOINT.

        Este método realiza uma solicitação GET ao endpoint de preços dos destinos para obter 
        as informações dos preços e os armazena na variável `destination_data`.

        Retorna:
            dict: Dados dos destinos, contendo informações como preços e códigos IATA.
        """
        resposta = requests.get(url=ENDPOINT_PRECOS)
        dados = resposta.json()
        self.destination_data = dados["prices"]
        return self.destination_data

    def atualizar_codigos_destinos(self):
        """
        Atualiza os códigos IATA dos destinos no endpoint SHEETY_PRICES_ENDPOINT.

        Este método itera sobre a lista de destinos armazenada em `destination_data` e realiza 
        uma solicitação PUT para atualizar o código IATA de cada destino. A resposta da solicitação
        é impressa para verificar o status da atualização.

        Retorna:
            None
        """
        for cidade in self.destination_data:
            novos_dados = {
                "price": {
                    "iataCode": cidade["iataCode"]
                }
            }
            resposta = requests.put(
                url=f"{ENDPOINT_PRECOS}/{cidade['id']}",
                json=novos_dados
            )
            print(resposta.text)

    def obter_emails_clientes(self):
        """
        Obtém os emails dos clientes do endpoint SHEETY_USERS_ENDPOINT.

        Este método realiza uma solicitação GET ao endpoint de usuários para obter
        os emails dos clientes e os armazena na variável `customer_data`.

        Retorna:
            dict: Dados dos clientes, contendo informações como emails.
        """
        resposta = requests.get(url=ENDPOINT_USUARIOS)
        dados = resposta.json()
        self.customer_data = dados["users"]
        return self.customer_data
