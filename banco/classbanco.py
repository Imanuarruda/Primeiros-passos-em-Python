class CBanco:
    def __init__(self, numeroconta, saldo, nomecliente, tipoconta, limiteespeciel=False, status=False):
        self.numeroconta = numeroconta
        self.saldo = saldo
        self.nomecliente = nomecliente
        self.tipoconta = tipoconta
        self.status = status
        self.limiteespecial = limiteespeciel

        # Não precisa de parâmetro
    def ativar(self):
        if not self.status:
            self.status = True
            print(f"\n{self.nomecliente} sua conta está ativada")

    def verificar(self):
        print(f"Saldo é R${self.saldo:.2f}")
        if self.limiteespecial is True:
            print(f"Saldo de limite especial é de R${self.liberado:.2f}")
            self.saldototal = self.saldo + self.liberado

    def depositar(self, deposito):
        if self.limiteespecial is False or self.liberado == self.limite:
            self.saldo += deposito
        print(f"Deposito de R${deposito:.2f} realizado com sucesso.")
        if self.limiteespecial is True and self.liberado < self.limite:
            self.diferencalimite = self.limite - self.liberado
            if deposito > self.diferencalimite:
                self.liberado += self.diferencalimite
                self.acrescimodeposito = deposito - self.diferencalimite
                self.saldo += self.acrescimodeposito
            else:
                self.liberado += deposito
        with open("extrato.txt", "a") as arquivo:
            arquivo.write(f"\nDepósito de R${deposito:.2f}")

    def sacar(self, saque):
        if saque > 0 and saque <= self.saldo:
            self.saldo -= saque
            print(f"Seu saque de R${saque:.2f} foi realizado com sucesso!")
        else:
            if saque > 0 and self.limiteespecial is True and saque <= self.saldototal:
                self.resto = saque - self.saldo
                self.saldo = 0
                self.liberado -= self.resto
                print(f"Seu saque de R${saque:.2f} foi realizado com sucesso!")
        with open("extrato.txt", "a") as arquivo:
            arquivo.write(f"\nSaque de R${saque:.2f}")
    def desativar(self):
        if self.saldo == 0 and self.status is True and self.liberado == self.limite:
            print("Sua conta foi desativada com sucesso.")
        else:
            if self.saldo > 0:
                print(f"Não é possível fazer a desativação.\nSua conta precisa estar zerada.")
            elif self.liberado < self.limite:
                print(f"Não é possível fazer a desativação.\nVocê tem pendências no limite especial.")

    def ativarlimite(self):
        self.limiteespecial = True
        self.limite = 200
        self.liberado = self.limite
        print("Seu limite especial foi liberado!")

    def extrato(self):
        with open("extrato.txt", "r") as arquivo:
            self.exibir = arquivo.read()
        return self.exibir