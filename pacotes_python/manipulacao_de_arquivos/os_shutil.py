# os_shutil.py

"""_summary_
"""
import os
import shutil
from pathlib import Path 

#ROOT_PATH = Path(__file__) # caminho do arquivo fonte
ROOT_PATH = Path(__file__).parent # pasta onde se encontra o código fonte

""" os.mkdir() sozinho escreve no diretório raiz e necessita de copiar
caminhos longos, sem caminhos relativos"""
#os.mkdir('novo-diretorio')
"""o método os.mkdir() sobrecarrega a operação / e entende como
um caminho viável até mesmo para windows (onde os diretórios são separados por '\')
"""
#os.mkdir(ROOT_PATH / 'novo-diretorio') #cria novo diretório na pasta onde está o arquivo fonte
#arquivo = open(ROOT_PATH / 'novo.txt','w') # abre o arquivo novo.txt para escrita e cria o arquivo caso não exista
#arquivo.close()

#os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / "novo_arquivo.txt") #renomeia
#os.remove(ROOT_PATH / "novo_arquivo.txt") #remove
shutil.move(ROOT_PATH / 'novo.txt',ROOT_PATH / "novo-diretorio" / 'novo.txt')