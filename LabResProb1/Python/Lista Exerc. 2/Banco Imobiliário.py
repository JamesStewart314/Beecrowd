entrada = list(map(int, input().split()))
jogadores = dict(Dália=entrada[0], Elói=entrada[0], Félix=entrada[0])
for i in range(entrada[1]):
    operacao = input().split()
    for z in operacao:
        if z == 'D':
            operacao[operacao.index(z)] = 'Dália'
        elif z == 'E':
            operacao[operacao.index(z)] = 'Elói'
        elif z == 'F':
            operacao[operacao.index(z)] = 'Félix'
    if operacao[0] == 'C':
        jogadores[f'{operacao[1]}'] = str(int(jogadores[f'{operacao[1]}']) - int(operacao[2]))
    elif operacao[0] == 'V':
        jogadores[f'{operacao[1]}'] = str(int(jogadores[f'{operacao[1]}']) + int(operacao[2]))
    elif operacao[0] == 'A':
        jogadores[f'{operacao[1]}'] = str(int(jogadores[f'{operacao[1]}']) + int(operacao[3]))
        jogadores[f'{operacao[2]}'] = str(int(jogadores[f'{operacao[2]}']) - int(operacao[3]))
print(jogadores['Dália'], jogadores['Elói'], jogadores['Félix'])