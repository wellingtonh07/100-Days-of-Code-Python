from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

# Defina suas credenciais do Facebook
EMAIL_FACEBOOK = 'SEU EMAIL DO FACEBOOK'
SENHA_FACEBOOK = 'SUA SENHA DO FACEBOOK'

# Inicialize o navegador Chrome
driver = webdriver.Chrome()

# Acesse o site do Tinder
driver.get("http://www.tinder.com")

# Aguarde a página carregar
sleep(2)

# Clique no botão de login
botao_login = driver.find_element(By.XPATH, '//*[text()="Log in"]')
botao_login.click()

# Aguarde o modal de login aparecer
sleep(2)

# Clique no botão de login via Facebook
botao_login_fb = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
botao_login_fb.click()

# Aguarde a janela de login do Facebook aparecer
sleep(2)

# Altere o foco para a janela de login do Facebook
janela_base = driver.window_handles[0]
janela_login_fb = driver.window_handles[1]
driver.switch_to.window(janela_login_fb)

# Preencha o formulário de login do Facebook
campo_email = driver.find_element(By.XPATH, '//*[@id="email"]')
campo_senha = driver.find_element(By.XPATH, '//*[@id="pass"]')
campo_email.send_keys(EMAIL_FACEBOOK)
campo_senha.send_keys(SENHA_FACEBOOK)
campo_senha.send_keys(Keys.ENTER)

# Volte para a janela principal do Tinder
driver.switch_to.window(janela_base)

# Aguarde o carregamento da página do Tinder
sleep(5)

# Permita o acesso à localização
botao_permitir_localizacao = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
botao_permitir_localizacao.click()

# Permita notificações
botao_notificacoes = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
botao_notificacoes.click()

# Aceite os cookies
botao_cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
botao_cookies.click()

# Limite de 100 "Likes" por dia para contas gratuitas
for _ in range(100):
    # Adicione um atraso de 1 segundo entre os likes
    sleep(1)

    try:
        # Tente clicar no botão "Like"
        botao_like = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        botao_like.click()

    except ElementClickInterceptedException:
        # Se houver um pop-up de "Match", clique para fechá-lo
        try:
            popup_match = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            popup_match.click()

        except NoSuchElementException:
            # Se o botão "Like" não estiver carregado, espere 2 segundos e tente novamente
            sleep(2)

# Feche o navegador
driver.quit()
