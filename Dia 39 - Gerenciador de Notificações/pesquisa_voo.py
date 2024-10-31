import requests
from dados_de_voo import DadosDoVoo

# Endpoint e chave da API Tequila
ENDPOINT_TEQUILA = "https://tequila-api.kiwi.com"
CHAVE_API_TEQUILA = "********************************"

class BuscaDeVoos:

    def obter_codigo_do_destino(self, nome_da_cidade):
        # Endpoint para consultar localizações
        endpoint_localizacao = f"{ENDPOINT_TEQUILA}/locations/query"
        # Cabeçalhos da requisição com a chave da API
        cabecalhos = {"apikey": CHAVE_API_TEQUILA}
        # Parâmetros da consulta com o nome da cidade e tipo de localização
        consulta = {"term": nome_da_cidade, "location_types": "city"}
        # Fazendo a requisição GET para obter códigos de localização
        resposta = requests.get(url=endpoint_localizacao, headers=cabecalhos, params=consulta)
        resultados = resposta.json()["locations"]
        # Obtém o código da primeira localização encontrada
        codigo = resultados[0]["code"]
        return codigo

    def verificar_voos(self, codigo_cidade_origem, codigo_cidade_destino, data_de, data_ate):
        # Cabeçalhos da requisição com a chave da API
        cabecalhos = {"apikey": CHAVE_API_TEQUILA}
        # Parâmetros da consulta para buscar voos
        consulta = {
            "fly_from": codigo_cidade_origem,
            "fly_to": codigo_cidade_destino,
            "date_from": data_de.strftime("%d/%m/%Y"),
            "date_to": data_ate.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        # Fazendo a requisição GET para buscar voos
        resposta = requests.get(
            url=f"{ENDPOINT_TEQUILA}/v2/search",
            headers=cabecalhos,
            params=consulta,
        )

        try:
            dados = resposta.json()["data"][0]
        except IndexError:
            print(f"Nenhum voo encontrado para {codigo_cidade_destino}.")
            return None

        # Cria uma instância da classe DadosDoVoo com os dados do voo
        dados_do_voo = DadosDoVoo(
            preco=dados["price"],
            cidade_origem=dados["route"][0]["cityFrom"],
            aeroporto_origem=dados["route"][0]["flyFrom"],
            cidade_destino=dados["route"][0]["cityTo"],
            aeroporto_destino=dados["route"][0]["flyTo"],
            data_ida=dados["route"][0]["local_departure"].split("T")[0],
            data_volta=dados["route"][1]["local_departure"].split("T")[0]
        )
        # Exibe as informações do voo encontrado
        print(f"{dados_do_voo.cidade_destino}: £{dados_do_voo.preco}")
        return dados_do_voo
