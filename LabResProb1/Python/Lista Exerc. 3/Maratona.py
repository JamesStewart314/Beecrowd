qt_postos, dist_max = map(int, input().split())
postos = input().split()
postos.extend(['42195'])
resp = 'S'
for i in range(qt_postos + 1):
    dist = int(postos[i]) - int(postos[i - 1])
    if dist > dist_max:
        resp = 'N'
        break
print(resp)