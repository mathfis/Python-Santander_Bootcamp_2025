# conceitos de herança múltipla
class FalarMixIn:
    def falar(self):
        print(f"\nSou {self.__class__.__name__} e estou falando")

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: "+\
                ', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])

class Ave(Animal):
    def __init__(self, cor_do_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_do_bico = cor_do_bico

class Mamifero(Animal):
    def __init__(self, cor_do_pelo='preto', **kwargs):
        super().__init__(**kwargs)
        self.cor_do_pelo = cor_do_pelo

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave, FalarMixIn):
    pass

# Para não haver conflito em herança múltipla, foi necessário passar os argumentos da classe avó como
# **kwargs e, como isso, tornou-se necessário nomear os argumentos
o = Ornitorrinco(nro_patas = 2, cor_do_pelo = 'marrom', cor_do_bico = 'laranja')
print(o)

# com isso, as outras classes deixam de poder serem criadas com argumentos posicionais para nro_patas
# se faz necessário
c = Cachorro(nro_patas = 4) #preto por padrão na construção da classe
print(c)
c = Cachorro('branco', nro_patas = 4)
print(c)
# ou
c = Cachorro(cor_do_pelo='marrom', nro_patas = 4)
print(c)

# Para saber a ordem de resolução do interpretador
print(f"\n{Ornitorrinco.__mro__}")

# Método falar da classe extendida FalarMixIn
o.falar()
print("\n")