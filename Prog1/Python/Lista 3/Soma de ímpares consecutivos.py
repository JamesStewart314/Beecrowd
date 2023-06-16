X = int(input())
Y = int(input())
k = 0
list = []
if min(X, Y) % 2 == 1 and X != Y:
    k = min(X, Y) + 2
    while True:
        if k >= max(X, Y):
            break
        list.append(k)
        k += 2
if min(X, Y) % 2 == 0 and X != Y:
    k = min(X, Y) + 1
    while True:
        if k >= max(X, Y):
            break
        list.append(k)
        k += 2
print(sum(list))
