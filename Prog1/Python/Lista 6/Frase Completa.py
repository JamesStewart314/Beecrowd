casos_teste = int(input())
for i in range(casos_teste):
    frase = {*input()}
    if " " in frase:
        frase.remove(" ")
    if "," in frase:
        frase.remove(",")
    tamanho = len(frase)
    if tamanho == 26:
        print('frase completa')
    elif tamanho >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')