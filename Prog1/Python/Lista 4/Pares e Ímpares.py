valores = []
n = int(input())
for i in range(n):
    valores.append(int(input()))
valores_pares = [i for i in valores if i % 2 == 0]
valores_impares = [i for i in valores if i % 2 == 1]
valores_pares.sort()
valores_impares.sort(reverse=True)
for z in range(len(valores_pares)):
    print(valores_pares[z])
for z in range(len(valores_impares)):
    print(valores_impares[z])
