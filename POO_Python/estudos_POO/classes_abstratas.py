# Classes abstratas usando o módulo ABC

# Classes abstratas fornecem projetos para classes a serem implementadas 
# a partir de extensões da mesma, fazendo com que o polimorfismo seja mais seguro.

# Por padrão, o Python não oferece classes abstratas e módulo ABC ajuda com isso.
from abc import ABC, abstractmethod
class ControleRemoto(ABC): #ControleRemoto extende a classe ABC

    controles = []    
    #construtor
    def __init__(self, marca):
        self._marca = marca

    # método de classe
    @classmethod
    def cria_controle(cls, marca):
        novo_controle = cls(marca)
        cls.controles.append(novo_controle)
        return novo_controle
    
    # método de classe
    @classmethod
    def lista_marcas_controles(cls):
        """ Retorna a lista de marcas de controles criados 
            e a classe do controle como String
        """
        n = len(cls.controles)
        nros_controles = zip( range(1,n+1) , cls.controles) # objeto zip iteravel
        marcas_controles = [f"{i}:({c.__class__.__name__} {c.marca})" for i , c in nros_controles]
        
        return marcas_controles
       
    @abstractmethod # o decorador transforma o método em abstrato
    def ligar(self):
        pass
    
    @abstractmethod # o decorador transforma o método em abstrato
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

    # por conta dos decoradores, as classes que extendam a classe ControleRemoto
    # precisarão implementar os métodos ligar() e desligar()
    
class ControleTV(ControleRemoto):
    
    def ligar(self):
        print("Ligando a TV...")
    
    def desligar(self):
        print("Desligando a TV...")

    @property
    def marca(self):
        return self._marca
    
class ControleAC(ControleRemoto):
    
    def ligar(self):
        print("Ligando o ar-condicionado...")
    
    def desligar(self):
        print("Desligando o ar-condicionado...")

    @property
    def marca(self):
        return self._marca
    

# teste
controle_ac = ControleAC.cria_controle(marca='LG')
controle_tv1 = ControleTV.cria_controle(marca='RokuTV')
controle_tv2 = ControleTV.cria_controle(marca='LG')
# Utiliza a listagem de ControleRemoto para imprimir todos os controles
print(", ".join(ControleRemoto.lista_marcas_controles()))