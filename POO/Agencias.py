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
        super().__init__(telefone, cnpj, 1400)
        self.caixa = 1000000


class AgenciaComum(Agencia):

    pass


class AgenciaPremium(Agencia):

    pass












agencia1 = Agencia(2222333, 200000000, 4561)

agencia_virtual = AgenciaVirtual("www.agencia.com.br", 22549878, 111188999774557)
agencia_virtual.verificar_caixa()

print(agencia_virtual.__dict__)