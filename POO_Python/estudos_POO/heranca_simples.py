# conceitos de herança simples

class Veiculo_Automotor:
    # Classe com atributos comuns a todos os veículos automotores
    def __init__(self, placa, cor, num_de_rodas):
        self.placa = placa
        self.cor = cor
        self.num_de_rodas = num_de_rodas
        automotores.append(self)

    def ligar_motor(self):
        print("Ligando o motor...\nLIGOU!!!\n")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(map(str,self.__dict__.values()))}"
              

class Motocicleta(Veiculo_Automotor):
    def empinar(self):
        print("empinei a moto")


class Carro(Veiculo_Automotor):
    #sobrescrevendo o método ligar na clase Carro
    def ligar_motor(self):
        print(f"Ligando o motor do {self.__class__.__name__}...\nLIGOU!!!\n")


class Caminhao(Veiculo_Automotor):
    # sobrescrevendo o construtor
    def __init__(self, placa, cor, num_de_rodas, carregado=False):
         super().__init__(placa, cor, num_de_rodas) # herda de Veiculos_Automotres
         self.carregado = carregado
    #pass

# lista de instâncias de Veiculos_Automotores
automotores =[]

# Cria instâncias
motocicleta = Motocicleta("MMM-1111", "vermelho", 2)
carro = Carro('CCC-2222',"branco",4)
caminhao_vazio = Caminhao('KKK-3333',"preto",6)

# mostra o método de saída do print
[print(auto) for auto in automotores]

# motocicleta, carro e caminhao herdam o método ligar_motor
[auto.ligar_motor() for auto in automotores]
#no entanto, apenas a moto empina
for auto in automotores:
    try:
        auto.empinar()
    except:
        print(f"{auto.__class__.__name__} não empina")

# O caminhão está carregado?
caminhao_cheio = Caminhao("KKK-4444", "preto", 6, True)
print(f"\nO caminhão_cheio {(not caminhao_cheio.carregado)*'não '}está carregado")
print(caminhao_cheio)

print(f"\nO caminhão_vazio {(not caminhao_vazio.carregado)*'não '}está carregado")