menor = 0
meio = 0
maior = 0

##for i, hero in enumerate(listaDeHerois):

for numero in range(1, 4):
    if numero == 1:
        numero1 = int(input())
        menor = numero1
        meio = numero1
        maior = numero1
    elif numero == 2:
        numero2 = int(input())
        if numero2 > maior:
            menor = maior
            maior = numero2
        elif numero2 < menor:
            maior = menor
            menor = numero2
    elif numero == 3:
        numero3 = int(input())
        if numero3 > maior:
            meio = maior
            maior = numero3
        elif numero3 > meio:
            menor = meio
            meio = numero3
        elif numero3 > meio:
            meio = maior
            maior = numero3
        elif numero3 < meio:
            menor = meio
            meio = numero3


print(f"{maior} {menor} {meio}")
