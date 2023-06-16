z = True
while True:
    try:
        text = str(input())
    except EOFError:
        break

    if z is False:
        print('')
    lista_letras = [*text]
    lista_letras_sem_rep = list(set(lista_letras))
    resp = []
    for i in range(len(lista_letras_sem_rep)):
        resp.append(str(f'{ord(lista_letras_sem_rep[i])}'
                        f' {lista_letras.count(lista_letras_sem_rep[i])}'))
    resp.sort(key=lambda a: (int(a.split()[1]), -int(a.split()[0])))
    for z in resp:
        print(z)
    z = False