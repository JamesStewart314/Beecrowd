while True:
    try:
        n = int(input())
    except EOFError:
        break
    telefones = []
    for i in range(n):
        telefones.append(input())
    soma = 0
    telefones.sort()
    for w in range(n-1):
        for z in range(len(telefones[0])):
            if telefones[w][z] == telefones[w+1][z]:
                soma += 1
            else:
                break
    print(soma)

