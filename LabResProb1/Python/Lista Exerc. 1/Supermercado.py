entrada = int(input())
minimo = 1_000_000
for i in range(entrada):
    preco = list(map(float, input().split()))
    if (1000*(preco[0]))/preco[1] < minimo:
        minimo = (1000*(preco[0]))/preco[1]
print(f'{minimo:.2f}')