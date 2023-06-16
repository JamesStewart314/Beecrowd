testes = int(input())


def up(matriz_teste):
    for i in range(3):
        contador = -1
        for z in matriz_teste[i]:
            contador += 1
            if z == 0:
                for z in range(i, 4):
                    if matriz_teste[z][contador] != 0:
                        return True
    return False


def left(matriz_teste):
    for i in range(4):
        contador = -1
        for i1 in range(3):
            contador += 1
            if matriz_teste[i][i1] == 0:
                for i2 in matriz_teste[i][contador:]:
                    if i2 != 0:
                        return True
    return False


def down(matriz_teste):
    for i in range(1, 4):
        contador = -1
        for i1 in matriz_teste[i]:
            contador += 1
            if i1 == 0:
                for z in range(i):
                    if matriz_teste[z][contador] != 0:
                        return True
    return False


def right(matriz_teste):
    for i in range(4):
        for i1 in range(3):
            if matriz_teste[i][i1] != 0:
                for z in range(i1+1, 4):
                    if matriz_teste[i][z] == 0:
                        return True
    return False


for i in range(testes):
    matriz = []
    resposta = []
    soma = 0
    zero = False
    up_and_down = False
    left_and_right = False
    bloco_vit = False
    lista_comp = [-1, -1, -1, -1]
    for i1 in range(4):
        linha = list(map(int, input().split()))
        soma += sum(linha)
        for j in linha:
            if j == 2048:
                bloco_vit = True
        for p in range(4):
            if linha[p] != 0 and lista_comp[p] != 0 and linha[p] == lista_comp[p]:
                up_and_down = True
        lista_comp = [i for i in linha]
        for p1 in range(1, 4):
            if linha[p1-1] != 0 and linha[p1] != 0 and linha[p1-1] == linha[p1]:
                left_and_right = True
        if linha.count(0) != 0:
            zero = True
        matriz.append(linha)
    if soma == 0:
        print('NONE')
    else:
        if bloco_vit is True:
            print('NONE')
        else:
            if zero is True:
                if up_and_down is True:
                    resposta.append('DOWN')
                else:
                    if down(matriz):
                        resposta.append('DOWN')
                if left_and_right is True:
                    resposta.append('LEFT')
                else:
                    if left(matriz):
                        resposta.append('LEFT')
                if left_and_right is True:
                    resposta.append('RIGHT')
                else:
                    if right(matriz):
                        resposta.append('RIGHT')
                if up_and_down is True:
                    resposta.append('UP')
                else:
                    if up(matriz):
                        resposta.append('UP')
                print(" ".join(resposta))
            else:
                if up_and_down is True:
                    resposta.append('DOWN')
                if left_and_right is True:
                    resposta.append('LEFT')
                if left_and_right is True:
                    resposta.append('RIGHT')
                if up_and_down is True:
                    resposta.append('UP')
                if len(resposta) == 0:
                    print('NONE')
                else:
                    print(" ".join(resposta))