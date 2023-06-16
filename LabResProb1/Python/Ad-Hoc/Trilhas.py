linhas = int(input())
trilhas = []
comparacoes = []
for i in range(linhas):
    trilhas.append(list(map(int, input().split())))
for z in range(linhas):
    a = 0
    b = 0
    c = trilhas[z][0]
    for w in range(1, c):
        if trilhas[z][w] < trilhas[z][w+1]:
            a += trilhas[z][w+1] - trilhas[z][w]
    trilhas[z].reverse()
    for y in range(0, c-1):
        if trilhas[z][y] < trilhas[z][y+1]:
            b += trilhas[z][y+1] - trilhas[z][y]
    comparacoes.append(min(a, b))
print(comparacoes.index(min(comparacoes))+1)
