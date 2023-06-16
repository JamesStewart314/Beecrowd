testes = int(input())
for i in range(testes):
    produtos = int(input())
    tabela_produtos = dict()
    for w in range(produtos):
        linha = input().split()
        tabela_produtos.update({linha[0]: float(linha[1])})
    quant_compras = int(input())
    resposta = 0
    for w1 in range(quant_compras):
        linha = input().split()
        resposta += tabela_produtos[linha[0]] * float(linha[1])
    print(f'R$ {resposta:.2f}')