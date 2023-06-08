from classbanco import CBanco
import os
from random import randint
from time import sleep
saldo = 0
conta = "Corrente"
numero = randint(0, 999)

print(40 * "-")
print("           BANCO NOVA ESTAÇÃO")
print(40 * "-", "\n")
nome = input("Nome: ")
nascimento = input("Data Nascimento: ")
cliente = CBanco(numero, saldo, nome, conta)
print(f"\nVejo que ainda não tem uma conta. Vamos Abrir sua conta.")
escolha = input("Sim ou Não? ").strip().upper()
if escolha == "SIM":
    cliente.ativar()
    print(f"Conta {conta}\nNúmero {numero}")
    sleep(2)
else:
    print("Ah, então quem sabe mais tarde você não volta aqui e abre sua conta.")
os.system("cls")
while True:
    print(40 * "-")
    print("           BANCO NOVA ESTAÇÃO")
    print(40 * "-", "\n")
    print("""
    [1] Saldo
    [2] Depositar
    [3] Sacar
    [4] Extrato
    [5] Limite Especial
    [6] Desativar conta
    [7] Sair
    """)
    escolhaopcao = int(input())

    match escolhaopcao:
        case 1:
            cliente.verificar()
        case 2:
            valorDeposito = float(input("Quanto você deseja depositar: "))
            cliente.depositar(valorDeposito)
        case 3:
            valorSaque = float(input("Quanto deseja sacar? "))
            cliente.sacar(valorSaque)
        case 4:
            print(cliente.extrato())
        case 5:
            cliente.ativarlimite()
        case 6:
            cliente.desativar()
        case 7:
            break
        case _:
            print("Opção inválida.\nDigite a opção correta.")
    sleep(2)
    os.system("cls")
