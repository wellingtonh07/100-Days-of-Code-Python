from menu import Menu
from maquina_de_café import MaquinaDeCafe
from maquina_de_dinheiro import MaquinaDeDinheiro


maquina_de_dinheiro = MaquinaDeDinheiro()
maquina_de_cafe = MaquinaDeCafe()
menu = Menu()

ligada = True

while ligada:
    opcoes = menu.obter_itens()
    opcoes += "sair/"  # Adiciona a opção para sair
    escolha = input(f"O que você gostaria? ({opcoes}): ").strip().lower()
    
    if escolha == "sair":
        print("Obrigado por usar a máquina de café. Até a próxima!")
        ligada = False
    elif escolha == "relatorio":
        maquina_de_cafe.relatorio()
        maquina_de_dinheiro.relatorio()
    else:
        bebida = menu.encontrar_bebida(escolha)
        
        if bebida and maquina_de_cafe.recursos_suficientes(bebida) and maquina_de_dinheiro.efetuar_pagamento(bebida.custo):
            maquina_de_cafe.preparar_bebida(bebida)
        else:
            print("Desculpe, não conseguimos processar seu pedido. Verifique a opção e tente novamente.")
