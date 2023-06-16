def escada(colunas, somatorio):
    resultado = float((-1 + pow(1 + 8 * somatorio, 1/2)) / 2)
    teste_inteiro = resultado - int(resultado)
    if teste_inteiro == 0 and resultado == colunas:
        return True
    else:
        return False


colunas = int(input())
if colunas == 0:
    exit()
else:
    valores = list(map(int, input().split()))
    min_valores = min(valores)
    if min_valores > 1:
        quad_sub = min_valores - 1
        linha_sub = colunas * quad_sub
        soma = sum(valores) - linha_sub
        if escada(colunas, soma) is True:
            resposta = 0
            for z in range(colunas):
                mini_escada = (valores[z] - quad_sub) - (z+1)
                if mini_escada >= 0:
                    resposta += mini_escada
            print(resposta)
        else:
            print(-1)
    else:
        soma = sum(valores)
        if escada(colunas, soma) is True:
            resposta = 0
            for z in range(colunas):
                mini_escada = valores[z] - (z+1)
                if mini_escada >= 0:
                    resposta += mini_escada
            print(resposta)
        else:
            print(-1)

