def combinador(string):
    palavras = string.split()
    minimo = min(len(palavras[0]), len(palavras[1]))
    resposta = ""
    for w in range(minimo):
        resposta += palavras[0][w]
        resposta += palavras[1][w]
    if len(palavras[0]) == len(palavras[1]):
        return resposta
    else:
        if len(palavras[0]) > len(palavras[1]):
            resposta += palavras[0][minimo:]
        else:
            resposta += palavras[1][minimo:]
        return resposta


testes = int(input())
for i in range(testes):
    print(combinador(input()))