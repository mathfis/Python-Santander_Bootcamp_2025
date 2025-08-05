import functools #introspecção

def meu_decorador(funcao):
    
    #@functools.wraps(funcao) # introspecção
    
    def envelope(*args,**kwargs): #os argumentos permitem entradas mais genéricas
        print("Faz alguma coisa antes de executar")
        resultado = funcao(*args,**kwargs)
        print("Faz alguma coisa depois de executar")
        return resultado
    
    return envelope
    
@meu_decorador
def oi_mundo(nome, qualquer_coisa):
    print(f"Oi mundo, {nome}!")
    return nome.upper()

resultado = oi_mundo('João', 1000)
print(resultado) #imprime a alteração feita em 'joão'

print(oi_mundo.__name__) # sem o decorador de introspecção
                         # a função retornada seria envelope