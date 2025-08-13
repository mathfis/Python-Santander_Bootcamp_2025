# Manipulação de Arquivos

## Leitura de Arquivos
def le_arquivo_com_read(caminho,codificacao='utf-8'):
    """abertura de um arquivo para leitura em codificação utf-8
    modos: leitura ('r'), gravação ('w') e anexação ('a')"""
    arquivo = open(caminho,'r',encoding=codificacao)
    # le todo o arquivo
    print("Lendo tudo com read()...\n") 
    leitura = arquivo.read()
    arquivo.close()
    return leitura

def le_arquivo_com_readline(caminho,n_linhas = 1,codificacao='utf-8',leitura=None, arquivo=None):
    if leitura is None:
        arquivo = open(caminho,'r',encoding=codificacao)
        print('\nLendo por linha com readline()...')
        return le_arquivo_com_readline(caminho,n_linhas,codificacao,leitura=[],arquivo=arquivo)
    else:
        linha = (arquivo.readline())*(n_linhas != 0)
        leitura.append(linha) if linha else arquivo.close()    
        return le_arquivo_com_readline(caminho,n_linhas - 1,codificacao,leitura,arquivo) if linha else "".join(leitura)

def le_arquivo_com_readlines(caminho, linha_fim = None, linha_ini = None, codificacao='utf-8'):
    
    arquivo = open(caminho,'r',encoding=codificacao)
    print("\nLendo por linha com readlines()...")
    lista_de_linhas = arquivo.readlines()[0:linha_fim] if linha_ini is None else arquivo.readlines()[linha_ini-1:linha_fim]  
    arquivo.close()
    
    saida = ''
    for linha in lista_de_linhas:
        saida = saida+linha
    
    return saida

def leitura_otimizada(caminho,codificacao='utf-8'):
    arquivo = open(caminho,'r',encoding=codificacao)
    print("\nLendo por linha com readline() de forma otimizada...")
    # leitura otimizada
    saida = ''
    while(len(linha:=arquivo.readline())):# := é comparação e atribuição
        saida = saida+linha
    arquivo.close()
    return(saida)

## Escrita de Arquivos
#escrita de string inteira
def escreve_com_write(texto,caminho,codificacao='utf-8'):
    """abertura de um arquivo para escrita em codificação utf-8
    modos: leitura ('r'), gravação ('w') e anexação ('a')"""
    arquivo = open(caminho,'w',encoding=codificacao)
    # le todo o arquivo
    print("Escrevendo tudo com read()...\n") 
    leitura = arquivo.write(texto)
    arquivo.close()
    return leitura

#TODO: escrita com writelines
def escrita_com_writelines():
    pass

#TODO: escrita otimizada
def escrita_otimizada():
    pass

#ler e escrever no sistema
pasta = "c:/Users/mlara/Tec/Dio/Python-Santander_Bootcamp_2025/pacotes_python/manipulacao_de_arquivos/"
arquivo = f"{pasta+'escrita.txt'}"


texto = """
        Escrevendo linhas
        linha 1
        linha 2
        linha 3
        linha 4
        linha 5
        linha 6        
        """
escreve_com_write(texto,arquivo)
print(le_arquivo_com_read(arquivo))
#print(le_arquivo_com_readline(ler,5))
#print(le_arquivo_com_readlines(ler))
#print(leitura_otimizada(ler))

#print('\nOs arquivos foram lidos de 4 formas diferentes')

