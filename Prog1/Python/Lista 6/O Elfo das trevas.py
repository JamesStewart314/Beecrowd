t = 1
testes = int(input())
for i in range(testes):
    quant_renas = tuple(map(int, input().split()))
    renas = []
    for r in range(quant_renas[0]):
        renas.append(input())
    renas.sort(key=lambda x: (-int(x.split()[1]), int(x.split()[2]), -float(x.split()[3]), x.split()[0]))
    print('CENARIO {' + str(t) + '}')
    for i in range(quant_renas[1]):
        print(f'{i + 1} - {renas[i].split()[0]}')
    t += 1