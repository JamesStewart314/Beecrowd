testes = int(input())
for i in range(testes):
    dieta = set(input())
    cafe_manha = input().strip()
    almoco = input().strip()
    union = set(set(cafe_manha) | set(almoco))
    if union.issubset(dieta):
        resposta = list(dieta - union)
        resposta.sort()
        print(*resposta, sep='')
    else:
        print('CHEATER')