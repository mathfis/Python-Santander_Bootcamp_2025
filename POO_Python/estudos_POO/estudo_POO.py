# Estudo de Programa Orientada a Objetos

# Classe define características e comportamentos de um objeto
# Objeto é uma instância de uma classe  

# modelagem de bicicleta

class Bicicleta:
    # construtor da classe Bicicleta
    def __init__(self, cor, modelo, ano, valor):
        print("criando uma bicicleta...\n")
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    # Destrutor da classe bicicleta
    # Pouco necessário no python porque ele já administra esta memória
    # Mas pode ser importante para executar alguma ação antes de destruir o objeto 
    def __del__(self):
        print("Bicicleta destruída!\n")

    def buzinar(self):
        print("trim trim\n")
    
    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!\n")

    def correr(self):
        print("Iuuuupiiiii!!!\n")

    # definindo apresentação da classe.
    def __str__(self):
        # return (f"Bicicleta: cor= {self.cor},"+\
        #         f" modelo= {self.modelo}," +\
        #         f" ano={self.ano}, valor={self.valor}")
        nome_da_classe = self.__class__.__name__
        lista_de_atributos=[
                            f'{chave}={valor}'
                            for chave, valor in self.__dict__.items()
                            ]
        return f"{nome_da_classe}:{', '.join(lista_de_atributos)}\n"
        # esta forma possui a vantagem de exibir uma saída de atributos
        # mesmo quando a quantidade de atributos for modificada
    


# criando objeto
b1 = Bicicleta("vemelha", "caloi", 2022, 600)

#obtendo atributos
print(b1.cor, b1.modelo, b1.ano, b1.valor, sep=", ")

#chamando métodos
b1.buzinar()
b1.correr()
b1.parar()

# mostrando a saída padrão modificada
print(b1)