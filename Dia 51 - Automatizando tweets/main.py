from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Velocidade prometida do provedor de internet (em Mbps)
VELOCIDADE_PROMETIDA_DOWN = 150
VELOCIDADE_PROMETIDA_UP = 10

# Credenciais do Twitter
EMAIL_TWITTER = 'SEU EMAIL DO TWITTER'
SENHA_TWITTER = 'SUA SENHA DO TWITTER'

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        # Inicializa o driver do navegador e variáveis para armazenar a velocidade da internet
        self.driver = webdriver.Chrome()
        self.velocidade_down = 0
        self.velocidade_up = 0

    def obter_velocidade_internet(self):
        # Acesse o site Speedtest
        self.driver.get("https://www.speedtest.net/")

        # Aguarde o carregamento da página
        time.sleep(3)

        # Inicie o teste de velocidade
        botao_iniciar = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        botao_iniciar.click()

        # Aguarde o teste concluir
        time.sleep(60)

        # Obtenha as velocidades de download e upload
        self.velocidade_down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.velocidade_up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def twittar_para_provedor(self):
        # Acesse a página de login do Twitter
        self.driver.get("https://twitter.com/login")

        # Aguarde o carregamento da página de login
        time.sleep(2)

        # Preencha o formulário de login do Twitter
        campo_email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        campo_senha = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        campo_email.send_keys(EMAIL_TWITTER)
        campo_senha.send_keys(SENHA_TWITTER)
        time.sleep(2)
        campo_senha.send_keys(Keys.ENTER)

        # Aguarde o carregamento da página principal do Twitter
        time.sleep(5)

        # Componha o tweet
        composicao_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        
        mensagem_tweet = f"Ei Provedor de Internet, por que minha velocidade de internet é {self.velocidade_down}down/{self.velocidade_up}up quando eu pago por {VELOCIDADE_PROMETIDA_DOWN}down/{VELOCIDADE_PROMETIDA_UP}up?"
        composicao_tweet.send_keys(mensagem_tweet)
        time.sleep(3)

        # Envie o tweet
        botao_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        botao_tweet.click()

        # Feche o navegador
        time.sleep(2)
        self.driver.quit()

# Crie uma instância do bot e execute as funções
bot = InternetSpeedTwitterBot(driver_path='CAMINHO/DO/CHROMEDRIVER')
bot.obter_velocidade_internet()
bot.twittar_para_provedor()
