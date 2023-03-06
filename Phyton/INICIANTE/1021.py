cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0

moedaUm = 0
moedaCinquenta = 0
moedaVinte = 0
moedaDez = 0
moedaCinco = 0
moedaUmCentavo = 0

n = float(input())

while n > 0:
    if n >= 100:
        n -= 100
        cem += 1
    elif n >= 50:
        n -= 50
        cinquenta += 1
    elif n >= 20:
        n -= 20
        vinte += 1
    elif n >= 10:
        n -= 10
        dez += 1
    elif n >= 5:
        n -= 5
        cinco += 1
    elif n >= 2:
        n -= 2
        dois += 1
    elif n >= 1:
        n -= 1
        moedaUm += 1
    elif n >= 0.50:
        n -= 0.50
        moedaCinquenta += 1
    elif n >= 0.20:
        n -= 0.20
        moedaVinte += 1
    elif n >= 0.10:
        n -= 0.10
        moedaDez += 1
    elif n >= 0.05:
        n -= 0.05
        moedaCinco += 1
    elif n >= 0.01:
        n -= 0.01
        moedaUmCentavo += 1
    else:
        break

print("NOTAS:")
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print("MOEDAS:")
print(f"{moedaUm} moeda(s) de R$ 1.00")
print(f"{moedaCinquenta} moeda(s) de R$ 0.50")
print(f"{moedaVinte} moeda(s) de R$ 0.25")
print(f"{moedaDez} moeda(s) de R$ 0.10")
print(f"{moedaCinco} moeda(s) de R$ 0.05")
print(f"{moedaUmCentavo} moeda(s) de R$ 0.01")
