X = int(input())
n = 0
if X == 1:
    print(X)
else:
    while True:
        if 2*n+1 > X:
            break
        print(2*n + 1)
        n += 1
