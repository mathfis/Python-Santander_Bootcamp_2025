# estudo de metodos de classe e de objeto
# Método de objeto precisa de atributos de um objeto e referenciar um objeto "self"
# Método de classe precisa de atributos de classe e referenciar uma classe "cls"
## usa-se o decorador @classmethod
# Caso o método não necessite nem de "self" e nem de "cls", então é estático
## usa-se o decorador @staticmethod

class Pessoa:
    # método de objeto
    def __init__(self,nome, idade):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

    # método de classe
    @classmethod
    def cria_pessoa(cls, nome, ano_nascimento, ano_atual):
        idade = ano_atual - ano_nascimento
        return cls(nome, idade)

p = Pessoa.cria_pessoa("João", 2000, 2025)
print(p)
    