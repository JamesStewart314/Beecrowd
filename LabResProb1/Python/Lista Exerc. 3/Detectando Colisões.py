retangulo_1 = tuple(map(int, input().split()))
retangulo_2 = tuple(map(int, input().split()))
seq_x_1 = [retangulo_1[0], retangulo_1[2]]
seq_x_2 = [retangulo_2[0], retangulo_2[2]]
seq_y_1 = [retangulo_1[1], retangulo_1[3]]
seq_y_2 = [retangulo_2[1], retangulo_2[3]]
resposta = 0
px = None
if seq_x_1[0] <= seq_x_2[0] <= seq_x_1[1] or seq_x_1[0] <= seq_x_2[1] <= seq_x_1[1] or\
        seq_x_2[0] <= seq_x_1[0] <= seq_x_2[1] or seq_x_2[0] <= seq_x_1[1] <= seq_x_2[1]:
    px = True
if px is True:
    if seq_y_1[0] <= seq_y_2[0] <= seq_y_1[1] or seq_y_1[0] <= seq_y_2[1] <= seq_y_1[1] or\
            seq_y_2[0] <= seq_y_1[0] <= seq_y_2[1] or seq_y_2[0] <= seq_y_1[1] <= seq_y_2[1]:
        resposta = 1
print(resposta)
