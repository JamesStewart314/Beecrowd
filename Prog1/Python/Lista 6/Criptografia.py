def Conversor(frase):
    resposta1 = ""
    for letra in frase:
        asc = ord(letra)
        if 65 <= asc <= 90 or 97 <= asc <= 122:
            resposta1 += chr(asc + 3)
        else:
            resposta1 += letra
    resposta1 = resposta1[::-1]
    resposta2 = resposta1[:int(len(frase) / 2)]
    for i in range(int(len(frase) / 2), len(frase)):
        asc = ord(resposta1[i])
        resposta2 += chr(asc - 1)
    return resposta2


testes = int(input())
for i in range(testes):
    print(Conversor(input()))