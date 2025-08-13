import csv
from pathlib import Path 
ROOT_PATH = Path(__file__).parent

#criacao
# try:
#     with open(ROOT_PATH / 'exemplo.csv','w',newline='', encoding='utf-8') as arquivo:
#         writer = csv.writer(arquivo)
#         writer.writerow(["id","nome"])
#         writer.writerow(["1","Maria"])
#         writer.writerow(["2","Joao"])
# except (IOError) as exc:
#     print(f'Erro ao criar o arquivo:{exc}')


#criacao
try:
    with open(ROOT_PATH / 'exemplo.csv','r',newline='', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        print(reader.fieldnames)
        for row in reader:
            print(f"ID:{row['id']}")            
            print(f"NOME:{row['nome']}")
except (IOError) as exc:
    print(f'Erro ao criar o arquivo:{exc}')