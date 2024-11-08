from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Opcional - Manter o navegador aberto (ajuda a diagnosticar problemas caso o script falhe)
opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

# Inicializa o navegador com as opções especificadas
navegador = webdriver.Chrome(options=opcoes_chrome)

# Abre o site do experimento do cookie
navegador.get("http://orteil.dashnet.org/experiments/cookie/")

# Obtém o botão de cookie para clicar
botao_cookie = navegador.find_element(by=By.ID, value="cookie")

# Obtém todos os itens de upgrade
itens = navegador.find_elements(by=By.CSS_SELECTOR, value="#store div")
ids_itens = [item.get_attribute("id") for item in itens]

# Define o tempo de espera inicial para 5 segundos
tempo_limite = time.time() + 5
# Define o tempo de execução total para 5 minutos
cinco_minutos = time.time() + 60*5  # 5 minutos

while True:
    # Clica no botão de cookie
    botao_cookie.click()

    # A cada 5 segundos:
    if time.time() > tempo_limite:

        # Obtém todos os preços dos upgrades
        todos_precios = navegador.find_elements(by=By.CSS_SELECTOR, value="#store b")
        precos_itens = []

        # Converte o texto dos preços em números inteiros
        for precio in todos_precios:
            texto_elemento = precio.text
            if texto_elemento != "":
                custo = int(texto_elemento.split("-")[1].strip().replace(",", ""))
                precos_itens.append(custo)

        # Cria um dicionário com os itens da loja e seus preços
        melhorias_cookie = {}
        for n in range(len(precos_itens)):
            melhorias_cookie[precos_itens[n]] = ids_itens[n]

        # Obtém a quantidade atual de cookies
        elemento_dinheiro = navegador.find_element(by=By.ID, value="money").text
        if "," in elemento_dinheiro:
            elemento_dinheiro = elemento_dinheiro.replace(",", "")
        contagem_cookie = int(elemento_dinheiro)

        # Encontra os upgrades que podemos pagar no momento
        upgrades_aseguraveis = {}
        for custo, id in melhorias_cookie.items():
            if contagem_cookie > custo:
                upgrades_aseguraveis[custo] = id

        # Compra o upgrade mais caro que podemos pagar
        upgrade_mais_caro_aseguravel = max(upgrades_aseguraveis)
        print(upgrade_mais_caro_aseguravel)
        id_para_comprar = upgrades_aseguraveis[upgrade_mais_caro_aseguravel]

        # Clica no upgrade para comprá-lo
        navegador.find_element(by=By.ID, value=id_para_comprar).click()

        # Atualiza o tempo limite para a próxima verificação
        tempo_limite = time.time() + 5

    # Após 5 minutos, para o bot e exibe a quantidade de cookies por segundo
    if time.time() > cinco_minutos:
        cookies_por_segundo = navegador.find_element(by=By.ID, value="cps").text
        print(cookies_por_segundo)
        break
