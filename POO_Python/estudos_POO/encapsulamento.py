# estudo de encapsulamento

# Encapsulamento é a proteção dos dados de um objeto. Isto é importante
# para evitar modificações acidentais.

# Recursos Públicos e privados
# Python não tem palavras reservadas para variáveis públicas e privadas, mas há convenções
# por padrão, variáveis públicas devem ser escritas normalmente (`var`) e variáveis privadas deveriam
# ser iniciadas por um subtexto (`_var`).
# Python tem todas as suas variáveis como públicas, então é possível modificar uma _var, mas não é
# recomendado, por padrão.

class Conta:
    def __init__(self, saldo, nro_agencia):
        self._saldo = saldo # _saldo é privada não deve ser modificada fora da classe
        self.nro_agencia = nro_agencia # nro_agencia é pública, portanto
                                       # pode ser acessada e modificada livremente
    def depositar(self, valor): # método público
        self._saldo += valor

    def sacar(self, valor): # método público
        self._saldo -= valor

    def get_saldo(self): # método público
        return self._saldo

valor = 50
conta = Conta(100, "001")
conta._saldo += valor  # você não deveria fazer isso
print(conta._saldo)    # e nem isso, mas...
# o Python deixa!
# O correto seria...
conta.sacar(valor)     # reduzir o saldo através de um método da classe Conta ou
conta.depositar(valor) # aumentaro saldo através de um método da classe Conta ou
# fazer qualquer modificação em _saldo através de algum método da classe Conta, assim como...
print( conta.get_saldo() ) # exibir informações privadas através de um método público
                           # da classe Conta
# Já variáveis públicas
conta.nro_agencia = "002" # podem ser modificadas ou
print(conta.nro_agencia)  # acessadas livremente!
