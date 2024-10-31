class DadosDoVoo:

    def __init__(self, preco, cidade_origem, aeroporto_origem, cidade_destino, aeroporto_destino, data_ida, data_volta):
        # Inicializa os atributos da classe com os dados fornecidos
        self.preco = preco  # Preço do voo
        self.cidade_origem = cidade_origem  # Cidade de origem do voo
        self.aeroporto_origem = aeroporto_origem  # Aeroporto de origem do voo
        self.cidade_destino = cidade_destino  # Cidade de destino do voo
        self.aeroporto_destino = aeroporto_destino  # Aeroporto de destino do voo
        self.data_ida = data_ida  # Data de ida do voo
        self.data_volta = data_volta  # Data de volta do voo
