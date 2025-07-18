# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for i in range(n):
    linha = input().strip()
    posicao_vigula = linha.rfind(",")
    participante = linha[:posicao_vigula]
    tema = linha[posicao_vigula+1:].strip()
    
    if tema not in eventos.keys():
        eventos[tema] = [participante]
    else:
        eventos[tema].append(participante)
    

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")