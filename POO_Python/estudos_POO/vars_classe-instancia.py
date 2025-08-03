# estudo de variaveis de classe e de instancia

# Atributos de instância são aqueles onde cada instância possui uma cópia deles
# Atributos de classe são aqueles compartilhados entre os objetos

class Estudante:
    
    escola = "Escola" #variavel de classe
    alunos = []
    def __init__(self,nome,matricula):
        self._nome = nome
        self._matricula = matricula
        (Estudante.alunos).append(self)
    
    @property
    def nome(self):
        return self._nome
    
    def __str__(self):
        return f"\n{self.__class__.__name__}: "+\
              f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"+\
              f" - Escola {self.escola}\n"
        
gui = Estudante("Guilherme",1234)
gi = Estudante("Giovana",1235)

Estudante.escola = "Colégio"
gi = Estudante("Giovana",2222)

for aluno in Estudante.alunos:
    print(aluno._nome)