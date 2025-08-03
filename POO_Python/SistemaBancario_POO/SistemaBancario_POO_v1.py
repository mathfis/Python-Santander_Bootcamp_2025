# Sistema Bancário com implementação em Python usando POO

from abc import ABC, abstractmethod


class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacoes(self,transacao):
        self.transacoes.append(transacao)

    def __str__(self):
        transacoes_str = [f"{t.__class__.__name__}:{t.valor}" for t in self.transacoes]
        return "\n".join(transacoes_str)


class Conta:
    def __init__(self, numero, cliente, n_saques=None, historico = None, agencia= None):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente  # instância de Cliente
        self._n_saques = n_saques if n_saques is not None else 0
        self._agencia = agencia if agencia is not None else "0001"
        self._historico = historico if historico is not None else Historico()  # instância de Historico

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo += valor
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, nova_agencia):
        self._agencia = nova_agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def n_saques(self):
        return self._n_saques
    
    @n_saques.setter
    def n_saques(self,valor):
        self._n_saques += valor
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero, agencia="0001"):
        return cls(numero=numero, agencia=agencia, cliente=cliente,
                   historico=Historico())

    # implementa depositar através do setter
    def depositar(self, valor): 
        if valor > 0:
            self.saldo = valor
            deposito = Deposito(self, valor)
            deposito.registrar(conta=self, proceder=True)
            return True
        return False
        
    # implementa sacar através do setter
    def sacar(self, valor):
        if valor > 0 and self.n_saques < self.limite_saques and valor <= self.saldo + self.limite:
            self.saldo = -valor
            self.n_saques = 1
            saque = Saque(self, valor)
            saque.registrar(conta=self, proceder=True)
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, n_saques=None,limite=None, limite_saques=None, historico=None, agencia=None):
        super().__init__(numero, cliente, n_saques, historico, agencia)
        self.limite = limite if limite is not None else 500
        self.limite_saques = limite_saques if limite_saques is not None else 1

    def __str__(self):
        nome_classe = self.__class__.__name__
        atributos_str = [f"{chave} = {valor}" for chave, valor in self.__dict__.items()]
        valor_atributos = ", ".join(atributos_str)
        return f"{nome_classe}: {valor_atributos}"


class Cliente:
    def __init__(self,endereco,contas=None):
        self._endereco = endereco
        # pode ser passada uma lista de contas existentes ou iniciar sem contas
        self._contas = contas if contas is not None else []

    @property
    def contas(self):
        return self._contas
    
    @contas.setter
    def contas(self, nova_conta):
        self._contas.append(nova_conta)

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco
    
    def __str__(self):
        return f"{self.__class__.__name__}: endereço = {self.endereco}"


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento,contas=None):
        super().__init__(endereco,contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        nome_classe = self.__class__.__name__
        atributos_str = [f"{chave} = {valor}" for chave, valor in self.__dict__.items()]
        valor_atributos = ", ".join(atributos_str)
        return f"{nome_classe}: {valor_atributos}"


class Transacao:  # interface
    def __init__(self, conta):
        self._conta = conta

    @abstractmethod
    def registrar(self, conta):
        raise NotImplementedError("O método registrar deve ser implementado pelas subclasses.")


class Deposito(Transacao): #corrigir
    def __init__(self, conta, valor):
        super().__init__(conta)
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta,proceder):
        # depósito realizado?
        if(proceder):
            historico = conta.historico
            historico.adicionar_transacoes(self)
    

class Saque(Transacao):
    def __init__(self, conta, valor):
        super().__init__(conta)
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta, proceder):
        # saque realizado?
        if(proceder):
            historico = conta.historico
            historico.adicionar_transacoes(self)

