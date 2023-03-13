## Essa questão n soube resolver

x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
## Se X positivo e Y positivo
elif x > 0 and y > 0:
    print("Q1")
## Se X negativo e Y positivo
elif x < 0 and y > 0:
    print("Q2")
## Se x negativo e Y negativo
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")