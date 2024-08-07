# Definição das variáveis iniciais de recursos e preços
agua = 300  # em ml
leite = 200  # em ml
cafe = 100   # em g
dinheiro = 0.0  # em reais

# Preços das bebidas
precos = {
    'espresso': 7.50,
    'leite': 10.00,
    'cappuccino': 12.00
}

# Ingredientes necessários para cada bebida
ingredientes = {
    'espresso': {'agua': 50, 'leite': 0, 'cafe': 18},
    'leite': {'agua': 200, 'leite': 150, 'cafe': 24},
    'cappuccino': {'agua': 250, 'leite': 100, 'cafe': 24}
}

def imprimir_relatorio():
    """Imprime o relatório atual dos recursos e dinheiro."""
    global agua, leite, cafe, dinheiro
    print(f"Água: {agua}ml")
    print(f"Leite: {leite}ml")
    print(f"Café: {cafe}g")
    print(f"Dinheiro: R${dinheiro:.2f}")

def verificar_recursos(bebida):
    """Verifica se há recursos suficientes para fazer a bebida escolhida."""
    global agua, leite, cafe
    ingredientes_bebida = ingredientes[bebida]
    if agua < ingredientes_bebida['agua']:
        print("Desculpe, não há água suficiente.")
        return False
    if leite < ingredientes_bebida['leite']:
        print("Desculpe, não há leite suficiente.")
        return False
    if cafe < ingredientes_bebida['cafe']:
        print("Desculpe, não há café suficiente.")
        return False
    return True

def processar_moeda():
    """Processa as moedas inseridas pelo usuário e retorna o valor total em reais."""
    total = 0.0
    while True:
        try:
            # Solicita a quantidade de moedas em centavos
            centavos = int(input("Insira o total em centavos (ex: 25 para R$0.25): "))
            total += centavos / 100
            mais_moedas = input("Deseja inserir mais moedas? (s/n): ").lower()
            if mais_moedas == 'n':
                break
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    return total

def fazer_bebida(bebida):
    """Prepara a bebida e atualiza os recursos e o dinheiro da máquina."""
    global agua, leite, cafe, dinheiro
    ingredientes_bebida = ingredientes[bebida]
    agua -= ingredientes_bebida['agua']
    leite -= ingredientes_bebida['leite']
    cafe -= ingredientes_bebida['cafe']
    dinheiro += precos[bebida]
    print(f"Aqui está o seu {bebida}. Aproveite!")

def main():
    """Função principal do programa da máquina de café."""
    global agua, leite, cafe, dinheiro
    while True:
        pedido = input("O que você gostaria? (espresso/leite/cappuccino/report/off): ").lower()
        
        if pedido == "off":
            print("Desligando a máquina. Até logo!")
            break
        elif pedido == "report":
            imprimir_relatorio()
        elif pedido in precos:
            if verificar_recursos(pedido):
                print(f"O custo da bebida {pedido} é R${precos[pedido]:.2f}")
                total_inserido = processar_moeda()
                
                if total_inserido < precos[pedido]:
                    print("Desculpe, o dinheiro inserido não é suficiente. Dinheiro devolvido.")
                else:
                    troco = round(total_inserido - precos[pedido], 2)
                    if troco > 0:
                        print(f"Aqui está R${troco:.2f} de troco.")
                    fazer_bebida(pedido)
        else:
            print("Escolha inválida. Por favor, escolha entre espresso, leite, cappuccino, report ou off.")

# Executa a função principal
main()
