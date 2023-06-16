casos = tuple(map(int, input().split()))
cabines_visit = set(map(int, input().split()))
resp = ""
for i in range(casos[0]):
    teste = int(input())
    if teste in cabines_visit:
        resp += "0"
    else:
        cabines_visit.add(teste)
        resp += "1"
print(*resp, sep="\n")