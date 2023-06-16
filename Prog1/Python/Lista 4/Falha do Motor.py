n = int(input())
velocidades = list(map(int, input().split()))
queda = 0
for i in range(n-1):
    if velocidades[i+1] - velocidades[i] >= 0:
        queda = 0
    else:
        queda = i + 2
        break
print(queda)