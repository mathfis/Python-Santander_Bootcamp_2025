def msg_comparacao(valor1, valor2, comparacao):
    """
    Retorna a string da comparacao entre dois valores.
    As comparações podem ser de valores 'igual', 'diferente',
    'menor','maior', 'menor ou igual', 'maior ou igual'.   
    """
    #  questionamento
    print("\nÉ "+comparacao+"?",end=' ')
    # comparações
    
    if(comparacao == "igual"):#igual        
        return f"{(not(valor1 == valor2))*'não '}é {comparacao} a"
    elif(comparacao =="diferente"):# diferente
        return f"{(not(valor1 != valor2))*'não '}é {comparacao} a"
    elif(comparacao == "menor"):# menor
        return f"{(not(valor1 != valor2))*'não '}é {comparacao} a"
    elif(comparacao == "maior"):# maior
        return f"{(not(valor1 != valor2))*'não '}é {comparacao} a"
    elif(comparacao == "menor ou igual"):# menor ou igual
        return f"{(not(valor1 != valor2))*'não '}é {comparacao} a"
    elif(comparacao == "maior ou igual"):# maior ou igual
        return f"{(not(valor1 != valor2))*'não '}é {comparacao} a"
    else:
        print("Comparação desconhecida! Os valores de comparação precisam ser " \
        "'igual', 'diferente', 'menor', 'maior', 'menor ou igual' ou 'maior ou igual'.") 
        return "não pode ser comparado com"
    # fim da função print_comparacao

#teste
def mostra_comparacoes_2a2(valor_1, valor_2, naturezas):
    """
    organiza um loop para imprimir na tela se as comparações são verdadeiras
    """
    print(f"\n{naturezas[0]} = {valor_1}, {naturezas[1]} = {valor_2}")
    comps = ('igual', 'diferente', 'menor', 'maior', 'menor ou igual', 'maior ou igual','mais bonito')
    for comp in comps:
        compara_str = msg_comparacao(valor_1, valor_2, comp)
        print(f"{naturezas[0].capitalize()} {compara_str} {naturezas[1]}.")


mostra_comparacoes_2a2(450, 200, ('saldo','saque'))

