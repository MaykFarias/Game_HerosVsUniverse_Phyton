import random

listaDeHerois = ["Superman", "Batman", "Mulher Maravilha"]
listaDeViloes = ["Coringa", "Lex Luthor", "Flash Reverso"]
dicionarioAtaques = {"ataquefraco" : 10, "ataqueforte" : 20, "ataquecritico" : 40}

vidaHeroi = 100
vidaVilao = 100
escolhaHeroi = 0
escolhaVilao = 0
numeroGolpeHeroi = 0
numeroGolpeVilao = 0


print(" -" * 15)
print("|        JOGO DOS HEROIS       |")
print("\033[0:33:44     QUAL HEROI VOCÊ ESCOLHE ?\033[m")
print(" -" * 15)
print("[1] Superman \n[2] Batmam \n[3] Mulher Maravilha")
print("-" * 30)
escolhaUsuario = int(input("---> "))
escolhaHeroi = listaDeHerois[escolhaUsuario - 1]
print(f"Você escolheu o {escolhaHeroi}")
print("-" * 30)


print("\nO COMPUTADOR VAI ESCOLHER O SEU OPONENTE !")
escolhaPc = random.randint(1, 3)
escolhaVilao = listaDeViloes[escolhaPc - 1]
print(f"O oponente escolhido foi... {escolhaVilao}")

print("-" * 15)
print("|                HOUND               |")
print("-" * 15)
print("Quantos hounds deseja jogar ?")
print("-" * 15)
escolhaDosHounds = int(input("---> "))
print("-" * 15)

print("\nPREPARANDO CAMPO DE BATALHA\n")
print("= " * 20)
print(f" {escolhaHeroi} X {escolhaVilao} ")
print("=" * 20)
print(f" Vida 100         Vida  100  %")
print("-" * 20)
print(f"SERÁ UM PARTIDA DE {escolhaDosHounds} hounds.")
print("-" * 20)

escolhaRounds = escolhaDosHounds
while vidaHeroi > 0 and vidaVilao > 0 and escolhaRounds > 0:
    for roundAtual in range(escolhaDosHounds - escolhaRounds + 1):
        if vidaVilao > 0:
            print("=" * 20)
            print("             OPÇÔES ")
            print

    print("PREPARANDO CAMPO DE BATALHA\n")
    print("= " * 20)
    print(f" {escolhaHeroi} X {escolhaVilao} ")
    print("=" * 20)
    print(f" Vida 100         Vida  100  %")
    print("-" * 20)
    print(f"SERÁ UM PARTIDA DE {escolhaDosHounds} hounds.")
    print("-" * 20)

    while vidaHeroi > 0 and vidaVilao > 0 and escolhaDosHounds > 0:
        for escolhaRounds in range(escolhaRounds):
            if vidaVilao > 0:
                print("=" * 20)
                print("             OPÇÔES ")
                print(
                    "[1] ATAQUE FRACO \n" +
                    "[2] ATAQUE FORTE\n" +
                    "[3] ATAQUE CRITICO\n" +
                    "[4] DEFESA \n"
                )
                print("=" * 20)
                print("= QUAL O SEU COMANDO ?           =")
                escolhaDeAtaque = int(input("-----> "))
                vidaVilao -= dicionarioAtaques{escolhaDeAtaque}
                print("=" * 20)
                print(f"O {escolhaHeroi} casou {escolhaDeAtaque} de dano no {escolhaVilao}")
            if vidaHeroi > 0:
                random.randint(1, 3)
                vidaHeroi -= ataqueVilao
                print(f"O {escolhaHeroi} casou {escolhaDeAtaque} de dano no {escolhaVilao}")
                print("-" * 30)

            print(f"{escolhaHeroi} VIDA: {vidaHeroi}")
            print(f"{escolhaVilao} VIDA: {vidaVilao}")

            escolhaRounds -= 1
            if (vidaHeroi > vidaVilao):
                print("Você GANHOU !!!")
                break
            elif (vidaVilao > vidaHeroi):
                print("Você PERDEU !!!")
                break
            elif (vidaHeroi <= 0 or vidaVilao <= 0):
                print("OS HOUNDS ACABARAM !!!")
                break
        escolhaRounds += 1
