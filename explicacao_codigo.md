# Explicacao do Codigo

Este arquivo explica o funcionamento do programa `rally.py`, que resolve o
problema do rally usando um algoritmo guloso.

## Ideia principal

O objetivo do programa e escolher o menor numero de pontos de parada para
conseguir sair do inicio da trilha e chegar ate o final.

A estrategia usada e:

> A cada dia, ir ate o ponto mais distante possivel que ainda esteja dentro da
> distancia maxima permitida.

Essa e uma estrategia gulosa, pois em cada passo o algoritmo faz a melhor escolha
local: andar o maximo possivel naquele momento.

## Funcao `escolher_paradas`

A funcao principal do algoritmo e:

```python
def escolher_paradas(L, d, pontos):
```

Ela recebe:

- `L`: comprimento total da trilha;
- `d`: distancia maxima que pode ser percorrida em um dia;
- `pontos`: lista com as posicoes dos pontos de parada.

Exemplo:

```python
L = 25
d = 10
pontos = [4, 8, 10, 14, 19, 23]
```

Nesse exemplo, a trilha tem tamanho `25`, o grupo anda no maximo `10` por dia e
os pontos de parada estao nas posicoes `4, 8, 10, 14, 19 e 23`.

## Ordenando os pontos

Logo no inicio da funcao:

```python
pontos.sort()
```

Essa linha coloca os pontos em ordem crescente.

Isso e importante porque a trilha e representada como uma linha, entao precisamos
analisar os pontos do inicio para o final.

Depois disso:

```python
pontos = [0] + pontos + [L]
```

O codigo adiciona:

- `0`, que representa o inicio da trilha;
- `L`, que representa o final da trilha.

Com o exemplo anterior, a lista fica assim:

```python
[0, 4, 8, 10, 14, 19, 23, 25]
```

## Guardando a resposta

Em seguida:

```python
paradas = []
atual = 0
```

`paradas` guarda os pontos escolhidos para acampar.

`atual` indica em qual posicao da lista `pontos` o grupo esta. No inicio,
`atual = 0`, ou seja, o grupo esta no ponto `0`, o inicio da trilha.

## Laco principal

O laco principal e:

```python
while atual < len(pontos) - 1:
```

Esse laco continua enquanto o grupo ainda nao chegou ao ultimo ponto da lista,
que e o final da trilha.

Dentro dele, o codigo comeca assim:

```python
proximo = atual
```

Isso significa que, inicialmente, o proximo ponto alcancavel e o proprio ponto
atual.

## Escolha gulosa

A parte mais importante do algoritmo e:

```python
while proximo + 1 < len(pontos) and pontos[proximo + 1] - pontos[atual] <= d:
    proximo += 1
```

Essa parte tenta avancar o maximo possivel.

Ela verifica se o ponto seguinte ainda pode ser alcancado a partir do ponto atual.
Se puder, o algoritmo avanca para esse ponto.

Com o exemplo:

```python
pontos = [0, 4, 8, 10, 14, 19, 23, 25]
d = 10
atual = 0
```

O algoritmo testa:

```text
4 - 0 = 4, pode
8 - 0 = 8, pode
10 - 0 = 10, pode
14 - 0 = 14, nao pode
```

Entao a melhor escolha local e parar em `10`, pois e o ponto mais distante
alcancavel naquele dia.

## Caso impossivel

Depois da busca pelo proximo ponto, existe este teste:

```python
if proximo == atual:
    return None
```

Se `proximo` continuou igual a `atual`, significa que o grupo nao conseguiu
avancar para nenhum ponto.

Exemplo:

```python
L = 25
d = 10
pontos = [15, 20]
```

Saindo do inicio `0`, o primeiro ponto esta em `15`, mas:

```text
15 - 0 = 15
```

Como `15 > 10`, nao da para chegar ate ele em um dia. Nesse caso, o programa
retorna `None`, indicando que nao existe rota valida.

## Adicionando uma parada

Se o ponto encontrado nao for o final da trilha, ele e adicionado na resposta:

```python
if proximo < len(pontos) - 1:
    paradas.append(pontos[proximo])
```

No exemplo principal, o primeiro ponto escolhido e `10`, entao:

```python
paradas = [10]
```

Depois, o codigo atualiza a posicao atual:

```python
atual = proximo
```

Agora o algoritmo passa a repetir o mesmo processo a partir do ponto `10`.

## Continuando o exemplo

A partir de `10`, com `d = 10`, o algoritmo testa:

```text
14 - 10 = 4, pode
19 - 10 = 9, pode
23 - 10 = 13, nao pode
```

Entao escolhe `19`.

Agora:

```python
paradas = [10, 19]
```

A partir de `19`, ele consegue chegar ao final:

```text
25 - 19 = 6, pode
```

Como `25` e o final da trilha, ele nao e adicionado como ponto de acampamento.

Resultado final:

```python
[10, 19]
```

## Entrada de dados

A funcao `main` comeca perguntando os valores ao usuario:

```python
print("Digite o comprimento total da trilha (L):")
L = int(input())
```

Depois pede a distancia maxima por dia:

```python
print("Digite a distancia maxima que pode andar por dia (d):")
d = int(input())
```

Depois pede a quantidade de pontos:

```python
print("Digite a quantidade de pontos de parada (n):")
n = int(input())
```

Se existirem pontos de parada, o programa le a lista:

```python
if n > 0:
    print("Digite as posicoes dos pontos de parada, separadas por espaco (exemplo: 3 4 9 14 19 23 28):")
    pontos = list(map(int, input().split()))
```

## Chamando o algoritmo

Depois de ler os dados, o programa chama:

```python
resposta = escolher_paradas(L, d, pontos)
```

Essa linha executa o algoritmo guloso e guarda a resposta.

## Saida do programa

Se a resposta for `None`, o programa mostra:

```python
print("Nao existe uma rota valida com esses pontos de parada.")
```

Caso contrario, mostra a quantidade minima de paradas:

```python
print("Quantidade minima de paradas:", len(resposta))
```

Se nao precisar parar, mostra:

```python
print("Pontos escolhidos: nenhum, pois da para chegar direto ao final.")
```

Se precisar parar, mostra os pontos escolhidos:

```python
print("Pontos escolhidos para acampar:", *resposta)
```

## Exemplo completo

Entrada digitada no terminal:

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

Isso significa que a rota escolhida foi:

```text
0 -> 10 -> 19 -> 25
```

## Por que o algoritmo e guloso?

Ele e guloso porque, em cada passo, escolhe o ponto mais distante que ainda pode
ser alcancado naquele dia.

Ele nao testa todas as combinacoes possiveis de paradas. Ele simplesmente faz a
melhor escolha local e segue em frente.

A escolha gulosa aparece principalmente neste trecho:

```python
while proximo + 1 < len(pontos) and pontos[proximo + 1] - pontos[atual] <= d:
    proximo += 1
```

Esse trecho faz o algoritmo andar ate o ultimo ponto possivel antes de precisar
acampar.

## Tempo de execucao

O tempo de execucao do algoritmo depende principalmente de duas partes do codigo.

Primeiro, o programa ordena os pontos de parada:

```python
pontos.sort()
```

Essa ordenacao tem custo:

```text
O(n log n)
```

Aqui, `n` representa a quantidade de pontos de parada.

Depois disso, o algoritmo percorre a lista procurando sempre o ponto mais
distante que ainda pode ser alcancado:

```python
while atual < len(pontos) - 1:
    proximo = atual

    while proximo + 1 < len(pontos) and pontos[proximo + 1] - pontos[atual] <= d:
        proximo += 1
```

Mesmo tendo dois `while`, essa parte nao vira `O(n^2)`. O motivo e que o
algoritmo avanca pelos pontos da esquerda para a direita, sem ficar testando
todas as combinacoes possiveis de paradas. Assim, a etapa gulosa tem custo:

```text
O(n)
```

Como a ordenacao custa `O(n log n)` e a parte gulosa custa `O(n)`, o tempo total
da implementacao é:

```text
O(n log n)
```

Se os pontos ja viessem ordenados na entrada, nao seria necessario usar:

```python
pontos.sort()
```

Nesse caso, o algoritmo guloso em si teria tempo:

```text
O(n)
```
