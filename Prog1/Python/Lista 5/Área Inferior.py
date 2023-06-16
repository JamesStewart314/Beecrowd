operacao = input().upper()
matriz = []
for i in range(12):
    lista_aux = []
    for i1 in range(12):
        lista_aux.append(eval(input()))
    matriz.append(lista_aux)
somatorio = 0
for z in range(1, 6):
    for z1 in range(z, 12 - z):
        somatorio += matriz[12 - z][z1]
if operacao == 'S':
    print(f'{somatorio:.1f}')
elif operacao == 'M':
    print(f'{(somatorio / 30):.1f}')