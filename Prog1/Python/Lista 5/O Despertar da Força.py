def idx(linha):
    locais = []
    start = 1
    while True:
        try:
            local = linha.index(42, start)
        except ValueError:
            return locais
        if local != dimensoes[1] - 1:
            locais.append(local)
        start = local + 1


def teste_sabre(matriz, linha):
    global resposta
    testes = idx(matriz[linha])
    simp = matriz[linha]
    simp2 = matriz[linha + 1]
    simp3 = matriz[linha - 1]
    for z in testes:
        if simp[z - 1] == simp[z + 1] == simp2[z - 1] == simp2[z] == simp2[z + 1] == simp3[z - 1] == simp3[z] == simp3[z + 1] == 7:
            resposta = (linha + 1, z + 1)
            return True
    return False


matriz = []
chave = True
resposta = (0, 0)
valor = False
dimensoes = tuple(map(int, input().split()))
for i in range(dimensoes[0]):
    matriz.append(list(map(int, input().split())))
break_flag = False
for i in range(1, dimensoes[0] - 1):
    if matriz[i].count(42) != 0:
        if teste_sabre(matriz, i):
            break
print(*resposta, sep=" ")