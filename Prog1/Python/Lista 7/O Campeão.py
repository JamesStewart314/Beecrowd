while True:
    quant_jogadores = int(input())
    if quant_jogadores == 0:
        break
    jogadores = dict()
    for i in range(quant_jogadores):
        jog = input().split()
        jogadores.update({jog[0]: int(jog[1])})
    for w in range(int(quant_jogadores / 2)):
        partida = input().split()
        pont = partida[1].split("-")
        jogadores[partida[0]] += 3 * int(pont[0])
        jogadores[partida[2]] += 3 * int(pont[1])
        if int(pont[0]) == int(pont[1]):
            jogadores[partida[0]] += 1
            jogadores[partida[2]] += 1
        else:
            if int(pont[0]) > int(pont[1]):
                jogadores[partida[0]] += 5
            else:
                jogadores[partida[2]] += 5

    maximo = 0
    vencedor = None
    for chave in jogadores.keys():
        if jogadores[chave] > maximo:
            maximo = jogadores[chave]
            vencedor = chave

    if vencedor == "Sport":
        print(f'O Sport foi o campeao com {maximo} pontos :D\n')
    else:
        print(f'O Sport nao foi o campeao. O time campeao foi o {vencedor} com {maximo} pontos :(\n')
