class ContaCorrente:
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self.saldo:,.2f}")

    def depositar(self, valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -1000
        return self.limite
      
    def sacar(self, valor):
        if self.saldo - valor < self.limite_conta():
            print("Você não possui saldo o suficiente.")
            self.consultar_saldo()
            return
        
        self.saldo -= valor
        self.consultar_saldo()

#programa
conta_lira = ContaCorrente("Lira", "111.222.333-45")



conta_lira.consultar_saldo()
conta_lira.depositar(17000)
conta_lira.consultar_saldo()
conta_lira.sacar(1000)
conta_lira.sacar(16000.01)


   