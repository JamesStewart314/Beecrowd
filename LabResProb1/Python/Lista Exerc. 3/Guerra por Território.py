territorios = int(input())
seq = list(map(int, input().split()))
obj = sum(seq) / 2
comparador = 0
w = 0
while True:
    comparador += seq[w]
    w += 1
    if comparador == obj:
        break
print(w)