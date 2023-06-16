dicio_notas = dict({"W": 1, "H": 1/2, "Q": 1/4, "E": 1/8, "S": 1/16, "T": 1/32, "X": 1/64})

while True:
    jingle = input().strip("/").split("/")
    if jingle[0] == "*":
        break
    resposta = 0
    for notas in jingle:
        comparador = 0
        for i in range(len(notas)):
            comparador += dicio_notas[notas[i]]
            if comparador > 1:
                break
        if comparador == 1:
            resposta += 1
    print(resposta)