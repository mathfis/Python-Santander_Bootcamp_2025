# estudo de polimorfismo com herança

# Polimorfismo significa a utilização de mesmos nomes para comportamentos diferentes
# No contexto da POO, trata-se da sobrescrição de métodos da classe pai em classes filhas,
# onde estes métodos substituem os métodos das classes pai.

class Passaro:
    
    def voar(self):
        print("Voando...")

class Pardal(Passaro):

    def voar(self):
        super().voar()
    
class Avestruz(Passaro):

    def voar(self):
        print("Avestruz não voa")


class Aviao:
        
    def voar(self):
        print("Avião decolando...")


[c.voar() for c in (Pardal(),Avestruz(),Aviao())]