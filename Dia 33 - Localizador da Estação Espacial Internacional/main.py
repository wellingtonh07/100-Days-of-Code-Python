import requests
from datetime import datetime
import smtplib
import time

# Informações do usuário
MEU_EMAIL = "___SEU_EMAIL_AQUI___"
MINHA_SENHA = "___SUA_SENHA_AQUI___"

# Coordenadas da localização do usuário
MINHA_LATITUDE = 51.507351 
MINHA_LONGITUDE = -0.127758 

def verificar_iss_acima():
    """Verifica se a Estação Espacial Internacional (ISS) está passando diretamente sobre a localização do usuário."""
    resposta = requests.get(url="http://api.open-notify.org/iss-now.json")
    resposta.raise_for_status()  # Lança um erro se a requisição falhar
    dados = resposta.json()

    latitude_iss = float(dados["iss_position"]["latitude"])
    longitude_iss = float(dados["iss_position"]["longitude"])

    # Verifica se a ISS está dentro de um intervalo de 5 graus da localização do usuário
    if MINHA_LATITUDE - 5 <= latitude_iss <= MINHA_LATITUDE + 5 and MINHA_LONGITUDE - 5 <= longitude_iss <= MINHA_LONGITUDE + 5:
        return True
    return False

def verificar_noite():
    """Verifica se é noite na localização do usuário."""
    parametros = {
        "lat": MINHA_LATITUDE,
        "lng": MINHA_LONGITUDE,
        "formatted": 0,  # Formato de resposta no formato ISO 8601
    }
    resposta = requests.get("https://api.sunrise-sunset.org/json", params=parametros)
    resposta.raise_for_status()  # Lança um erro se a requisição falhar
    dados = resposta.json()
    
    # Obtém as horas de nascer e pôr do sol
    nascer_sol = int(dados["results"]["sunrise"].split("T")[1].split(":")[0])
    por_do_sol = int(dados["results"]["sunset"].split("T")[1].split(":")[0])

    hora_atual = datetime.now().hour

    # Verifica se a hora atual está dentro do período de noite
    if hora_atual >= por_do_sol or hora_atual <= nascer_sol:
        return True
    return False

while True:
    time.sleep(60)  # Aguarda 60 segundos entre as verificações
    if verificar_iss_acima() and verificar_noite():
        # Configura a conexão com o servidor de e-mail
        conexao = smtplib.SMTP("__SEU_SERVIDOR_SMTP_AQUI___")
        conexao.starttls()  # Inicia a criptografia para a conexão
        conexao.login(MEU_EMAIL, MINHA_SENHA)  # Faz login na conta de e-mail
        conexao.sendmail(
            from_addr=MEU_EMAIL,
            to_addrs=MEU_EMAIL,
            msg="Subject: Olhe para Cima👆\n\nA ISS está acima de você no céu."
        )
        conexao.quit()  # Fecha a conexão com o servidor de e-mail
