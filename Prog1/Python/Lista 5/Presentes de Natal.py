while True:
    netos = eval(input())
    if netos == 0:
        break
    valores = list(map(int, input().split()))
    if netos == 1:
        a = sum(valores)
        print(a, a)
    elif netos == 2:
        resposta = set()
        resposta.add(valores[0]+valores[3])
        resposta.add(valores[1]+valores[2])
        print(f'{max(resposta)} {min(resposta)}')
    else:
        minimo = 2 * 10 ** 8
        maximo = 0
        for i in range(0, netos):
            if valores[i] + valores[2*netos-1-i] < minimo:
                minimo = valores[i] + valores[2*netos-1-i]
            if valores[i] + valores[2*netos-1-i] > maximo:
                maximo = valores[i] + valores[2*netos-1-i]
        print(f'{maximo} {minimo}')