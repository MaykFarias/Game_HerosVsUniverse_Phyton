import math

a = float(input())
b = float(input())
c = float(input())

##bhaskara = (-b ± √(b² - 4ac)) / 2a

delta = b**2 - 4*a*c

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")