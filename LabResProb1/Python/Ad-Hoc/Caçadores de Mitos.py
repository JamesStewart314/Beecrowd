testes = int(input())
casos = []
casos1 = set()
resp = 0
for i in range(testes):
    x, y = map(int, input().split())
    raio = (x, y)
    if len(casos) == len(casos1):
        casos1.add(raio)
        casos.append(raio)
    else:
        resp = 1
print(resp)