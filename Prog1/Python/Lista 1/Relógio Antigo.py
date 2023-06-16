while True:
    try:
        h, m = map(int, input().split())
    except EOFError:
        break
    tempo = 120*h + 10*m
    print('{:0>2}:{:0>2}'.format((tempo//3600) % 12, (tempo//60) % 60))