# Importa a biblioteca random para gerar caracteres aleatórios
import random

# Listas contendo letras (maiúsculas e minúsculas), números e símbolos
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Exibe a saudação e o nome do gerador de senhas
print("Bem vindos ao PyPassword, o seu Gerador de Senhas em Python!")

# Solicita ao usuário o número de letras, símbolos e números que a senha deve ter
numero_de_letras = int(input("Quantas letras você quer que tenha na sua senha?\n"))
numero_de_simbolos = int(input(f"Quantos símbolos você quer que tenha na sua senha?\n"))
numero_de_numeros = int(input(f"Quantos números você quer que tenha na sua senha?\n"))

# Inicializa uma lista para armazenar os caracteres da senha
lista_senha = []

# Gera letras aleatórias e as adiciona à lista da senha
for caracteres in range(1, numero_de_letras + 1):
    lista_senha += random.choice(letras)

# Gera símbolos aleatórios e os adiciona à lista da senha
for caracteres in range(1, numero_de_simbolos + 1):
    lista_senha += random.choice(simbolos)

# Gera números aleatórios e os adiciona à lista da senha
for caracteres in range(1, numero_de_numeros + 1):
    lista_senha += random.choice(numeros)

# Embaralha os caracteres da senha para torná-la aleatória
random.shuffle(lista_senha)

# Converte a lista de caracteres em uma string para formar a senha final
senha = ""
for caracteres in lista_senha:
    senha += caracteres

# Exibe a senha gerada para o usuário
print(f"Sua senha é: {senha}")
