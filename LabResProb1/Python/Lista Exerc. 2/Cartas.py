cartas = list(map(int, input().split()))
cartas1 = cartas.copy()
cartas1.sort()
cartas2 = cartas1.copy()
cartas2.reverse()
if cartas == cartas1:
    print('C')
elif cartas == cartas2:
    print('D')
else:
    print('N')