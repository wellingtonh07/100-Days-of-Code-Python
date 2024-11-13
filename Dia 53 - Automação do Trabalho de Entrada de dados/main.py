from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Parte 1 - Raspagem dos links, endereços e preços dos imóveis para aluguel

# Cabeçalhos para a solicitação HTTP para simular um navegador real
cabeçalho = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Usamos nosso site de clone do Zillow (em vez do Zillow.com)
try:
    resposta = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=cabeçalho)
    resposta.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
except requests.RequestException as e:
    print(f"Erro ao fazer a solicitação: {e}")
    exit()

dados = resposta.text
sopa = BeautifulSoup(dados, "html.parser")

# Criar uma lista de todos os links na página usando um seletor CSS
todos_os_links_elementos = sopa.select(".StyledPropertyCardDataWrapper a") 
todos_os_links = [link["href"] for link in todos_os_links_elementos]
print(f"Existem {len(todos_os_links)} links para listagens individuais no total: \n")
print(todos_os_links)

# Criar uma lista de todos os endereços na página usando um seletor CSS
todos_os_endereços_elementos = sopa.select(".StyledPropertyCardDataWrapper address")
todos_os_endereços = [endereço.get_text().replace(" | ", " ").strip() for endereço in todos_os_endereços_elementos]
print(f"\n Após a limpeza, os {len(todos_os_endereços)} endereços agora são os seguintes: \n")
print(todos_os_endereços)

# Criar uma lista de todos os preços na página usando um seletor CSS
todos_os_precos_elementos = sopa.select(".PropertyCardWrapper span")
todos_os_precos = [preço.get_text().replace("/mo", "").split("+")[0] for preço in todos_os_precos_elementos if "$" in preço.text]
print(f"\n Após a limpeza, os {len(todos_os_precos)} preços agora são os seguintes: \n")
print(todos_os_precos)


# Parte 2 - Preencher o Formulário do Google usando Selenium

# Configurações do Chrome
opções_chrome = Options()
opções_chrome.add_experimental_option("detach", True)
service = Service('caminho/para/chromedriver')  # Substitua pelo caminho real do chromedriver

# Inicializa o driver do Chrome
try:
    driver = webdriver.Chrome(service=service, options=opções_chrome)
except Exception as e:
    print(f"Erro ao inicializar o driver do Chrome: {e}")
    exit()

# Define um tempo máximo para esperar elementos carregarem
espera = WebDriverWait(driver, 10)

for n in range(len(todos_os_links)):
    try:
        driver.get("SEU_LINK_DE_FORMULARIO_DO_GOOGLE_AQUI")
        
        # Espera até que o formulário esteja disponível
        espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        
        # Localiza e preenche os campos do formulário
        endereço = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        preço = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        botão_enviar = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        
        endereço.send_keys(todos_os_endereços[n])
        preço.send_keys(todos_os_precos[n])
        link.send_keys(todos_os_links[n])
        botão_enviar.click()
        
        # Adiciona um atraso para evitar enviar formulários muito rapidamente
        time.sleep(1)

    except Exception as e:
        print(f"Erro ao preencher o formulário: {e}")

driver.quit()  # Fecha o navegador quando terminar
