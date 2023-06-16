casos_teste = int(input())
for i in range(casos_teste):
    quat_alunos = int(input())
    alunos = tuple(input().split())
    presenca = tuple(input().split())
    contador = 0
    resposta = []
    for chave in alunos:
        z = presenca[contador]
        w1 = z.count('A')
        w2 = z.count('P')
        if w2 / (w1 + w2) < 0.75:
            resposta.append(chave)
        contador += 1
    print(*resposta, sep=" ")
