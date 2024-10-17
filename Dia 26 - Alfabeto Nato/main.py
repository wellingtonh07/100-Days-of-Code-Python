
import pandas  # Importa a biblioteca pandas para manipulação de dados

# Lê o arquivo CSV que contém o alfabeto fonético da OTAN e cria um DataFrame
dados = pandas.read_csv("fonetico_alfabeto_nato.csv")

# Cria um dicionário onde a chave é a letra e o valor é o código fonético correspondente
# Utiliza compreensão de dicionário para iterar sobre cada linha do DataFrame
dicionario_fonetico = {linha.letra: linha.codigo for (indice, linha) in dados.iterrows()}

# Imprime o dicionário fonético, mostrando as letras e seus códigos fonéticos
print(dicionario_fonetico)

# Solicita ao usuário que insira uma palavra e converte a entrada para maiúsculas
palavra = input("Digite uma palavra: ").upper()

# Cria uma lista dos códigos fonéticos para cada letra na palavra fornecida pelo usuário
# Utiliza compreensão de lista para buscar o código fonético de cada letra no dicionário
lista_saida = [dicionario_fonetico[letra] for letra in palavra]

# Imprime a lista dos códigos fonéticos resultante
print(lista_saida)
