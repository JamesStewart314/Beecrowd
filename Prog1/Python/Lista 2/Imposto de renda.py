sal = float(input())
if sal <= 2000:
    print('Isento')
else:
    if sal <= 3000:
        print('R$ {:.2f}'.format((sal-2000)*8 / 100))
    if 3000 < sal <= 4500:
        print('R$ {:.2f}'.format((1000 * 8 / 100) + (sal-3000)*18/100))
    if sal > 4500:
        print('R$ {:.2f}'.format((1000 * 8 / 100) + 1500*18/100 + (sal - 4500)*28/100))
