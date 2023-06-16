overflow = int(input())
op = input().split()
P = int(op[0])
Q = int(op[2])
C = op[1]
if C == '+':
    if P+Q > overflow:
        print('OVERFLOW')
    else:
        print('OK')
else:
    if P*Q > overflow:
        print('OVERFLOW')
    else:
        print('OK')