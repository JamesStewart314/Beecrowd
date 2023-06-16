loop = int(input())
valores = []
acum = 1
for i in range(loop):
    valores.append(int(input()))
a = valores[0]
for z in range(1, loop):
    if a != valores[z]:
        a = valores[z]
        acum += 1
print(acum)
