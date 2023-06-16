testes = int(input())
for w in range(testes):
    resposta = ''
    frase = input()
    chave = True
    for caractere in frase:
        if caractere == ' ':
            chave = True
        else:
            if chave is True:
                resposta += caractere
                chave = False
    print(resposta)