import random
import time

listaDeHerois = ["\033[31:1mSuperman\033[m", "\033[36:1mBatman\033[m", "\033[33:1mMulher Maravilha\033[m"]
listaDeViloes = ["\033[35:1mCoringa\033[m", "\033[37:1mLex Luthor\033[m", "\033[32:1mDuende Verde\033[m"]
listaDeAtaques = [10, 20, 40]

vidaHeroi = 100
vidaVilao = 100
escolhaHeroi = 0
escolhaVilao = 0
numeroGolpeHeroi = 0
numeroGolpeVilao = 0

## APRESENTAÇÃO DOS HEROIS
print("")
print(" -" * 15)
print(f"\033[0:1m{f'JOGO DOS HEROIS':^30}\033[m")
print(" -" * 15)
print("\033[0:1mQUAL HEROI VOCÊ ESCOLHE ?\033[m")
for i, hero in enumerate(listaDeHerois):
    print(f"[{i + 1}] {hero}")
print("Digite o numero do heroi que voce deseja: ")
print("-" * 30)
escolhaUsuario = 0
while True:
    escolhaUsuario = input("Escolha um ataque (1, 2 ou 3): ").strip()
    try:
        escolhaUsuario = int(escolhaUsuario)
        if escolhaUsuario not in (1, 2, 3):
            print("Escolha inválida. Tente novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Tente novamente.")
escolhaHeroi = listaDeHerois[escolhaUsuario - 1]
print(f"Você escolheu o {escolhaHeroi}")
print("-" * 30)
time.sleep(1)

## ESCOLHA DO COMPUTADOR
print("O COMPUTADOR VAI ESCOLHER O SEU OPONENTE !")
escolhaPc = random.randint(1, 3)
escolhaVilao = listaDeViloes[escolhaPc - 1]
print(f"O oponente escolhido foi... {escolhaVilao}\n")
time.sleep(2)

## HOUNDS
print("-" * 30)
print(f"\033[30:0:1m{f'HOUND':^30}\033[m")
print("-" * 30)
print("\033[0:1mQuantos hounds deseja jogar ?\033[m")
print("-" * 15)
while True:
    escolhaDosHounds = int(input("---> "))
    try:
        escolhaDeHounds = int(escolhaDosHounds)
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")
print("-" * 15)
print(" ")
print("= " * 15)

## APRESENTAÇÃO
print("\033[0:1mPREPARANDO CAMPO DE BATALHA...\n")
time.sleep(2)
print(f"{escolhaHeroi} _X_ {escolhaVilao}")
print(f"{f'Vida 100%         Vida  100%':^5}")
print(f"SERÁ UM PARTIDA DE {escolhaDosHounds} HOUNDS.\033[m")
print("= " * 15)

## LUTA
time.sleep(2)
while vidaHeroi > 0 and vidaVilao > 0:
    while escolhaDeHounds > 0:
        print("")
        print(f"\033[30:0:1m{f'HOUND ':>17}{escolhaDosHounds}\033[m")
        if vidaVilao > 0:
            print("__" * 15)
            print(f"{'OPÇÔES':^30}")
            print("=" * 30)
            print(
                "[1] ATAQUE FRACO \n" +
                "[2] ATAQUE FORTE\n" +
                "[3] ATAQUE CRITICO")
            print("=" * 30)
            escolhaDeAtaqueUsuario = 0
            while True:
                escolhaDeAtaqueUsuario = input("Escolha um ataque (1, 2 ou 3): ").strip()
                try:
                    escolhaDeAtaqueUsuario = int(escolhaDeAtaqueUsuario)
                    if escolhaDeAtaqueUsuario not in (1, 2, 3):
                        print("Escolha inválida. Tente novamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Tente novamente.")
            vidaVilao -= listaDeAtaques[escolhaDeAtaqueUsuario - 1]
            print("=" * 30)
            print(
                f"\033[0:1m{escolhaHeroi} casou {listaDeAtaques[escolhaDeAtaqueUsuario - 1]} de dano no {escolhaVilao}\033[m")
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
        print(f"{escolhaHeroi} VIDA: \033[1m{vidaHeroi}%\033[m")
        print(f"{escolhaVilao} VIDA: \033[1m{vidaVilao}%\033[1m")

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
