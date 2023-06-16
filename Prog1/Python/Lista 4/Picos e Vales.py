n = int(input())
valores = list(map(int, input().split()))
variacoes = []
resp = 1
for i in range(1, n):
    if valores[i-1] < valores[i]:
        variacoes.append('pos')
    if valores[i-1] > valores[i]:
        variacoes.append('neg')
    if valores[i-1] == valores[i]:
        variacoes.append('nulo')
for i in range(1, n):
    if n == 2:
        if variacoes.count('nulo') != 0:
            resp = 0
            break
        else:
            resp = 1
            break
    else:
        if i <= len(variacoes) - 1:
            if variacoes.count('nulo') != 0:
                resp = 0
                break
            if variacoes[i - 1] != variacoes[i]:
                resp = resp
            else:
                resp = 0
                break
print(resp)
