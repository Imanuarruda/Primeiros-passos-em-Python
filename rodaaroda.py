import os
import secrets
from random import randint
from time import sleep
jogadores = []
sorteio = []
classificacao = []
limite = []
frutas = ["banana","maça","uva","pera"]
casa = ["sofá","mesa","televisão","cama"]
roda = ["RS1,00","R$500,00","R$200,00","Passou a vez","R$100,00","Passou a vez","R$1,00","R$100,00","Perdeu tudo",
        "R$1.000,00"]
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
#sleep(30)
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

print(70*"=","\n""                            RODA A RODA""\n",70*"=")
print()
palavra = secrets.choice(casa + frutas)
print(palavra) #TIRAR
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
        while rodada == "acerto":
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
                    sleep(3)
                    exit()
                else:
                    print("Errado, está ainda não é a palavra")
            letra = input("\nDigite uma letra: ").lower().strip()
            for l in range(len(palavra)):
                if letra == palavra[l]:
                    espacos[l] = letra
                    rodada = "acerto"
                    limite.pop()
                if letra not in palavra:
                    rodada = "errou"
                print(espacos[l], end=" ")
            print()
            if letra in palavra:
                print(f"Certo!! Letra {letra} tem na palvra")
            else:
                print(f"AHHH! Letra {letra} não tem na palvra")
            sleep(2)
            os.system("cls")
