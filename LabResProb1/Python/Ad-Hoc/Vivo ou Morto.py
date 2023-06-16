n = 1
while True:
    testes = tuple(map(int, input().split()))
    if testes[0] == testes[1] == 0:
        break
    valores = list(map(int, input().split()))
    for i in range(testes[1]):
        comando = list(map(int, input().split()))
        jogadores = comando[2:]
        remover = []
        for z in range(len(jogadores)):
            if jogadores[z] != comando[1]:
                remover.append(valores[z])
        for w in remover:
            valores.remove(w)
    print(f'Teste {n}\n'
          f'{valores[0]}\n')
    n += 1