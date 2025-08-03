# estudo de encapsulamento --> propriedades

# Propriedades em Python são uma forma de controlar o acesso a atributos de uma classe,
# permitindo definir métodos para leitura, escrita e deleção de valores, usando o
# decorador @property.
# Elas ajudam a aplicar encapsulamento, permitindo que você execute código ao acessar
# ou modificar um atributo, sem mudar a interface da classe.

class Foo:
    def __init__(self, x = None):
        self._x = x

    @property # decorador de propriedade
    def x(self): # propriedade do tipo get
        return self._x  # retorna o valor de _x
    
    @x.setter
    def x(self, valor): #propriedade do tipo set
        self._x += valor # modifica o valor de _x
    
    @x.deleter
    def x(self): # Atribui um comportamento para x ao ser deletado
        self._x = -1

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    # bloco de propriedades
    @property
    def nome(self):
        return self._nome
    
    @property
    def ano_nascimento(self):
        return self._ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

    # bloco de setters
    @nome.setter
    def nome(self,sobrenome):
        self._nome += sobrenome
    
    @ano_nascimento.setter
    def ano_nascimento(self, ano_corrigido):
        self._ano_nascimento = ano_corrigido

    # bloco de deleters
    @nome.deleter
    def nome(self):
        self._nome = 'Anônimo'
    
    @ano_nascimento.deleter
    def ano_nascimento(self):
        self._ano_nascimento = 2325



opcao = input("Escolha o exemplo que pretende estudar: classe Foo (f) ou classe Pessoa (p) ").strip().lower()

if opcao == 'p':
    # Pessoa
    pessoa = Pessoa('José', 1980) #cria um pessoa onde _nome = 'José' e _ano_nascimento = 1980
    print(pessoa.nome, pessoa.ano_nascimento, f"{pessoa.idade} anos") # José 1980 45 anos 
    pessoa.nome = ' das Couves'    # o sinal de "=" indica que o uso da propriedade nome é um setter
    pessoa.ano_nascimento = 1990
    print(pessoa.nome, pessoa.ano_nascimento) # _nome = 'José das Couves' e _ano_nascimento = 1990
    del pessoa.nome,pessoa.ano_nascimento     # age conforme o deleter para nome
    print(pessoa.nome, pessoa.ano_nascimento) # neste caso, o deleter modifica _nome para 'Anônimo'
                                              # e _ano_nacimento para 2325

elif opcao == 'f':
    # Foo
    foo = Foo(10) #cria um foo onde _x = 10
    print(foo.x)  # mostra o valor do atributo _x do foo através da propriedade x
    foo.x = 10    # o sinal de "=" indica que o uso da propriedade x é um setter
    print(foo.x)  # neste caso, o set é somar o valor 10 em _x
    del foo.x     # age conforme o deleter para x
    print(foo.x)  # neste caso, o deleter modifica _x para -1

