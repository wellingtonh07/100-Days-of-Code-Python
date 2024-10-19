from tkinter import *

def milhas_para_km():
    """
    Função para converter milhas para quilômetros e atualizar o rótulo de resultado.
    """
    try:
        # Obtém o valor inserido na entrada, converte para float
        milhas = float(entrada_milhas.get())
        # Converte milhas para quilômetros (1 milha = 1.609 km) e arredonda
        km = round(milhas * 1.609)
        # Atualiza o texto do rótulo com o resultado em quilômetros
        resultado_km_label.config(text=f"{km}")
    except ValueError:
        # Atualiza o texto do rótulo com uma mensagem de erro se a conversão falhar
        resultado_km_label.config(text="Erro")

# Cria a janela principal
janela = Tk()
# Define o título da janela
janela.title("Conversor de Milhas para Km")
# Define o espaçamento interno da janela
janela.config(padx=20, pady=20)

# Cria um campo de entrada para o usuário digitar o valor em milhas
entrada_milhas = Entry(width=7)
# Posiciona o campo de entrada na linha 0 e coluna 1
entrada_milhas.grid(column=1, row=0)

# Cria um rótulo ao lado do campo de entrada para indicar a unidade "Milhas"
label_milhas = Label(text="Milhas")
# Posiciona o rótulo na linha 0 e coluna 2
label_milhas.grid(column=2, row=0)

# Cria um rótulo centralizado com o texto "é igual a"
label_e_igual = Label(text="é igual a")
# Posiciona o rótulo na linha 1 e coluna 0
label_e_igual.grid(column=0, row=1)

# Cria um rótulo que será atualizado com o resultado da conversão
resultado_km_label = Label(text=0)
# Posiciona o rótulo na linha 1 e coluna 1
resultado_km_label.grid(column=1, row=1)

# Cria um rótulo ao lado do resultado para indicar a unidade "km"
label_km = Label(text="km")
# Posiciona o rótulo na linha 1 e coluna 2
label_km.grid(column=2, row=1)

# Cria um botão que chama a função milhas_para_km quando clicado
botao_calcular = Button(janela, text="Calcular", command=milhas_para_km)
# Posiciona o botão na linha 2 e coluna 1
botao_calcular.grid(column=1, row=2)

# Inicia o loop principal da interface gráfica para que a janela permaneça aberta
janela.mainloop()
