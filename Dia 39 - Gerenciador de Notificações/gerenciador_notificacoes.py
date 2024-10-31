import requests

# Token do bot do Telegram e ID do chat
TOKEN_BOT = "********************************************"
ID_CHAT_BOT = "*********"

class GerenciadorDeNotificacoes:

    def enviar_texto_telegram(self, mensagem_bot):
        token_bot = TOKEN_BOT
        id_chat_bot = ID_CHAT_BOT
        # URL para enviar a mensagem via Telegram
        url_envio = f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={id_chat_bot}&parse_mode=Markdown&text={mensagem_bot}'
        # Fazendo a requisição GET para enviar a mensagem
        resposta_bot = requests.get(url_envio)
        return resposta_bot.json()
