testes = eval(input())
k = 1
for i in range(testes):
    resposta = True
    matriz = []
    teste_colunas = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    sub_teste1 = [set(), set(), set()]
    sub_teste2 = [set(), set(), set()]
    sub_teste3 = [set(), set(), set()]
    for i in range(9):
        if resposta is True:
            linha = list(map(int, input().split()))
            if len(set(linha)) < 9:
                resposta = False
                continue
            matriz.append(linha)
            for p in range(9):
                teste_colunas[p].add(linha[p])
            if i < 3:
                contador2 = 0
                for h in range(3):
                    for h1 in range(3):
                        sub_teste1[h].add(linha[h1+contador2])
                    contador2 += 3
            elif 3 <= i < 6:
                contador2 = 0
                for h in range(3):
                    for h1 in range(3):
                        sub_teste2[h].add(linha[h1+contador2])
                    contador2 += 3
            else:
                contador2 = 0
                for h in range(3):
                    for h1 in range(3):
                        sub_teste3[h].add(linha[h1+contador2])
                    contador2 += 3
        else:
            n = input()
    if resposta is False:
        print(f'Instancia {k}')
        print(f'NAO\n')
        k += 1
    else:
        for y in sub_teste1:
            if len(y) < 9:
                resposta = False
            if resposta is False:
                print(f'Instancia {k}')
                print(f'NAO\n')
                k += 1
                break
        if resposta is False:
            continue
        for y1 in sub_teste2:
            if len(y1) < 9:
                resposta = False
            if resposta is False:
                print(f'Instancia {k}')
                print(f'NAO\n')
                k += 1
                break
        if resposta is False:
            continue
        for y2 in sub_teste3:
            if len(y2) < 9:
                resposta = False
            if resposta is False:
                print(f'Instancia {k}')
                print(f'NAO\n')
                k += 1
                break
        if resposta is False:
            continue
        for y in teste_colunas:
            if len(y) < 9:
                resposta = False
            if resposta is False:
                print(f'Instancia {k}')
                print(f'NAO\n')
                k += 1
                break
        if resposta is False:
            continue
        print(f'Instancia {k}')
        print(f'SIM\n')
        k += 1
