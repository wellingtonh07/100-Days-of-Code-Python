from datetime import datetime, timedelta
from dados_voo import DadosDoVoo
from pesquisa_voo import PesquisaDeVoos
from gerenciador_notificiacoes import GerenciadorDeNotificacoes

# Código IATA da cidade de origem
CIDADE_ORIGEM_IATA = "LON"

# Inicializa as instâncias das classes para gerenciar dados, pesquisar voos e enviar notificações
gerenciador_de_dados = DadosDoVoo()
pesquisa_de_voos = PesquisaDeVoos()
gerenciador_de_notificacoes = GerenciadorDeNotificacoes()

# Obtém os dados dos destinos do gerenciador de dados
dados_da_planilha = gerenciador_de_dados.obter_dados_destinos()

# Se o código IATA estiver vazio, atualize os códigos IATA dos destinos
if dados_da_planilha[0]["iataCode"] == "":
    nomes_das_cidades = [linha["city"] for linha in dados_da_planilha]
    codigos_cidades = pesquisa_de_voos.obter_codigos_destinos(nomes_das_cidades)
    gerenciador_de_dados.city_codes = codigos_cidades
    gerenciador_de_dados.atualizar_codigos_destinos()
    dados_da_planilha = gerenciador_de_dados.obter_dados_destinos()

# Cria um dicionário de destinos com informações relevantes
destinos = {
    dado["iataCode"]: {
        "id": dado["id"],
        "cidade": dado["city"],
        "preco": dado["lowestPrice"]
    } for dado in dados_da_planilha
}

# Define o intervalo de datas para pesquisa de voos
amanha = datetime.now() + timedelta(days=1)
seis_meses_depois = datetime.now() + timedelta(days=6 * 30)

# Itera sobre os códigos de destinos para verificar os voos
for codigo_destino in destinos:
    voo = pesquisa_de_voos.verificar_voos(
        CIDADE_ORIGEM_IATA,
        codigo_destino,
        de=amanha,
        ate=seis_meses_depois
    )
    
    # Se não houver voo disponível, continue para o próximo destino
    if voo is None:
        continue

    print(voo.preco)

    # Se o preço do voo for menor que o preço atual registrado, envie uma notificação
    if voo.preco < destinos[codigo_destino]["preco"]:

        # Obtém os emails dos clientes
        usuarios = gerenciador_de_dados.obter_emails_clientes()
        emails = [linha["email"] for linha in usuarios]
        nomes = [linha["firstName"] for linha in usuarios]

        # Monta a mensagem de alerta
        mensagem = (
            f"Aviso de preço baixo! Apenas £{voo.preco} para voar de {voo.origem_cidade}-{voo.origem_aeroporto} "
            f"para {voo.destino_cidade}-{voo.destino_aeroporto}, de {voo.data_saida} a {voo.data_retorno}."
        )

        # Adiciona informações sobre escalas, se houver
        if voo.paradas > 0:
            mensagem += f"\nO voo tem {voo.paradas} escala(s), via {voo.cidade_via}."

        # Cria o link para o Google Flights
        link = (
            f"https://www.google.co.uk/flights?hl=pt#flt={voo.origem_aeroporto}.{voo.destino_aeroporto}.{voo.data_saida}"
            f"*{voo.destino_aeroporto}.{voo.origem_aeroporto}.{voo.data_retorno}"
        )
        
        # Envia os emails com as informações do voo e o link
        gerenciador_de_notificacoes.enviar_emails(emails, mensagem, link)
