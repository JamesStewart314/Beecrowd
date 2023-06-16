while True:
    try:
        M = float(input())
    except EOFError:
        break
    quad = ["Bom Dia!!", "Boa Tarde!!", "Boa Noite!!", "De Madrugada!!"]
    print(quad[int(M//90)])
    tempo = 240*((M+90) % 360)
    horas = int((tempo // 3600) % 24)
    minutos = int((tempo // 60) % 60)
    segundos = int(tempo - horas*3600 - minutos*60)
    print('{:0>2}:{:0>2}:{:0>2}'.format(horas, minutos, segundos))
