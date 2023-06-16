matring = []
resposta = ""
chave_1 = ""
chave_2 = ""
linha = input()
colunas = len(linha)
matring.append(linha)

for w in range(3):
    matring.append(input())

for w1 in range(4):
    chave_1 += matring[w1][0]
    chave_2 += matring[w1][colunas - 1]

chave_1 = int(chave_1)
chave_2 = int(chave_2)

for z1 in range(1, colunas - 1):
    numero = ""
    for z2 in range(4):
        numero += matring[z2][z1]
    numero = int(numero)
    resposta += chr((chave_1 * numero + chave_2) % 257)

print(resposta)
