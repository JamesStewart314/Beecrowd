matriz = []
while True:
    try:
        dimensoes = tuple(map(int, input().split()))
        jogador = (None, None)
        analog = (None, None)
        chave = True
        for i in range(dimensoes[0]):
            linha = list(map(int, input().split()))
            if chave is True:
                try:
                    p1 = linha.index(1)
                    jogador = (i, p1)
                except ValueError:
                    pass
                try:
                    p2 = linha.index(2)
                    analog = (i, p2)
                except ValueError:
                    pass
                if jogador[0] is not None and analog[0] is not None:
                    chave = False
                matriz.append(linha)
        resposta = abs(jogador[0] - analog[0]) + abs(jogador[1] - analog[1])
        print(resposta)
    except EOFError:
        break
