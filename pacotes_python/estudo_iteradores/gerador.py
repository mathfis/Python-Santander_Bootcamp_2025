"""
Geradores são iteradores que, ao contrário de outros iteradores,
não armazenam todos os seus valores na memória

- retornam valores com "yield" ao invés de "return"
- não podem ter valores recuperados depois de utilizados
- 

"""

def meu_gerador(numeros:list[int]):
    for numero in numeros:
        yield numero*2

for i in meu_gerador(numeros=[1,2,3]):
    print(i)