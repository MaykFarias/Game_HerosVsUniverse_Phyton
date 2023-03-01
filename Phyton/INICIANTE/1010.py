##map para ler os valores de entrada como números de ponto flutuante

codigopeca1, quantidade_peca1, valor_unitario1 = map(float, input().split())

codigopeca2, quantidade_peca2, valor_unitario2 = map(float, input().split())

valortotal = (quantidade_peca1 * valor_unitario1) + (quantidade_peca2 * valor_unitario2)

print(f"VALOR A PAGAR: R$ {valortotal:.2f}")