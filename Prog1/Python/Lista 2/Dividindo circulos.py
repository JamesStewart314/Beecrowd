from math import comb
N = int(input())
if N < 4:
    if N == 1:
        print(1)
    if N == 2:
        print(2)
    if N == 3:
        print(4)
else:
    valor = comb(N, 4) + comb(N, 2) + 1
    print(valor)
