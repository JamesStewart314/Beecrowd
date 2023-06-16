teste = 1
while True:
    partidas = eval(input())
    if partidas == 0:
        break
    jogadores = []
    vencedores = []
    for i in range(2):
        jogadores.append(str(input()))
    for z in range(partidas):
        jogo = tuple(map(int, input().split()))
        if sum(jogo) % 2 == 0:
            vencedores.append(jogadores[0])
        else:
            vencedores.append(jogadores[1])
    print(f'Teste {teste}')
    teste += 1
    for w in vencedores:
        print(w)
    print()