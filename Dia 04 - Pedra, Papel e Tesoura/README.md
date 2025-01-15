# Jogo Pedra, Papel e Tesoura

Este é um simples jogo de **Pedra, Papel e Tesoura** onde você pode competir contra o computador. O jogo aceita três escolhas: **Pedra**, **Papel** ou **Tesoura**, e dependendo das escolhas, o jogo determina o vencedor ou se é um empate.

## Descrição

No jogo, você escolhe entre **Pedra**, **Papel** ou **Tesoura**. O computador também faz uma escolha aleatória. As regras do jogo são as seguintes:

- **Pedra** vence **Tesoura**.
- **Tesoura** vence **Papel**.
- **Papel** vence **Pedra**.
- Se ambos escolherem a mesma opção, é um **empate**.

## Funcionalidade

1. O jogo pede que o jogador escolha uma das opções: **Pedra**, **Papel** ou **Tesoura**.
2. O computador faz sua escolha aleatória entre as três opções.
3. O jogo compara as escolhas e determina se o jogador venceu, perdeu ou empatou.

### Exemplo de uso:

```bash
$ python pedra_papel_tesoura.py
Qual você escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura 
>> 0
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computador escolhe:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Você VENCEU!
```

### Regras do jogo:

- **Pedra (0)** vence **Tesoura (2)**
- **Tesoura (2)** vence **Papel (1)**
- **Papel (1)** vence **Pedra (0)**
- Se ambos escolherem a mesma opção, é um **empate**.

## Como jogar

1. Clone ou baixe o repositório em sua máquina local.
2. Execute o arquivo Python (`pedra_papel_tesoura.py`) em seu terminal ou editor de código preferido.
3. Escolha sua opção digitando o número correspondente:
   - 0 para **Pedra**
   - 1 para **Papel**
   - 2 para **Tesoura**
4. O computador fará a sua escolha e o resultado será exibido, indicando se você ganhou, perdeu ou empatou.

## Tecnologias

- Python 3.x

## Contribuições

Contribuições são bem-vindas! Se você tem sugestões ou melhorias para o projeto, sinta-se à vontade para fazer um fork e enviar um pull request.
