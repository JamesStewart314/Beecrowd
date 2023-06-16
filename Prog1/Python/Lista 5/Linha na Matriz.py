L = int(input())
op = input().upper()
matriz = []
soma = 0
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = sum(matriz[L])
if op == 'S':
    print(f'{soma:.1f}')
elif op == 'M':
    print(f'{(soma / 12):.1f}')
