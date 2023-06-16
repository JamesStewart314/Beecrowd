def teste_real(tempo_voo, fuso_horario):
    global pa, cb, pb, ca, dia
    if (pa + tempo_voo + 60 * fuso_horario) % dia == cb and (pb + tempo_voo - 60 * fuso_horario) % dia == ca:
        return True
    else:
        return False


def casos_pos():
    global pa, cb, pb, ca, dia
    tempo_de_voo = dia
    fuso_horario = None
    a = (cb - pa) % dia
    b = (ca - pb) % dia
    t_voo, fuso = ((a + b) / 2, (a - b) / 120)
    if teste_real(t_voo, fuso) and 0 <= t_voo < tempo_de_voo and -11 <= fuso <= 12:
        tempo_de_voo = t_voo
        fuso_horario = fuso
    a -= dia
    t_voo, fuso = ((a + b) / 2, (a - b) / 120)
    if teste_real(t_voo, fuso) and 0 <= t_voo < tempo_de_voo and -11 <= fuso <= 12:
        tempo_de_voo = t_voo
        fuso_horario = fuso
    a += dia
    b -= dia
    t_voo, fuso = ((a + b) / 2, (a - b) / 120)
    if teste_real(t_voo, fuso) and 0 <= t_voo < tempo_de_voo and -11 <= fuso <= 12:
        tempo_de_voo = t_voo
        fuso_horario = fuso
    a -= dia
    t_voo, fuso = ((a + b) / 2, (a - b) / 120)
    if teste_real(t_voo, fuso) and 0 <= t_voo < tempo_de_voo and -11 <= fuso <= 12:
        tempo_de_voo = t_voo
        fuso_horario = fuso
    return int(tempo_de_voo), int(fuso_horario)

horarios = input().split()
pa = int(horarios[0].split(":")[0]) * 60 + int(horarios[0].split(":")[1])
cb = int(horarios[1].split(":")[0]) * 60 + int(horarios[1].split(":")[1])
pb = int(horarios[2].split(":")[0]) * 60 + int(horarios[2].split(":")[1])
ca = int(horarios[3].split(":")[0]) * 60 + int(horarios[3].split(":")[1])
dia = 1440
resposta = casos_pos()
print(f'{resposta[0]} {resposta[1]}')