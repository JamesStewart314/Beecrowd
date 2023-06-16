list = [None] * 3
for i in range(3):
    list[i] = input().lower()
tipo1 = list[0]
tipo2 = list[1]
tipo3 = list[2]
if tipo1 == 'vertebrado':
    if tipo2 == 'mamifero':
        if tipo3 == 'onivoro':
            print('homem')
        if tipo3 == 'herbívoro':
            print('vaca')
    if tipo2 == 'ave':
        if tipo3 == 'carnivoro':
            print('aguia')
        if tipo3 == 'onivoro':
            print('pomba')
if tipo1 == 'invertebrado':
    if tipo2 == 'inseto':
        if tipo3 == 'hematofago':
            print('pulga')
        if tipo3 == 'herbivoro':
            print('lagarta')
    if tipo2 == 'anelideo':
        if tipo3 == 'hematofago':
            print('sanguessuga')
        if tipo3 == 'onivoro':
            print('minhoca')