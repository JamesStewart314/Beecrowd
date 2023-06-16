chave = True
while True:
    testes = int(input())
    if testes == 0:
        break
    espaco = 0
    nomes = []
    for i in range(testes):
        nome = input()
        ln = len(nome)
        if ln > espaco:
            espaco = ln
        nomes.append(nome)
    if chave is False:
        print()
    chave = False
    for nome in nomes:
        print(nome.rjust(espaco))