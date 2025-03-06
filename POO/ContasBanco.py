from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do Cliente
        cpf (str): CPF do Cliente
        agencia (int): Agencia responsável pela conta do Cliente
        conta (int): Número da conta corrente do Cliente
        saldo (float): Saldo disponível na conta do Cliente
        limite (float): Limite de Cheque Especial do Cliente
        transacoes (list): Histórico de Transações do Cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime("%d/%m/%Y %H:%M:%S")
    
    def __init__(self, nome, cpf, agencia, conta):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.conta = conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """
            Exibe o saldo atual da conta do cliente.
            Não há parâmetros necessários.
        """
        print(f"Seu saldo atual é de R${self._saldo:,.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite
      
    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print("Você não possui saldo o suficiente.")
            self.consultar_saldo()
        else:        
            self._saldo -= valor
            self.consultar_saldo()
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print(f"Seu limite de Cheque Especial é de R${self._limite_conta():,.2f}")

    def consultar_historico_transacoes(self):
        print("Histórico de Transações:")
        print("Valor, Saldo, Data e Hora")
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")  
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}"
        self.cod_seguranca = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        self.limite = 1000
        self._senha = "1234"
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida.")