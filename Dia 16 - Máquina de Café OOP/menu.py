class ItemDoMenu:
    """Modela cada item do menu."""
    def __init__(self, nome, agua, leite, cafe, custo):
        self.nome = nome
        self.custo = custo
        self.ingredientes = {
            "agua": agua,
            "leite": leite,
            "cafe": cafe
        }

class Menu:
    """Modela o menu com as bebidas."""
    def __init__(self):
        self.menu = [
            ItemDoMenu(nome="leite", agua=200, leite=150, cafe=24, custo=2.5),
            ItemDoMenu(nome="expresso", agua=50, leite=0, cafe=18, custo=1.5),
            ItemDoMenu(nome="cappuccino", agua=250, leite=50, cafe=24, custo=3),
        ]

    def obter_itens(self):
        """Retorna todos os nomes dos itens disponíveis no menu."""
        opcoes = ""
        for item in self.menu:
            opcoes += f"{item.nome}/"
        return opcoes

    def encontrar_bebida(self, nome_pedido):
        """Procura no menu uma bebida específica pelo nome. Retorna o item se existir, caso contrário retorna None."""
        for item in self.menu:
            if item.nome == nome_pedido:
                return item
        print("Desculpe, esse item não está disponível.")
        return None
