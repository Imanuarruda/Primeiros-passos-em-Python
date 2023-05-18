import os
import random
import secrets
from random import randint
from time import sleep
jogadores = []
sorteio = []
classificacao = []
limite = []
frutas = ["banana","maça","uva","pera"]
casa = ["sofá","mesa","televisão","cama"]
roda = ["1.00","500.00","200.00","Passou a vez","100.00","Passou a vez","1.00","100.00","Perdeu tudo",
        "1.000.00","500.00","1.00","200.00","100.00","250.00","700.00"]
opcao = casa + frutas
rodada = "acerto"


print(70*"=","\n""                            RODA A RODA""\n",70*"=")
print()
print(29*"","Instruções",29*"*")
print()
print("- Serão inscritos os participantes e decidido a ordem dos jogadores.""\n"
      "- A partida será iniciada após a decisão da ordem dos particpantes.""\n""- Cada letra errada passará a vez. "
      "Repetir letra também passa a vez.""\n""- Poderá palpirtar a palavra quando tiver restando 3 letras ou menos"
      "\n""- Cada rodada com acerto o participante ganhará pontos.""\n""- Caso a roda pare em -Passou a vez- o jogador "
      "perderá a jogada.""\n""- Caso a roda pare em -Perdeu tudo- o jogador perderá tudo que ganhou até o momento.""\n"
      "- Ganha o jogo que estiver com mais pontos.")
sleep(30)
os.system("cls")

print(70*"=","\n""                            RODA A RODA""\n",70*"=")
while True:
    quant_jogadores = int(input("Quantos jogadores irão jogar: (2 a 4 jogadores) "))
    if quant_jogadores > 1  and quant_jogadores < 5:
        break
for s in range(quant_jogadores):
    jogadores.append(int(randint(1,10)))
    jogadores.append(str(input("Nome do jogador: ")))
    sorteio.append(jogadores[:])
    del(jogadores[:])
os.system("cls")
print(70*"=","\n""                            RODA A RODA""\n",70*"=")
print("O soteio está acontecendo...")
classificacao = sorted(sorteio)
classificacao.reverse()
for o in range(quant_jogadores):
    print(f"{o+1}º: {classificacao[o][1]} tirou {classificacao[o][0]}")
    sleep(1)
os.system("cls")
palavra = secrets.choice(casa + frutas)
espacos = ["_"]*len(palavra)
limite = len(palavra) * ["_"]
if palavra in casa:
    dica = "casa"
else:
    if palavra in frutas:
        dica = "frutas"

while "_" in espacos:
    for j in range(quant_jogadores):
        rodada = "acerto"
        roleta = secrets.choice(roda)
        if roleta == "Passou a vez" or roleta == "Perdeu tudo":
            rodada = "errou"
        os.system("cls")
        if roleta == "Passou a vez" or roleta == "Perdeu tudo":
            print(f"Ahh, {classificacao[j][1]} {roleta}")
            sleep(3)
            os.system("cls")
        print(70 * "=", "\n""                            RODA A RODA""\n", 70 * "=")
        print("\bRodando a roleta...")
        sleep(1)
        while rodada == "acerto":
            print(f"\nValendo R${roleta} reais")
            print(f"\n{classificacao[j][1]} sua vez de jogar\n")
            for e in range(len(palavra)):
                print(espacos[e], end=" ")
            print()
            print(f"\nA palavra é relacionada a {dica}")
            if len(limite) <= 3:
                palpite = input("\nQual a palavra? ").lower().strip()
                if palpite == palavra:
                    print("Você acertouuu!!")
                    print(f"A palavra é {palavra}")
                    print(f"\n{classificacao[j][1]} ganhou o jogo!!!!")
                    sleep(3)
                    exit()
                else:
                    print("Errado, está ainda não é a palavra")
            letra = input("\nDigite uma letra: ").lower().strip()
            for l in range(len(palavra)):
                if letra == palavra[l]:
                    espacos[l] = letra
                    limite.pop()
                    roleta = random.choice(roda)
                    if roleta == "Passou a vez" or roleta == "Perdeu tudo":
                        rodada = "errou"
                if letra not in palavra:
                    rodada = "errou"
                print(espacos[l], end=" ")
            print()
            if letra in palavra:
                print(f"\nCerto!! Letra {letra} tem na palvra")
            else:
                print(f"\nAHHH! Letra {letra} não tem na palvra")
            if len(limite) == 0:
                print("\nA palavra foi descorberta. Parabens!")
                print(f"\n{classificacao[j][1]} ganhou o jogo!!!!")
                sleep(3)
                exit()
            sleep(2)
            os.system("cls")
            print(70 * "=", "\n""                            RODA A RODA""\n", 70 * "=")
            print("\nRodando a roleta...")
            if roleta == "Passou a vez" or roleta == "Perdeu tudo":
                print(f"\nAhh, {classificacao[j][1]} {roleta}")
                sleep(3)
