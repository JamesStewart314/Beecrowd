fib = [0, 1]
valores = []
z = 0
t = int(input())
for i in range(t):
    valores.append(int(input()))
while len(fib) < max(valores) + 1:
    fib.append(fib[z] + fib[z+1])
    z += 1
for n in range(t):
    print(f'Fib({valores[n]}) =', fib[valores[n]])