class MaquinaDeCafe:
    """Modela a máquina de café que faz as bebidas."""
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leite": 200,
            "cafe": 100,
        }

    def relatorio(self):
        """Imprime o relatório dos recursos disponíveis."""
        print(f"Água: {self.recursos['agua']}ml")
        print(f"Leite: {self.recursos['leite']}ml")
        print(f"Café: {self.recursos['cafe']}g")

    def recursos_suficientes(self, bebida):
        """Verifica se há recursos suficientes para preparar a bebida."""
        pode_fazer = True
        for item in bebida.ingredientes:
            if bebida.ingredientes[item] > self.recursos[item]:
                print(f"Desculpe, não há {item} suficiente.")
                pode_fazer = False
        return pode_fazer

    def preparar_bebida(self, pedido):
        """Prepara a bebida e deduz os ingredientes dos recursos."""
        for item in pedido.ingredientes:
            self.recursos[item] -= pedido.ingredientes[item]
        print(f"Aqui está o seu {pedido.nome} ☕️. Aproveite!")
