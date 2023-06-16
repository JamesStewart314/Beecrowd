numeros = []
n = int(input())
for i in range(n):
    numeros.append(int(input()))
numeros_semrep = sorted(list(set(numeros)))
for i in range(len(numeros_semrep)):
    print(f'{numeros_semrep[i]} aparece {numeros.count(numeros_semrep[i])} vez(es)')
