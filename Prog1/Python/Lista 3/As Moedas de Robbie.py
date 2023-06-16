while True:
    try:
        qtd = int(input())
        valores = [None]*qtd
        for z in range(qtd):
            valores[z] = int(input())
        salto = int(input())
    except EOFError:
        break
    lista_salto = []
    for i in range(0, qtd, salto):
        lista_salto.append(valores[(qtd-1) - i])

    def primo(x):
        restos = []
        if x > 2:
            for z in range(2, x):
                restos.append(x % z)
        elif x == 1:
            return 'Bad boy! I’ll hit you.'
        elif x == 2:
            return 'You’re a coastal aircraft, Robbie, a large silver aircraft.'
        else:
            restos.append(0)
        if restos.count(0) == 0:
            return 'You’re a coastal aircraft, Robbie, a large silver aircraft.'
        if restos.count(0) > 0:
            return 'Bad boy! I’ll hit you.'
    print(primo(sum(lista_salto)))