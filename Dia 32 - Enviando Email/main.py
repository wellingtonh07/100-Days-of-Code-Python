import smtplib  # Importa o módulo para enviar e-mails via SMTP
from email.mime.multipart import MIMEMultipart  # Importa o tipo de mensagem para suportar múltiplas partes
from email.mime.text import MIMEText  # Importa o tipo de mensagem para corpo de texto
from datetime import datetime, timedelta  # Importa funções para manipulação de data e hora
import time  # Importa funções para manipulação de tempo

# Função para enviar o e-mail
def enviar_email(remetente, senha, destinatario, assunto, corpo):
    """
    Envia um e-mail usando o servidor SMTP do Gmail.
    
    Args:
        remetente (str): Endereço de e-mail do remetente.
        senha (str): Senha do e-mail do remetente.
        destinatario (str): Endereço de e-mail do destinatário.
        assunto (str): Assunto do e-mail.
        corpo (str): Corpo do e-mail.
    """
    # Configura o servidor SMTP
    servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Conecta ao servidor SMTP do Gmail na porta 587
    servidor.starttls()  # Inicia a criptografia TLS para proteger a comunicação com o servidor

    # Login no servidor SMTP
    servidor.login(remetente, senha)  # Faz login no servidor SMTP usando o e-mail e a senha fornecidos

    # Criação da mensagem
    mensagem = MIMEMultipart()  # Cria uma mensagem que pode conter múltiplas partes (texto, anexos, etc.)
    mensagem['From'] = remetente  # Define o remetente do e-mail
    mensagem['To'] = destinatario  # Define o destinatário do e-mail
    mensagem['Subject'] = assunto  # Define o assunto do e-mail

    # Adiciona o corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))  # Adiciona o corpo do e-mail como texto simples

    # Envia o e-mail
    servidor.send_message(mensagem)  # Envia a mensagem para o destinatário

    # Encerra a conexão com o servidor
    servidor.quit()  # Encerra a conexão com o servidor SMTP

    print(f'E-mail enviado para {destinatario} com assunto: {assunto}')  # Imprime uma confirmação no console

# Função para agendar o envio do e-mail
def agendar_envio(remetente, senha, destinatario, assunto, corpo, horario_envio):
    """
    Agenda o envio de um e-mail para um horário específico.
    
    Args:
        remetente (str): Endereço de e-mail do remetente.
        senha (str): Senha do e-mail do remetente.
        destinatario (str): Endereço de e-mail do destinatário.
        assunto (str): Assunto do e-mail.
        corpo (str): Corpo do e-mail.
        horario_envio (datetime): Data e hora para o envio do e-mail.
    """
    while True:
        agora = datetime.now()  # Obtém a data e hora atuais
        if agora >= horario_envio:  # Verifica se é o momento para enviar o e-mail
            enviar_email(remetente, senha, destinatario, assunto, corpo)  # Envia o e-mail
            break  # Sai do loop após o envio
        else:
            # Calcula o tempo de espera até o horário de envio
            espera = (horario_envio - agora).total_seconds()  # Calcula a diferença em segundos
            print(f'Aguardando {espera} segundos para enviar o e-mail...')  # Imprime o tempo restante no console
            time.sleep(min(espera, 60))  # Aguarda o tempo calculado ou até 60 segundos, o que for menor

# Exemplo de uso
if __name__ == "__main__":
    remetente = 'seu_email@gmail.com'  # Substitua pelo e-mail do remetente
    senha = 'sua_senha'  # Substitua pela senha do e-mail do remetente
    destinatario = 'destinatario@gmail.com'  # Substitua pelo e-mail do destinatário
    assunto = 'Assunto do E-mail'  # Substitua pelo assunto desejado
    corpo = 'Olá, este é um e-mail enviado automaticamente!'  # Substitua pelo corpo do e-mail
    
    # Define o horário de envio para 1 minuto no futuro
    horario_envio = datetime.now() + timedelta(minutes=1)
    
    print(f'Agendando o envio para {horario_envio.strftime("%Y-%m-%d %H:%M:%S")}')  # Imprime o horário de envio agendado
    agendar_envio(remetente, senha, destinatario, assunto, corpo, horario_envio)  # Chama a função para agendar o envio
