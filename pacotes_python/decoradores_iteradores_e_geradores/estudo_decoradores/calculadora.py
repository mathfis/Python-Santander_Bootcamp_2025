def calculadora(operacao):

    """
    define funções internas
    """
    def som(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

    match operacao:
        case "+":
            return som
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div

for op in ("+","-","*","/"):
    print(calculadora(op)(2,2))