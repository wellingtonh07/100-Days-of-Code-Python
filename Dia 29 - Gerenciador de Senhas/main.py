from tkinter import *  # Importa todos os widgets e funcionalidades do tkinter
from tkinter import messagebox  # Importa a biblioteca para exibir caixas de mensagem
from random import choice, randint, shuffle  # Importa funções para gerar aleatoriedade
import pyperclip  # Importa pyperclip para copiar texto para a área de transferência

# Função para gerar uma senha aleatória
def gerar_senha():
    # Listas de caracteres para gerar a senha
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sinais = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Gera uma lista de letras, sinais e números aleatórios
    senha_letras = [choice(letras) for _ in range(randint(8, 10))]
    senha_sinais = [choice(sinais) for _ in range(randint(2, 4))]
    senha_numeros = [choice(numeros) for _ in range(randint(2, 4))]

    # Combina todas as partes da senha e embaralha a lista
    lista_senha = senha_letras + senha_sinais + senha_numeros
    shuffle(lista_senha)

    # Junta a lista em uma string de senha
    senha = "".join(lista_senha)

    # Insere a senha gerada no campo de entrada e a copia para a área de transferência
    senha_entrada.insert(0, senha)
    pyperclip.copy(senha)

# Função para salvar as informações inseridas
def salvar():
    website = website_entrada.get()  # Obtém o site do campo de entrada
    email = email_entrada.get()  # Obtém o email do campo de entrada
    senha = senha_entrada.get()  # Obtém a senha do campo de entrada

    # Verifica se o site e a senha não estão vazios
    if len(website) == 0 or len(senha) == 0:
        messagebox.showinfo(title="Ops", message="Não deixe nenhum espaço em branco")
    else:
        # Solicita confirmação para salvar os dados
        esta_certo_disso = messagebox.askokcancel(title=website, message=f"Estes são os dados inseridos: \nEmail: {email} \nSenha: {senha} \nEstá tudo certo para salvar? ")

        if esta_certo_disso:
            # Salva as informações em um arquivo texto
            with open("dados.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {senha}\n")
                # Limpa os campos de entrada após salvar
                website_entrada.delete(0, END)
                senha_entrada.delete(0, END)

# Configuração da interface gráfica com tkinter
janela = Tk()
janela.title("Gerenciador de Senhas")  # Define o título da janela
janela.config(padx=50, pady=50)  # Configura a margem da janela

# Cria um canvas para exibir o logo
canvas = Canvas(width=200, height=200)
imagem_logo = PhotoImage(file="logo.png")  # Carrega a imagem do logo
canvas.create_image(100, 100, image=imagem_logo)  # Adiciona a imagem ao canvas
canvas.grid(row=0, column=1)

# Cria rótulos e campos de entrada para website, email e senha
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Nome de usuário:")
email_label.grid(row=2, column=0)

senha_label = Label(text="Senha:")
senha_label.grid(row=3, column=0)

website_entrada = Entry(width=35)  # Campo de entrada para o site
website_entrada.grid(row=1, column=1, columnspan=2)
website_entrada.focus()  # Foca no campo de entrada do site

email_entrada = Entry(width=35)  # Campo de entrada para o email
email_entrada.grid(row=2, column=1, columnspan=2)
email_entrada.insert(0, "seu_email@gmail.com")  # Insere um email padrão

senha_entrada = Entry(width=21)  # Campo de entrada para a senha
senha_entrada.grid(row=3, column=1)

# Cria botões para gerar a senha e adicionar as informações
senha_botao = Button(text="Gerar Senha", command=gerar_senha)
senha_botao.grid(row=3, column=2)

adicionar_botao = Button(text="Add", width=36, command=salvar)
adicionar_botao.grid(row=4, column=1, columnspan=2)

# Inicia o loop principal da interface gráfica
janela.mainloop()
