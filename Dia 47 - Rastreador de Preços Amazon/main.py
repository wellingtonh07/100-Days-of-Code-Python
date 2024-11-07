from bs4 import BeautifulSoup  # Importa BeautifulSoup da biblioteca bs4 para fazer parsing do HTML
import requests  # Importa o módulo requests para fazer requisições HTTP
import smtplib  # Importa o módulo smtplib para enviar e-mails
import os  # Importa o módulo os para acessar variáveis de ambiente
from dotenv import load_dotenv  # Importa load_dotenv para carregar variáveis de ambiente de um arquivo .env

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# URL do produto a ser monitorado
# url = "https://appbrewery.github.io/instant_pot/"
# Site ao vivo
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# ====================== Adicionar Cabeçalhos à Requisição ===========================

# Cabeçalhos detalhados (comentados)
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
# }

# Cabeçalhos mínimos
cabeçalho = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Adiciona cabeçalhos à requisição
resposta = requests.get(url, headers=cabeçalho)

# Cria um objeto BeautifulSoup para fazer parsing do HTML da resposta
sopa = BeautifulSoup(resposta.content, "html.parser")

# Verifica se a página da Amazon foi recebida corretamente (para depuração)
print(sopa.prettify())

# Encontra o elemento HTML que contém o preço do produto
preço = sopa.find(class_="a-offscreen").get_text()

# Remove o símbolo de dólar usando split
preço_sem_moeda = preço.split("$")[1]

# Converte o preço para um número de ponto flutuante
preço_como_float = float(preço_sem_moeda)
print(preço_como_float)

# Obtém o título do produto
título = sopa.find(id="productTitle").get_text().strip()
print(título)

# Define o preço abaixo do qual você gostaria de receber uma notificação
PREÇO_DE_COMPRA = 70

# Verifica se o preço do produto é menor que o preço desejado
if preço_como_float < PREÇO_DE_COMPRA:
    mensagem = f"{título} está em promoção por {preço}!"

    # ====================== Enviar o E-mail ===========================

    # Envia um e-mail usando o servidor SMTP
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as conexão:
        conexão.starttls()  # Inicializa a criptografia TLS
        resultado = conexão.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])  # Faz login no servidor SMTP
        conexão.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],  # Endereço de e-mail do remetente
            to_addrs=os.environ["EMAIL_ADDRESS"],  # Endereço de e-mail do destinatário (o mesmo do remetente)
            msg=f"Subject: Alerta de Preço na Amazon!\n\n{mensagem}\n{url}".encode("utf-8")  # Mensagem do e-mail
        )
