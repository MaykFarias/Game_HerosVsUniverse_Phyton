import random
import time

listaDeHerois = ["Superman", "Batman", "Mulher Maravilha"]
listaDeViloes = ["Coringa", "Lex Luthor", "Flash Reverso"]
listaDeAtaques = [10, 20, 40]

vidaHeroi = 100
vidaVilao = 100
escolhaHeroi = 0
escolhaVilao = 0
numeroGolpeHeroi = 0
numeroGolpeVilao = 0

print(" -" * 15)
print("\033[0:1m|        JOGO DOS HEROIS       |\033[m")
print(" -" * 15)
print("\033[0:1m QUAL HEROI VOCÊ ESCOLHE ?\033[m")
print("\033[0:36m [1] Superman \n [2] Batmam \n [3] Mulher Maravilha\033[m ")
print("-" * 30)
escolhaUsuario = int(input("---> "))
escolhaHeroi = listaDeHerois[escolhaUsuario - 1]
print(f"Você escolheu o {escolhaHeroi}")
print("-" * 30)

time.sleep(1)
print("O COMPUTADOR VAI ESCOLHER O SEU OPONENTE !")
escolhaPc = random.randint(1, 3)
escolhaVilao = listaDeViloes[escolhaPc - 1]
print(f"O oponente escolhido foi... {escolhaVilao}\n")

time.sleep(2)
print("-" * 30)
print("\033[0:1m|             HOUND            |\033[m")
print("-" * 30)
print("\033[0:1mQuantos hounds deseja jogar ?\033[m")
print("-" * 15)
escolhaDosHounds = int(input("---> "))
print("-" * 15)
print(" ")

time.sleep(2)
print("= " * 15)
print("\033[0:1mPREPARANDO CAMPO DE BATALHA...\n")
time.sleep(2)
print(f"{f'{escolhaHeroi} _X_ {escolhaVilao} ':^30}")
print(f"{f'Vida 100         Vida  100  %':^5}")
print(f"SERÁ UM PARTIDA DE {escolhaDosHounds} hounds.\033[m")
print("= " * 15)

time.sleep(2)
while vidaHeroi > 0 and vidaVilao > 0:
    while escolhaDosHounds > 0:
        if vidaVilao > 0:
            print(" ")
            print("__" * 15)
            print("           OPÇÔES ")
            print("=" * 30)
            print(
                "[1] ATAQUE FRACO \n" +
                "[2] ATAQUE FORTE\n" +
                "[3] ATAQUE CRITICO")
            print("=_" * 15)
            print("= QUAL O SEU COMANDO ?           ")
            escolhaDeAtaqueUsuario = int(input("-----> "))
            vidaVilao -= listaDeAtaques[escolhaDeAtaqueUsuario-1]
            print("=" * 20)
            print(
                f"\033[0:1m{escolhaHeroi} casou {listaDeAtaques[escolhaDeAtaqueUsuario-1]} de dano no {escolhaVilao}\033[m")
            time.sleep(2)
            if vidaVilao <= 0:
                break
        if vidaHeroi > 0:
            escolhaDeAtaquePc = random.randint(0, 2)
            vidaHeroi -= listaDeAtaques[escolhaDeAtaquePc]
            print(f"\033[0:1m{escolhaVilao} casou {listaDeAtaques[escolhaDeAtaquePc]} de dano no {escolhaHeroi}\033[m")
            print("-" * 30)
            if vidaHeroi <= 0:
                break

        time.sleep(2)
        print(f"{escolhaHeroi} VIDA: {vidaHeroi}%")
        print(f"{escolhaVilao} VIDA: {vidaVilao}%")

        escolhaDosHounds -= 1
    print("")
    time.sleep(1)
    if (vidaHeroi > vidaVilao):
        print("Você GANHOU !!!")
        break
    elif (vidaVilao > vidaHeroi):
        print("Você PERDEU !!!")
        break
    elif (vidaHeroi <= 0 or vidaVilao <= 0):
        print("EMPATE !!!")
        break
time.sleep(2)
print("Fim do Jogo !!!")
