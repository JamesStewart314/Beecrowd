while True:
    alunos_1 = int(input())
    if alunos_1 == 0:
        break
    alunos = []
    assinaturas = []
    for z1 in range(alunos_1):
        prova = input().split()
        alunos.append(prova[0])
        assinaturas.append(prova[1])
    alunos_2 = int(input())
    ass_falsas = 0
    for z2 in range(alunos_2):
        teste = input().split()
        diferencas = 0
        for k in range(len(teste[1])):
            if assinaturas[alunos.index(teste[0])][k] != teste[1][k]:
                diferencas += 1
        if diferencas > 1:
            ass_falsas += 1
    print(ass_falsas)