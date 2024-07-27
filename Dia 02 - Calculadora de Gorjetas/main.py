print("Calculadora de Gorjetas")
conta = float(input("Qual foi o total da conta? R$"))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? 10, 12, ou 15 ? "))    #porcentagem
pessoas = int(input("Quantas pessoas vão dividir a conta? "))
conta_com_gorjeta = gorjeta / 100 * conta + conta
conta_por_pessoa = conta_com_gorjeta / pessoas
print(f"Cada pessoa deve pagar: R${conta_por_pessoa :.2f}")

#2f - formatação para 2 casas decimais.