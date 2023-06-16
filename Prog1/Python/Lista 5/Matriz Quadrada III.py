while True:
    tamanho = eval(input())
    matriz = []
    if tamanho == 0:
        break
    for k in range(tamanho):
        matriz.append([((2 ** k) * (2 ** i)) for i in range(tamanho)])
    espaco = len(str(matriz[tamanho-1][tamanho-1]))
    for z in matriz:
        for z1 in z:
            z[z.index(z1)] = " " * (espaco - len(str(z1))) + str(z1)
    for z2 in matriz:
        print(" ".join(z2))
    print()