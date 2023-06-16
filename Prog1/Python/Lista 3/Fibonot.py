K = int(input())
if K >= 6:
    fib = [1, 1]
    for z in range(2, K+2):
            fib.append(fib[z-1]+fib[z-2])
    seqn = list(range(1, K*2-1))
    print(seqn)
    for i in range(1, len(fib)):
        if fib[i] <= seqn[len(seqn)-1]:
            seqn.remove(fib[i])
    print(seqn)
else:
    dem = [4, 6, 7, 9, 10]
    print(dem[K-1])