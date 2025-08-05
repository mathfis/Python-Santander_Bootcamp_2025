class MeuIterador:

    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0 #inicializa o contador em zero
    def __iter__(self):
        return self 

    def __next__(self):
        try:
            numero = self.numeros[self.contador] # obtem o elemento da posição contador da lista oferecida
            self.contador+=1 #acresce o contador em 1
            return numero*2 #retorna o número da lista duplicado
        except IndexError: #contador excede o tamanho de numeros
            raise StopIteration #parada


for i in MeuIterador([1,2,3]):
    print(i)

print("iterei")