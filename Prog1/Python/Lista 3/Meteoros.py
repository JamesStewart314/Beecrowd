teste = 1
while True:
    coordenadas = input().split()
    coordenadas = [int(i) for i in coordenadas]
    if coordenadas[0] == coordenadas[1] == coordenadas[2] == coordenadas[3] == 0:
        break
    n = int(input())
    z = 0
    resultado = 0
    meteoros = []
    while z < n:
        meteoros.append(input())
        z += 1
    for i in range(len(meteoros)):
        if coordenadas[0] <= int(meteoros[i].split()[0]) <= coordenadas[2] and coordenadas[3] <= int(meteoros[i].split()[1]) <= coordenadas[1]:
            resultado += 1
    print('Teste', teste)
    print(resultado)
    teste += 1
