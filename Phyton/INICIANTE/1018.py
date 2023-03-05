cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

n = int(input())

while n > 0:
    if n > 100:
        n -= 100
        cem += 1
    elif n > 50:
        n -= 50
        cinquenta += 1
    elif n > 20:
        n -= 20
        vinte += 1
    elif n > 10:
        n -= 10
        dez += 1
    elif n > 5:
        n -= 5
        cinco += 1
    elif n > 2:
        n -= 2
        dois += 1
    elif n > 1:
        n -= 1
        um += 1
    else:
        break

print(n)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")

