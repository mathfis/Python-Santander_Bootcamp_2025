"""
1) funções em python são objetos de primeira classe
Ou seja, as funções podem ser passadas como argumentos
"""

def dizer_oi():
    return "Oi!"

def dizer_msg_e_tchau(func,status=""):
    # a função abaixo deve ter a mesma saída que
    #return f"{func().strip('!')} e tchau!"

    """
    3) A função pode retornar uma outra função
    """
    status = status.lower()
    if status == "acabei de chegar":
        return func

    """
    2) É possível criar funções dentro de funções
    São as funções internas (inner functions)
    """
    char = func()[-1]
    def retira_caractere(func=None, char=""):

        if func == None:
            return
        
        frase_sem_char=''
        frase = func()
        for letra in frase:
            if letra != char:
                frase_sem_char += letra
        
        return frase_sem_char

    return f"{retira_caractere(func,char)} e tchau!"
            
print(dizer_oi()) # 1) imprime "Oi!"
print(dizer_msg_e_tchau(dizer_oi)) # 2) imprime "Oi e tchau!"
print(dizer_msg_e_tchau(func=dizer_oi,status="acabei de chegar")()) # 3) imprime "Oi!"