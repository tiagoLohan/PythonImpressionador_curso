from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.cliente = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado. Caixa atual: R${self.caixa:,.2f}")
        else:
            print(f"O valor de caixa esta ok. Caixa: R${self.caixa:,.2f}")

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Empréstimo não é possível. Dinheiro não disponível em caixa.")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.cliente.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("O cliente não tem o patrimônio mínimo para entrar na agência Premium.")







if __name__ == "__main__":

    agencia1 = Agencia(2222333, 200000000, 4561)

    agencia_virtual = AgenciaVirtual("www.agencia.com.br", 22549878, 111188999774557)
    agencia_comum = AgenciaComum(222222, 25555555555)
    agencia_premium = AgenciaPremium(45554848, 54444841)

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium.adicionar_cliente("Lira", 56958818, 50000000)
    print(agencia_premium.cliente)
