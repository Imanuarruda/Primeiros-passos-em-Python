import os
from time import sleep

alunos = ["ana beatriz", "anderson josé", "ânderson vinícius", "arthur henrique", "bárbara tavares", "bruno rafael",
          "débora lúcia", "emanuel assuero", "gabriel josé", "geraldo lucas", "helen maria", "inajá ramos",
          "joão victor",
          "lillyan de santana", "lucas nascimento", "manuela arruda", "marcus vinicius", "maria clara", "pedro victor",
          "raniely vitória", "sabrina ferreira", "thiago henrique", "thiago yuji", "vanessa ribeiro"]
alunos_senha = ["1382", "1814", "1501", "1273", "1929", "1438", "1309", "1845", "1825", "1322", "1550", "1546", "1976",
                "1403", "1170",
                "1233", "1216", "1831", "1016", "1704", "1498", "1044", "1960", "1509"]
alunos_votaram = []
cod_acesso = "1234"
inaja = mariaclara = marcus = 0
if os.path.isfile("votacao.txt"):
    with open("votacao.txt", "r") as arquivo:
        conteudo = arquivo.read()
        for linha in conteudo.splitlines():
            if "Inajá com" in linha:
                inaja = int(linha.split(" ")[-1])
            elif "Maria Clara com" in linha:
                mariaclara = int(linha.split(" ")[-1])
            elif "Marcus com" in linha:
                marcus = int(linha.split(" ")[-1])

while True:
    situacao = (f"\nNo momento a apuração está:\nInajá com {inaja}\nNaria Clara com {mariaclara}\nMarcus "
                f"com {marcus}")
    with open("votacao.txt", "a+") as arquivo:
        arquivo.write(situacao)
        arquivo.seek(0)
        conteudo = arquivo.read()
    print(40 * "=")
    print("      VOTAÇÃO PARA LÍDER DA TURMA")
    print(40 * "=")
    print()
    escolha = input("Você deseja VOTAR ou APURAR a votação? ").lower().strip()
    login_tentativa = 0
    if escolha == "votar" and login_tentativa < 2:
        print("(Primeiro e segundo nome)")
        login = str(input("Aluno: ")).strip().lower()
        while login not in alunos and login_tentativa < 2:
            if login in alunos_votaram:
                print("\nAluno já votou. Digite outro nome e sobrenme")
                login_tentativa += 1
                login = str(input("Aluno: ")).strip().lower()
            if login not in alunos and login not in alunos_votaram:
                print("\nAluno não encontrado. Digite nome e sobrenome""\n")
                login_tentativa += 1
                login = str(input("Aluno: ")).strip().lower()
            os.system("cls")
        if login_tentativa < 2:
            senha_correspondente = alunos.index(login)
            senha = input("Senha: ")
            while senha != alunos_senha[senha_correspondente]:
                print("\nSenha incorreta. Digite novamente""\n")
                senha = input("Senha: ")
            os.system("cls")
            print("=" * 37)
            print("     VOTAÇÃO PARA LÍDER DA TURMA     ")
            print("=" * 37)
            print("\nOpções de candidatos: ")
            print("1. Inajá\n2. Maria Clara\n3. Marcus\n")
            print("-" * 12, "Para quem vai seu voto?", "-" * 12)
            while True:
                escolha = input("Informe o número referente as opções apresentadas: ").strip()
                match escolha:
                    case "1":
                        inaja += 1
                        print("\nSeu voto foi computadorizado\nObrigado por votar!")
                        sleep(3)
                        break
                    case "2":
                        mariaclara += 1
                        print("\nSeu voto foi computadorizado\nObrigado por votar!")
                        sleep(3)
                        break
                    case "3":
                        marcus += 1
                        print("\nSeu voto foi computadorizado\nObrigado por votar!")
                        sleep(3)
                        break
                    case _:
                        print("\nOpção inválida")
            os.system("cls")
            if inaja > mariaclara and inaja > marcus:
                resultado = inaja
                lider = "INAJÁ"
            elif mariaclara > inaja and mariaclara > marcus:
                resultado = mariaclara
                lider = "MARIA CLARA"
            else:
                resultado = marcus
                lider = "MARCUS"
            alunos_votaram.append(alunos[senha_correspondente])
            alunos.pop(senha_correspondente)
            alunos_senha.pop(senha_correspondente)

    elif escolha == "apurar":
        cod = input("Código de acesso: ")
        tentativas = 0
        while tentativas < 1 and cod != cod_acesso:
            cod = input("Código de acesso: ")
            tentativas += 1
            os.system("cls")
        if cod == cod_acesso:
            print(40 * "=")
            print("      APURAÇÃO DE VOTOS PARA LÍDER DA TURMA")
            print(40 * "=")
            print(f"\nO LÍDER DA TURMA  É {lider} COM {resultado} VOTOS.\nPARABÉNS {lider}, TENHA UMA BOA LIDERANÇA!")
            sleep(40)
            break
    else:
        print("Opção inválida, tente novamente")
