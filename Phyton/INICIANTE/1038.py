codigo, quantidade = map(int, input().split())

tabela_de_precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

total = tabela_de_precos[codigo] * quantidade


print("Total: R$ {:.2f}".format(total))