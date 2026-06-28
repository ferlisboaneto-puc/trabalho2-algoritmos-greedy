def escolher_paradas(L, d, pontos):
    pontos.sort()
    pontos = [0] + pontos + [L]

    paradas = []
    atual = 0

    while atual < len(pontos) - 1:
        proximo = atual

        while proximo + 1 < len(pontos) and pontos[proximo + 1] - pontos[atual] <= d:
            proximo += 1

        if proximo == atual:
            return None

        if proximo < len(pontos) - 1:
            paradas.append(pontos[proximo])

        atual = proximo

    return paradas


def main():
    print("Digite o comprimento total da trilha (L):")
    L = int(input())

    print("Digite a distancia maxima que pode andar por dia (d):")
    d = int(input())

    print("Digite a quantidade de pontos de parada (n):")
    n = int(input())

    pontos = []
    if n > 0:
        print("Digite as posicoes dos pontos de parada, separadas por espaco (exemplo: 3 4 9 14 19 23 28):")
        pontos = list(map(int, input().split()))

    resposta = escolher_paradas(L, d, pontos)

    print()
    print("Resultado:")

    if resposta is None:
        print("Nao existe uma rota valida com esses pontos de parada.")
    else:
        print("Quantidade minima de paradas:", len(resposta))

        if len(resposta) == 0:
            print("Pontos escolhidos: nenhum, pois da para chegar direto ao final.")
        else:
            print("Pontos escolhidos para acampar:", *resposta)


main()
