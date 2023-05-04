from random import randint
import os
clientes = []
id = []
while True:
    print(15*"-","\n"," CADASTRANDO","\n",15*"-")
    cliente = input("Nome do cliente: ")
    cod = randint(1000,1999)
    clientes.append(cliente)
    id.append(cod)
    print(f"Cliente cadastrado! {cliente}-{cod}")
    print(34*"-")
    add = input("Deseja adicionar mais um cliente? [sim/não] ").lower()
    if add != "sim":
        break
    os.system("cls")
os.system("cls")

print(15*"-","\n","    ACESSO","\n",15*"-")
while True:
    id_cliente = int(input("Informe o id do cliente para acessarmos a conta: "))
    for c in range(len(id)):
        if id_cliente == id[c]:
            print(f"Olá, {clientes[c]}, seja bem vindo ao portal de simulação!")
            valor_investido = float(input("Qual o valor que deseja simular? "))
            tempo = float(input("Em quanto tempo deseja resgatar o valor? "))
            while True:
                conta = int(input(f"Qual a opção que deseja fazer a simulação: \n[1] Poupança \n[2] CDB \n[3] Tesouro Direto\n"))
                if conta == 1:
                    print("A poupança tem um rendimento de 6,17& ao ano")
                    poupanca = valor_investido*(1.0051**tempo)
                    print(f"Investindo {valor_investido} durante {tempo} meses na poupança, você terá o retorno de {poupanca:.2f}\n")
                elif conta == 2:
                    print("O CDB com retorno de 100% do CDI está com rendimento de 13,75% ao ano")
                    cdb = valor_investido*(1.0114**tempo)
                    print(f"Investindo {valor_investido} durante {tempo} meses no CDB, você terá o retorno de {cdb:.2f}\n")
                elif conta == 3:
                    print("O tesouro direto, pré-fixado, está com rendimento de 14% ao ano")
                    tesouro_direto = valor_investido * (1.0116**tempo)
                    print(f"Investindo {valor_investido} durante {tempo} meses no Tesouro Direto, você terá o retorno de {tesouro_direto:.2f}\n")
                else:
                    print("Opção inválida.")
                cont = int(input("[1] Deseja selecinoar esta opção?\n[2]Voltar as opções: "))
                if cont == 1:
                    break
        else:
            print("Usuário não encontrado.\n")

