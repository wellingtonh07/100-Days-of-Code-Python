import os

# Função para limpar a tela do console
def limpar_tela():
    # Verifica o sistema operacional para determinar o comando de limpeza adequado
    if os.name == 'posix':  # Se o sistema for Unix/Linux/MacOS/BSD/etc
        _ = os.system('clear')  # Usa 'clear' para limpar a tela
    elif os.name in ('nt', 'dos', 'ce'):  # Se o sistema for Windows
        _ = os.system('cls')  # Usa 'cls' para limpar a tela


print("Calculadora!")

def calculadora():
    while True:
        numero_1 = float(input("Digite o primeiro número:\n>>> "))
        operador = int(input("""
         Escolha uma operação:
         1 - Somar
         2 - Subtrair
         3 - Multiplicar
         4 - Dividir 
                          
         """))
        numero_2 = float(input("Digite o segundo número:\n>>> "))

        if operador == 1:
            resultado = numero_1 + numero_2
            print(f"O resultado é: {resultado}.")
        elif operador == 2:
            resultado = numero_1 - numero_2
            print(f"O resultado é: {resultado}.")
        elif operador == 3:
            resultado = numero_1 * numero_2
            print(f"O resultado é: {resultado}.")
        elif operador == 4:
            if numero_2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = numero_1 / numero_2
                print(f"O resultado é: {resultado}.")

        continuar = input("Deseja continuar? (S/N)\n>>> ").lower()
        if continuar != "s":
            break
        else:
            limpar_tela()

    print("Obrigado por usar a calculadora!")

calculadora()
