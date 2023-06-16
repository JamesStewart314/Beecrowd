casos_teste = int(input())
for teste in range(casos_teste):
    intervalos = tuple(map(int, input().split()))
    dicionario_trad = dict()
    for w in range(intervalos[0]):
        palavra = input()
        traducao = input()
        dicionario_trad.update({palavra: traducao})
    resposta = []
    for z in range(intervalos[1]):
        frase = input().split()
        resp = ""
        for pal in frase:
            try:
                resp += dicionario_trad[pal] + " "
            except KeyError:
                resp += pal + " "
        resposta.append(resp.strip())

    print(*resposta, sep="\n")
    print()