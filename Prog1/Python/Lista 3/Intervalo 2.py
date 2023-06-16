N = int(input())
lista = [None]*N
count = 0
for i in range(N):
    k = int(input())
    if 10 <= k <= 20:
        count += 1
    lista[i] = k
print(f'''{count} in
{len(lista)-count} out''')
