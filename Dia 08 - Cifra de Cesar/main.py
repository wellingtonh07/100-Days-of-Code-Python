def cifra_de_cesar():
    while True:
        # Pedir ao usuário para escolher codificar ou decodificar
        modo = input("Digite 'codificar' para criptografar ou 'decodificar' para descriptografar: ").lower()

        # Verificar se a entrada do usuário é válida
        if modo not in ['codificar', 'decodificar']:
            print("Opção inválida. Por favor, digite 'codificar' ou 'decodificar'.")
            continue
        
        # Pedir a mensagem para criptografar ou descriptografar
        mensagem = input("Digite a mensagem: ")
        
        # Pedir o número de posições de deslocamento
        try:
            deslocamento = int(input("Digite o número de posições no alfabeto para deslocar: "))
        except ValueError:
            print("Número inválido. Digite um número inteiro.")
            continue
        
        # Ajustar o deslocamento para o intervalo 0-25 (um ciclo completo do alfabeto)
        deslocamento = deslocamento % 26
        
        # Criar a mensagem criptografada ou descriptografada
        resultado = ''
        if modo == 'codificar':
            for char in mensagem:
                if char.isalpha():  # Verificar se é uma letra
                    char_idx = ord(char.lower()) - ord('a') #Representa o índice númerico de uma letra do alfabeto.
                    novo_idx = (char_idx + deslocamento) % 26
                    novo_char = chr(ord('a') + novo_idx)
                    if char.isupper():  # Manter maiúscula se era maiúscula
                        resultado += novo_char.upper()
                    else:
                        resultado += novo_char
                else:
                    resultado += char  # Mantém caracteres não alfabéticos
        elif modo == 'decodificar':
            for char in mensagem:
                if char.isalpha():
                    char_idx = ord(char.lower()) - ord('a')
                    novo_idx = (char_idx - deslocamento) % 26
                    novo_char = chr(ord('a') + novo_idx)
                    if char.isupper():
                        resultado += novo_char.upper()
                    else:
                        resultado += novo_char
                else:
                    resultado += char
        
        # Mostrar o resultado
        print(f"Aqui está o resultado: {resultado}")
        
        # Perguntar se quer repetir o processo
        repetir = input("Deseja continuar? (Digite 'S' ou 'N'): ").lower()
        if repetir != 's':
            print("Encerrando programa...")
            break

# Executar o programa
cifra_de_cesar()
