n, i, f = map(float, input().split())
n = int(n)
lista = list(map(int, input().split()))
count = 0
for z in range(n):
    for w in range(z+1, n):
        if i <= lista[z] + lista[w] <= f:
            count += 1
print(count)