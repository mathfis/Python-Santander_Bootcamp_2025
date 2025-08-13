def meu_decorador(funcao):
    
    def envelope():
        print("Faz alguma coisa antes de executar")
        funcao()
        print("Faz alguma coisa depois de executar")

    return envelope
    
def ola_mundo():
    print( "Olá, mundo!")

print(ola_mundo()) #Saída normal

"""
Decoradores agregam funcionalidades às funções
"""
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

print("\n forma menos verbosa...\n")

"""
Eles podem ficar menos verbosos ao adicionar @ (açúcar)
"""
@meu_decorador
def oi_mundo():
    print("Oi, mundo!")

oi_mundo()