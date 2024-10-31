class DadosDoVoo:
    
    def __init__(
        self, preco, cidade_origem, aeroporto_origem, cidade_destino, aeroporto_destino, data_ida, data_volta, escalas=0, cidade_transito=""
    ):
        """
        Inicializa uma instância da classe DadosDoVoo com as informações do voo.

        Parâmetros:
        preco (float): O preço do voo.
        cidade_origem (str): Nome da cidade de origem.
        aeroporto_origem (str): Código IATA do aeroporto de origem.
        cidade_destino (str): Nome da cidade de destino.
        aeroporto_destino (str): Código IATA do aeroporto de destino.
        data_ida (str): Data de partida no formato YYYY-MM-DD.
        data_volta (str): Data de retorno no formato YYYY-MM-DD.
        escalas (int): Número de escalas no voo (padrão é 0 para voos diretos).
        cidade_transito (str): Nome da cidade onde o voo faz escala (padrão é uma string vazia).
        """
        # Armazena o preço do voo
        self.preco = preco
        # Armazena o nome da cidade de origem
        self.cidade_origem = cidade_origem
        # Armazena o código IATA do aeroporto de origem
        self.aeroporto_origem = aeroporto_origem
        # Armazena o nome da cidade de destino
        self.cidade_destino = cidade_destino
        # Armazena o código IATA do aeroporto de destino
        self.aeroporto_destino = aeroporto_destino
        # Armazena a data de partida
        self.data_ida = data_ida
        # Armazena a data de retorno
        self.data_volta = data_volta
        # Armazena o número de escalas
        self.escalas = escalas
        # Armazena o nome da cidade de transito, se houver
        self.cidade_transito = cidade_transito
