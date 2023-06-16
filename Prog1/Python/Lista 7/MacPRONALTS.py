tabela_cardapio = dict({1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5})
tam_pedido = int(input())
valor_final = 0
for i in range(tam_pedido):
    pedido = list(map(int, input().split()))
    valor_final += tabela_cardapio[pedido[0]] * pedido[1]
print(f'{valor_final:.2f}')