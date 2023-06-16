tabela = dict(A=[86, 100],
     B=[61, 85],
     C=[36, 60],
     D=[1, 35],
     E=[0, 0])
entrada = int(input())
for z in tabela.keys():
    if tabela[z][0] <= entrada <= tabela[z][1]:
        print(z)