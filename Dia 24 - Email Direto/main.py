# Abre o arquivo com os nomes convidados e lê todos os nomes
with open("./Entrada/Nomes/nomes_convidados.txt") as nomes_convidados:
    lista_nomes = nomes_convidados.readlines()  # Lê todos os nomes no arquivo

# Abre o arquivo da carta inicial e lê seu conteúdo
with open("./Entrada/Cartas/carta_inicial.txt") as arquivo_carta:
    conteudo_carta = arquivo_carta.read()  # Lê o conteúdo da carta
    
    # Itera sobre cada nome na lista de nomes
    for nome in lista_nomes:
        nome = nome.strip()  # Remove espaços em branco do início e do fim do nome
        carta_nova = conteudo_carta.replace("[nome]", nome)  # Substitui o placeholder pelo nome
        
        # Cria um novo arquivo de carta personalizada para cada nome
        with open(f"./Saída/Pronto_Para_Enviar/carta_para_{nome}.txt", mode="w") as arquivo_final:
            arquivo_final.write(carta_nova)  # Escreve a carta personalizada no arquivo
