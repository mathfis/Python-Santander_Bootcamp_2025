# excecoes_arquivos.py

from pathlib import Path

# Não encontra arquivo
try:
    arquivo = open("nao_tem.txt",'r')
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)

# Tentou abrir pasta 
ROOT_PATH = Path(__file__).parent # pasta onde se encontra o código fonte
try:
    arquivo = open(ROOT_PATH / 'novo-diretorio/', 'r')
except (IsADirectoryError, PermissionError) as exc:  # Captura ambos!
    if isinstance(exc, IsADirectoryError):
        print("Não é possível abrir, pois é um diretório")
    else:  # PermissionError
        print("O sistema bloqueou: tentativa de abrir diretório como arquivo")
    print(exc)

