def idx(linha):
    start = -1
    locais = []
    while True:
        try:
            local = linha.index(9, start + 1)
        except ValueError:
            break
        locais.append(local)
        start = local
    return locais


def teste_sweeper(matriz, linha, dimA, dimB):
    testes = idx(matriz[linha])
    for i in testes:
        if linha == 0:
            if i == 0:
                if matriz[linha][i + 1] != 9:
                    matriz[linha][i + 1] += 1
                if matriz[linha + 1][i] != 9:
                    matriz[linha + 1][i] += 1
            elif i == dimB - 1:
                if matriz[linha][i - 1] != 9:
                    matriz[linha][i - 1] += 1
                if matriz[linha + 1][i] != 9:
                    matriz[linha + 1][i] += 1
            else:
                if matriz[linha][i + 1] != 9:
                    matriz[linha][i + 1] += 1
                if matriz[linha + 1][i] != 9:
                    matriz[linha + 1][i] += 1
                if matriz[linha][i - 1] != 9:
                    matriz[linha][i - 1] += 1
        elif linha == dimA - 1:
            if i == 0:
                if matriz[linha][i + 1] != 9:
                    matriz[linha][i + 1] += 1
                if matriz[linha - 1][i] != 9:
                    matriz[linha - 1][i] += 1
            elif i == dimB - 1:
                if matriz[linha][i - 1] != 9:
                    matriz[linha][i - 1] += 1
                if matriz[linha - 1][i] != 9:
                    matriz[linha - 1][i] += 1
            else:
                if matriz[linha][i + 1] != 9:
                    matriz[linha][i + 1] += 1
                if matriz[linha - 1][i] != 9:
                    matriz[linha - 1][i] += 1
                if matriz[linha][i - 1] != 9:
                    matriz[linha][i - 1] += 1
        else:
            if i == 0:
                if matriz[linha][i + 1] != 9:
                    matriz[linha][i + 1] += 1
                if matriz[linha - 1][i] != 9:
                    matriz[linha - 1][i] += 1
                if matriz[linha + 1][i] != 9:
                    matriz[linha + 1][i] += 1
            elif i == dimB - 1:
                if matriz[linha][i - 1] != 9:
                    matriz[linha][i - 1] += 1
                if matriz[linha - 1][i] != 9:
                    matriz[linha - 1][i] += 1
                if matriz[linha + 1][i] != 9:
                    matriz[linha + 1][i] += 1
            else:
                if matriz[linha][i - 1] != 9:
                    matriz[linha][i - 1] += 1
                if matriz[linha][i + 1] != 9:
                    matriz[linha][i + 1] += 1
                if matriz[linha - 1][i] != 9:
                    matriz[linha - 1][i] += 1
                if matriz[linha + 1][i] != 9:
                    matriz[linha + 1][i] += 1
    return matriz

while True:
    try:
        dimensoes = tuple(map(int, input().split()))
    except EOFError:
        break
    if dimensoes[0] == 1 or dimensoes[1] == 1:
        if dimensoes[0] == dimensoes[1]:
            n = int(input())
            print(9 * n)
        elif dimensoes[0] == 1:
            n = list(map(lambda x: int(x) * 9, input().split()))
            testes = idx(n)
            for z in testes:
                if z == 0:
                    if n[z + 1] != 9:
                        n[z + 1] += 1
                elif z == dimensoes[1] - 1:
                    if n[z - 1] != 9:
                        n[z - 1] += 1
                else:
                    for i in range(-1, 2, 2):
                        if n[z + i] != 9:
                            n[z + i] += 1
            print(*n, sep="")
        else:
            n = []
            for i in range(dimensoes[1]):
                n.append(int(input()) * 9)
            testes = idx(n)
            for z in testes:
                for i in range(-1, 2, 2):
                    if n[z + i] != 9:
                        n[z + i] += 1
            for z in n:
                print(z)
    else:
        matriz = []
        for i in range(dimensoes[0]):
            linha = list(map(lambda x: int(x) * 9, input().split()))
            matriz.append(linha)
            if i >= 1:
                matriz = teste_sweeper(matriz, i-1, dimensoes[0], dimensoes[1])
        matriz = teste_sweeper(matriz, dimensoes[0]-1, dimensoes[0], dimensoes[1])
        for z in matriz:
            print(*z, sep="")
