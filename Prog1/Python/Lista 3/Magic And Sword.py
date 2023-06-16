T = int(input())
z = 0
while z < T:
    w, h, x0, y0 = map(int, input().split())
    magia, N, cx, cy = map(str, input().split())
    N, cx, cy = int(N), int(cx), int(cy)
    z += 1

    def raio(mg, n):
        if mg == 'fire':
            lvl = [20, 30, 50]
            return [lvl[n-1], 200]
        if mg == 'water':
            lvl = [10, 25, 40]
            return [lvl[n-1], 300]
        if mg == 'earth':
            lvl = [25, 55, 70]
            return [lvl[n-1], 400]
        if mg == 'air':
            lvl = [18, 38, 60]
            return [lvl[n-1], 100]

    radius = raio(magia, N)[0]
    dano = raio(magia, N)[1]
    canto_inf_esq = [x0, y0]
    canto_sup_esq = [x0, y0 + h]
    canto_inf_dir = [x0 + w, y0]
    canto_sup_dir = [x0 + w, y0 + h]

    def distancia(x1, y1, x2, y2):
        return pow((x2-x1)**2 + (y2 - y1)**2, 1/2)

    if distancia(canto_inf_esq[0], canto_inf_esq[1], cx, cy) <= radius:
        print(dano)
    else:
        if distancia(canto_sup_esq[0], canto_sup_esq[1], cx, cy) <= radius:
            print(dano)
        else:
            if distancia(canto_inf_dir[0], canto_inf_dir[1], cx, cy) <= radius:
                print(dano)
            else:
                if distancia(canto_sup_dir[0], canto_sup_dir[1], cx, cy) <= radius:
                    print(dano)
                else:
                    if (canto_inf_esq[0] - radius) <= cx <= (canto_inf_dir[0] + radius) and canto_inf_dir[1] <= cy <= canto_sup_dir[1]:
                        print(dano)
                    else:
                        if canto_inf_esq[0] <= cx <= canto_inf_dir[0] and (canto_inf_esq[1] - radius) <= cy <= (canto_sup_esq[1] + radius):
                            print(dano)
                        else:
                            print(0)