class MaquinaDeDinheiro:
    """Modela a máquina que gerencia o dinheiro."""
    MOEDA = "R$"

    VALORES_MOEDA = {
        "moedas de 25 centavos": 0.25,
        "moedas de 10 centavos": 0.10,
        "moedas de 5 centavos": 0.05,
        "moedas de 1 centavo": 0.01
    }

    def __init__(self):
        self.provento = 0
        self.dinheiro_recebido = 0

    def relatorio(self):
        """Imprime o lucro atual da máquina de dinheiro."""
        print(f"Dinheiro: {self.MOEDA}{self.provento}")

    def processar_moedas(self):
        """Processa as moedas inseridas e retorna o total."""
        print("Por favor, insira as moedas.")
        for moeda in self.VALORES_MOEDA:
            self.dinheiro_recebido += int(input(f"Quantas {moeda}?: ")) * self.VALORES_MOEDA[moeda]
        return self.dinheiro_recebido

    def efetuar_pagamento(self, custo):
        """Verifica se o pagamento é suficiente e, se sim, retorna troco. Caso contrário, reembolsa o dinheiro."""
        self.processar_moedas()
        if self.dinheiro_recebido >= custo:
            troco = round(self.dinheiro_recebido - custo, 2)
            print(f"Aqui está {self.MOEDA}{troco} de troco.")
            self.provento += custo
            self.dinheiro_recebido = 0
            return True
        else:
            print("Desculpe, o valor não é suficiente. Dinheiro reembolsado.")
            self.dinheiro_recebido = 0
            return False
