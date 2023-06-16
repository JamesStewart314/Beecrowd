while True:
    quantidades = tuple(map(int, input().split()))
    if sum(quantidades) == 0:
        break
    servidores = []
    resposta = 0
    for w1 in range(quantidades[0]):
        servidores.append(set(input()[2:].split()))
    for w2 in range(quantidades[1]):
        cliente = set(input()[2:].split())
        for servidor in servidores:
            if len(cliente - servidor) != len(cliente):
                resposta += 1
    print(resposta)
