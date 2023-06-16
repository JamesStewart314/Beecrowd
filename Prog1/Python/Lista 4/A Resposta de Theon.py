n = int(input())
valores = list(map(int, input().split()))
valor_min = sorted(valores)[0]
print(valores.index(valor_min) + 1)