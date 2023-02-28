nome = str(input())
salario = float(input())
totalvendas = float(input())

comissao = 15
total = salario + (totalvendas * 15 / 100)

print(f"TOTAL = R$ {total:.2f}")