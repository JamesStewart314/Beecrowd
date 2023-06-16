vl = list(map(float, input().split()))
vl.sort(reverse=True)
A, B, C = vl[0], vl[1], vl[2]
prod = (A-B)*(A-C)*(B-C)
dif = (A-B) == 0 and (A-C) == 0 and (B-C) == 0
if A >= B + C:
    print('NAO FORMA TRIANGULO')
elif A ** 2 == B ** 2 + C ** 2:
    print('TRIANGULO RETANGULO')
else:
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if prod == 0 and dif is True:
        print('TRIANGULO EQUILATERO')
    if prod == 0 and dif is False:
        print('TRIANGULO ISOSCELES')