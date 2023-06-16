bits = input()
soma = sum(list(map(int, bits)))
if soma % 2 == 0:
    print(bits + '0')
else:
    print(bits + '1')