from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Defina suas credenciais de login e outras informações pessoais
EMAIL_CONTA = 'SEU EMAIL DE LOGIN'
SENHA_CONTA = 'SUA SENHA DE LOGIN'
TELEFONE = 'SEU NÚMERO DE TELEFONE'

def abortar_aplicacao():
    # Clique no Botão Fechar
    botao_fechar = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    botao_fechar.click()

    time.sleep(2)
    # Clique no Botão Descartar
    botao_descartar = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    botao_descartar.click()

# Opcional - Mantenha o navegador aberto se o script falhar.
opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

# Inicie o navegador Chrome com as opções configuradas
driver = webdriver.Chrome(options=opcoes_chrome)

# Abra a página de busca de empregos no LinkedIn
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Clique no botão para rejeitar cookies
time.sleep(2)
botao_rejeitar = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
botao_rejeitar.click()

# Clique no botão de login
time.sleep(2)
botao_login = driver.find_element(by=By.LINK_TEXT, value="Sign in")
botao_login.click()

# Faça login na conta
time.sleep(5)
campo_email = driver.find_element(by=By.ID, value="username")
campo_email.send_keys(EMAIL_CONTA)
campo_senha = driver.find_element(by=By.ID, value="password")
campo_senha.send_keys(SENHA_CONTA)
campo_senha.send_keys(Keys.ENTER)

# CAPTCHA - Resolva o CAPTCHA manualmente
input("Pressione Enter quando tiver resolvido o CAPTCHA")

# Obtenha as listas de empregos
time.sleep(5)
todas_listagens = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Candidate-se a vagas de emprego
for listagem in todas_listagens:
    print("Abrindo Listagem")
    listagem.click()
    time.sleep(2)
    try:
        # Clique no botão de aplicar
        botao_aplicar = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        botao_aplicar.click()

        # Insira o número de telefone
        # Encontre um elemento <input> onde o id contém phoneNumber
        time.sleep(5)
        campo_telefone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if campo_telefone.text == "":
            campo_telefone.send_keys(TELEFONE)

        # Verifique o botão de enviar
        botao_enviar = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if botao_enviar.get_attribute("data-control-name") == "continue_unify":
            abortar_aplicacao()
            print("Aplicação complexa, ignorada.")
            continue
        else:
            # Clique no botão de enviar
            print("Enviando aplicação para o emprego")
            botao_enviar.click()

        time.sleep(2)
        # Clique no botão de fechar
        botao_fechar = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        botao_fechar.click()

    except NoSuchElementException:
        abortar_aplicacao()
        print("Nenhum botão de aplicação encontrado, ignorado.")
        continue

# Espere um pouco antes de fechar o navegador
time.sleep(5)
driver.quit()
