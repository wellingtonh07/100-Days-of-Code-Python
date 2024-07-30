import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindos ao PyPassword, o seu Gerador de Senhas em Python!")

# Solicitando ao usuário o número de letras, símbolos e números na senha
numero_de_letras = int(input("Quantas letras você quer que tenha na sua senha?\n"))
numero_de_simbolos = int(input(f"Quantos símbolos você quer que tenha na sua senha?\n"))
numero_de_numeros = int(input(f"Quantos números você quer que tenha na sua senha?\n"))

lista_senha = []

# Gerando letras aleatórias para a senha
for caracteres in range(1, numero_de_letras + 1):
    lista_senha += random.choice(letras)

# Gerando símbolos aleatórios para a senha
for caracteres in range(1, numero_de_simbolos + 1):
    lista_senha += random.choice(simbolos)

# Gerando números aleatórios para a senha
for caracteres in range(1, numero_de_numeros + 1):
    lista_senha += random.choice(numeros)

random.shuffle(lista_senha)  # Embaralhando a lista de caracteres da senha

# Convertendo a lista de caracteres em uma string para formar a senha final
senha = ""
for caracteres in lista_senha:
    senha += caracteres

# Exibindo a senha gerada
print(f"Sua senha é: {senha}")