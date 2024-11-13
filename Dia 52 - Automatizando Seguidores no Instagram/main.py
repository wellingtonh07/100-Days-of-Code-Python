from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Conta do Instagram semelhante para encontrar seguidores
CONTA_SEMELHANTE = "buzzfeedtasty"  # Altere para a conta de sua escolha

# Credenciais do Instagram
USUARIO = 'SEU_USUARIO'
SENHA = 'SUA_SENHA'

class InstaFollower:
    def __init__(self):
        # Mantém o navegador aberto para que você possa se desconectar manualmente
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        # Acesse a página de login do Instagram
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4)  # Aguarde o carregamento da página

        # Verifique se o aviso de cookies está presente
        xpath_avisos_cookies = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        aviso_cookies = self.driver.find_elements(By.XPATH, xpath_avisos_cookies)
        if aviso_cookies:
            # Feche o aviso de cookies clicando no botão
            aviso_cookies[0].click()

        # Preencha os campos de usuário e senha
        campo_usuario = self.driver.find_element(By.NAME, "username")
        campo_senha = self.driver.find_element(By.NAME, "password")
        campo_usuario.send_keys(USUARIO)
        campo_senha.send_keys(SENHA)

        time.sleep(2)
        campo_senha.send_keys(Keys.ENTER)  # Faça login

        time.sleep(4)
        # Clique em "Não agora" para ignorar o prompt de salvar informações de login
        prompt_salvar_login = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        if prompt_salvar_login:
            prompt_salvar_login.click()

        time.sleep(3)
        # Clique em "Não agora" no prompt de notificações
        prompt_notificacoes = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if prompt_notificacoes:
            prompt_notificacoes.click()

    def find_followers(self):
        time.sleep(5)
        # Acesse a página de seguidores de uma conta
        self.driver.get(f"https://www.instagram.com/{CONTA_SEMELHANTE}/followers")

        time.sleep(8)
        # Atualize o XPath do modal de seguidores conforme necessário
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(By.XPATH, modal_xpath)
        for i in range(5):
            # Role a lista de seguidores para baixo
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Encontre todos os botões de "Seguir"
        todos_botoes = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')

        for botao in todos_botoes:
            try:
                botao.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # Se o botão tentar seguir alguém que já está sendo seguido, feche o diálogo
                botao_cancelar = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                botao_cancelar.click()

# Crie uma instância do bot e execute as funções
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
