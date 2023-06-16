testes = int(input())
copos_queb = 0
for i in range(testes):
    bandeja = list(map(int, input().split()))
    if bandeja[0] > bandeja[1]:
        copos_queb += bandeja[1]
print(copos_queb)