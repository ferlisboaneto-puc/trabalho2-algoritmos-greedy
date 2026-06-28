# Implementacao - Exercicio Greedy

Este projeto resolve o problema do rally no deserto usando a estrategia gulosa de
sempre escolher, como proxima parada para acampar, o ponto mais distante que ainda
pode ser alcancado dentro do limite diario `d`.

Arquivos:

- `rally.py`: implementacao em Python 3.

## Formato da entrada

Ao executar o programa, ele pede cada informacao no terminal:

- `L`: comprimento total da trilha.
- `d`: distancia maxima que pode ser percorrida em um dia.
- `n`: quantidade de pontos de parada disponiveis.
- `x1 ... xn`: distancias dos pontos de parada em relacao ao inicio.

Nesta implementacao, os valores da entrada sao inteiros. Os pontos podem estar
fora de ordem; a implementacao ordena os valores antes de executar o algoritmo.

## Formato da saida

O programa imprime uma resposta explicada, mostrando a quantidade minima de
paradas e quais pontos foram escolhidos para acampar. Se nao existir uma rota
valida, ele mostra uma mensagem informando isso.

## Execucao

Para executar:

```bash
python rally.py
```

## Exemplo

Ao rodar:

```bash
python rally.py
```

Digite os valores pedidos no terminal:

```text
Digite o comprimento total da trilha (L):
25
Digite a distancia maxima que pode andar por dia (d):
10
Digite a quantidade de pontos de parada (n):
6
Digite as posicoes dos pontos de parada, separadas por espaco:
4 8 10 14 19 23
```

Saida:

```text
Resultado:
Quantidade minima de paradas: 2
Pontos escolhidos para acampar: 10 19
```

Nesse exemplo, a rota escolhida e `0 -> 10 -> 19 -> 25`.
