horarios = input().split()
pa = int(horarios[0].split(":")[0]) * 60 + int(horarios[0].split(":")[1])
cb = int(horarios[1].split(":")[0]) * 60 + int(horarios[1].split(":")[1])
pb = int(horarios[2].split(":")[0]) * 60 + int(horarios[2].split(":")[1])
ca = int(horarios[3].split(":")[0]) * 60 + int(horarios[3].split(":")[1])
tempo_voo_min = 24 * 60
resposta = None
for fuso in range(-11, 13):
    tempo_voo = (cb - pa - 60 * fuso) % (60 * 24)
    if ((pa + tempo_voo + fuso * 60) % (60 * 24)) == cb and ((pb + tempo_voo - fuso * 60) % (60 * 24)) == ca:
        if tempo_voo < tempo_voo_min:
            tempo_voo_min = tempo_voo
            resposta = (tempo_voo, fuso)
print(*resposta)