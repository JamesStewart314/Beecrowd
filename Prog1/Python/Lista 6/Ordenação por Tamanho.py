testes = int(input())
for i in range(testes):
    strings = input().split()
    strings_ord = sorted(strings, key=lambda x: len(x), reverse=True)
    print(*strings_ord, sep=" ")