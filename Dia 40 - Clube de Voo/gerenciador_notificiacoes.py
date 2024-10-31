import smtplib  # Biblioteca para enviar e-mails usando o protocolo SMTP
import requests  # Biblioteca para fazer requisições HTTP

# Variáveis de configuração para o bot do Telegram e o e-mail
TOKEN_BOT = "******************************************"
ID_CHAT_BOT = "*********"
ENDERECO_SMTP_PROVEDOR = "smtp.outlook.com"
EMAIL = "***********************"
SENHA = "p*********"

class GerenciadorDeNotificacoes:
    
    def enviar_mensagem_telegram(self, mensagem_bot):
        """
        Envia uma mensagem para um chat do Telegram usando a API do Telegram.

        Parâmetros:
        mensagem_bot (str): O texto da mensagem a ser enviada para o chat do Telegram.

        Retorna:
        dict: A resposta da API do Telegram em formato JSON.
        """
        token_bot = TOKEN_BOT
        id_chat_bot = ID_CHAT_BOT
        url_envio = (
            'https://api.telegram.org/bot' + token_bot + '/sendMessage?chat_id=' + id_chat_bot +
            '&parse_mode=Markdown&text=' + mensagem_bot
        )
        resposta_bot = requests.get(url_envio)
        return resposta_bot.json()
        # Retorna a resposta da API do Telegram

    def enviar_emails(self, lista_emails, mensagem, link_voo_google):
        """
        Envia e-mails para uma lista de endereços com uma mensagem e um link.

        Parâmetros:
        lista_emails (list): Lista de endereços de e-mail para os quais a mensagem será enviada.
        mensagem (str): O corpo da mensagem a ser enviada.
        link_voo_google (str): Link para a oferta de voo no Google Flights que será incluído no e-mail.

        Retorna:
        None
        """
        with smtplib.SMTP(ENDERECO_SMTP_PROVEDOR) as conexao:
            # Cria uma conexão SMTP com o servidor do provedor de e-mail
            conexao.starttls()
            # Inicia a comunicação segura com o servidor SMTP
            conexao.login(EMAIL, SENHA)
            # Faz login no servidor SMTP usando o e-mail e a senha fornecidos
            for email in lista_emails:
                # Itera sobre cada e-mail na lista de destinatários
                conexao.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Novo Alerta de Preço Baixo!\n\n{mensagem}\n{link_voo_google}".encode('utf-8')
                    # Envia o e-mail com o assunto e corpo da mensagem, incluindo o link para o voo
                )
                # O e-mail é enviado para o endereço especificado
