# boas_praticas_arquivos.py

from pathlib import Path 
ROOT_PATH = Path(__file__).parent
"""
Utilização do with
"""
try:
    with open(ROOT_PATH / 'exemplo.txt','r',encoding='utf-8') as arquivo:
    # abre e fecha arquivos de forma automatizada e com segurança
        print('trabalhando com o arquivo')
    #1/0
except ZeroDivisionError as exc:
    print('Problema ao realizar a divisao', exc)
except IOError as exc:
    print("Erro ao abrir o arquivo\n", exc)

