# Exibe o título do programa
print("Calculadora de Gorjetas")

# Solicita o valor total da conta ao usuário e converte para float (valor monetário)
conta = float(input("Qual foi o total da conta? R$"))

# Solicita a porcentagem de gorjeta que o usuário deseja dar (opções 10, 12, ou 15)
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? 10, 12, ou 15 ? "))  # porcentagem

# Solicita a quantidade de pessoas que irão dividir a conta
pessoas = int(input("Quantas pessoas vão dividir a conta? "))

# Calcula o valor da conta com a gorjeta incluída
conta_com_gorjeta = gorjeta / 100 * conta + conta

# Divide o valor total da conta com a gorjeta pelo número de pessoas para saber quanto cada pessoa deve pagar
conta_por_pessoa = conta_com_gorjeta / pessoas

# Exibe o valor que cada pessoa deve pagar, formatado com 2 casas decimais
print(f"Cada pessoa deve pagar: R${conta_por_pessoa :.2f}")
