count = 1
while True:
    testes = int(input())
    if testes == 0:
        break
    resposta = []
    tabela = []
    seq = []
    for w in range(testes):
        informacoes = input().split()
        tabela.append(dict(A=[informacoes[0], informacoes[1]],
                           B=[informacoes[2], informacoes[3]],
                           C=[informacoes[4], informacoes[5]],
                           D=[informacoes[6], informacoes[7]],
                           E=[informacoes[8], informacoes[9]]))
        seq.append(informacoes[10:])
    valor = None
    for i in range(6):
        for y in range(testes):
            comp1 = tabela[0][seq[0][i]]
            comp2 = tabela[y][seq[y][i]]
            valor = []
            for h in comp1:
                if h in comp2:
                    valor.append(h)
            if len(valor) == 1:
                break
        resposta.append(int(valor[0]))
    print(f'Teste {count}')
    print(f'{resposta[0]} {resposta[1]} {resposta[2]} {resposta[3]} {resposta[4]} {resposta[5]} \n')
    count += 1