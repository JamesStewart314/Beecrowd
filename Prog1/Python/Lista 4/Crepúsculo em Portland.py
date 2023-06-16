n = int(input())
matrizes = []
for i in range(n+1):
    matrizes.append(list(map(int, input().split())))


def seguranca(m1, m2):
    resp = []
    for z in range(n):
        matriz_comp = [matrizes[m1][z], matrizes[m1][z+1], matrizes[m2][z], matrizes[m2][z+1]]
        if matriz_comp.count(1) > 1:
            resp.append('S')
            matriz_comp.clear()
        else:
            resp.append('U')
            matriz_comp.clear()
    return "".join(resp)

for z in range(n):
    print(seguranca(z, z+1))