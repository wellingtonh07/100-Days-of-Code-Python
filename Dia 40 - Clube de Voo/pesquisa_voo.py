import requests  # Biblioteca para fazer requisições HTTP
from dados_voo import DadosDoVoo  # Importa a classe FlightData para armazenar os dados do voo

# Endpoint da API Tequila
ENDPOINT_TEQUILA = "https://tequila-api.kiwi.com"
# Chave da API Tequila para autenticação
CHAVE_API_TEQUILA = "********************************"

class PesquisaDeVoos:
    
    def obter_codigo_destino(self, nome_cidade):
        """
        Obtém o código IATA da cidade de destino usando a API da Tequila.

        Parâmetros:
        nome_cidade (str): O nome da cidade para a qual se deseja obter o código IATA.

        Retorna:
        str: O código IATA da cidade de destino.
        """
        # Endpoint da API para buscar localidades
        endpoint_localizacao = f"{ENDPOINT_TEQUILA}/locations/query"
        # Cabeçalhos de autenticação para a API Tequila
        cabeçalhos = {"apikey": CHAVE_API_TEQUILA}
        # Parâmetros da consulta
        parametros = {"term": nome_cidade, "location_types": "city"}
        # Faz a requisição GET para o endpoint da API Tequila
        resposta = requests.get(url=endpoint_localizacao, headers=cabeçalhos, params=parametros)
        # Extrai o código IATA da resposta JSON
        resultados = resposta.json()["locations"]
        codigo = resultados[0]["code"]
        return codigo

    def verificar_voos(self, codigo_cidade_origem, codigo_cidade_destino, data_ida, data_volta):
        """
        Verifica opções de voos entre a cidade de origem e a cidade de destino para as datas especificadas.

        Parâmetros:
        codigo_cidade_origem (str): O código IATA da cidade de origem.
        codigo_cidade_destino (str): O código IATA da cidade de destino.
        data_ida (datetime): A data de partida.
        data_volta (datetime): A data de retorno.

        Retorna:
        FlightData ou None: Um objeto FlightData com os detalhes do voo se encontrado; None se nenhum voo for encontrado.
        """
        # Cabeçalhos de autenticação para a API Tequila
        cabeçalhos = {"apikey": CHAVE_API_TEQUILA}
        # Parâmetros da consulta para a API de busca de voos
        parametros = {
            "fly_from": codigo_cidade_origem,
            "fly_to": codigo_cidade_destino,
            "date_from": data_ida.strftime("%d/%m/%Y"),
            "date_to": data_volta.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        # Faz a requisição GET para buscar voos diretos
        resposta = requests.get(
            url=f"{ENDPOINT_TEQUILA}/v2/search",
            headers=cabeçalhos,
            params=parametros,
        )

        try:
            # Tenta extrair os dados do voo direto da resposta JSON
            dados = resposta.json()["data"][0]
        except IndexError:
            # Se nenhum voo direto for encontrado, tenta buscar voos com uma escala
            parametros["max_stopovers"] = 1
            resposta = requests.get(
                url=f"{ENDPOINT_TEQUILA}/v2/search",
                headers=cabeçalhos,
                params=parametros,
            )
            dados = resposta.json()["data"][0]
            # Exibe os dados do voo com uma escala
            from pprint import pprint
            pprint(dados)
            # Cria um objeto FlightData com os dados do voo com uma escala
            voo_dados = DadosDoVoo(
                preco=dados["price"],
                cidade_origem=dados["route"][0]["cityFrom"],
                aeroporto_origem=dados["route"][0]["flyFrom"],
                cidade_destino=dados["route"][1]["cityTo"],
                aeroporto_destino=dados["route"][1]["flyTo"],
                data_ida=dados["route"][0]["local_departure"].split("T")[0],
                data_volta=dados["route"][2]["local_departure"].split("T")[0],
                escalas=1,
                cidade_transito=dados["route"][0]["cityTo"]
            )
            return voo_dados
        else:
            # Cria um objeto FlightData com os dados do voo direto
            voo_dados = DadosDoVoo(
                preco=dados["price"],
                cidade_origem=dados["route"][0]["cityFrom"],
                aeroporto_origem=dados["route"][0]["flyFrom"],
                cidade_destino=dados["route"][0]["cityTo"],
                aeroporto_destino=dados["route"][0]["flyTo"],
                data_ida=dados["route"][0]["local_departure"].split("T")[0],
                data_volta=dados["route"][1]["local_departure"].split("T")[0]
            )
            return voo_dados
