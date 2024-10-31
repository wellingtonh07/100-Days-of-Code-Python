from datetime import datetime, timedelta
from gerenciador_dados import GerenciadorDeDados
from pesquisa_voo import BuscaDeVoos
from gerenciador_notificacoes import GerenciadorDeNotificacoes

# Criação de instâncias das classes
gerenciador_de_dados = GerenciadorDeDados()
dados_da_planilha = gerenciador_de_dados.obter_dados_dos_destinos()
busca_de_voos = BuscaDeVoos()
gerenciador_de_notificacoes = GerenciadorDeNotificacoes()

# Código da cidade de origem (Londres, por exemplo)
CODIGO_CIDADE_ORIGEM = "LON"

# Verifica se o código IATA está vazio e, se estiver, atualiza os códigos
if dados_da_planilha[0]["iataCode"] == "":
    for linha in dados_da_planilha:
        linha["iataCode"] = busca_de_voos.obter_codigo_do_destino(linha["cidade"])
    gerenciador_de_dados.dados_destinos = dados_da_planilha
    gerenciador_de_dados.atualizar_codigos_dos_destinos()

# Define as datas para a busca de voos
amanha = datetime.now() + timedelta(days=1)
seis_meses_a_partir_de_hoje = datetime.now() + timedelta(days=(6 * 30))

# Verifica os voos para cada destino e envia notificação se o preço estiver abaixo do mínimo
for destino in dados_da_planilha:
    voo = busca_de_voos.verificar_voos(
        CODIGO_CIDADE_ORIGEM,
        destino["iataCode"],
        data_de=amanha,
        data_ate=seis_meses_a_partir_de_hoje
    )
    if voo and voo.preco < destino["menorPreco"]:
        gerenciador_de_notificacoes.enviar_texto_telegram(
            f"Aviso de preço baixo! Apenas £{voo.preco} para voar de {voo.cidade_origem}-{voo.aeroporto_origem} "
            f"para {voo.cidade_destino}-{voo.aeroporto_destino}, "
            f"de {voo.data_ida} até {voo.data_volta}."
        )
