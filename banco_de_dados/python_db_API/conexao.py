import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent


# CRIAÇÃO DO BANCO
def criar_tabela(conexao,cursor):
    # comandos para criar o banco
    comandos_sql = "CREATE TABLE clientes(" \
            "id INTEGER PRIMARY KEY AUTOINCREMENT," \
            "nome VARCHAR(100)," \
            "email VARCHAR(150)" \
            ")"
    ## o método execute recebe os comandos SQL a serem utilizados
    cursor.execute(comandos_sql)    
    ## envia as alterações ao banco
    conexao.commit()

# INSERE dados de nome e email
def inserir_registro(conexao,cursor):
    comandos_sql = "INSERT INTO clientes(nome, email) VALUES (?,?)" # uma tupla com dois valores deve ser informada
                                                                    # (?, ?) utilizada para evitar injeção de SQL https://realpython.com/prevent-python-sql-injection/
    valores = ("Sicrana", "sicrana@servidor_de_email.com.br")
    cursor.execute(comandos_sql, valores)
    conexao.commit()

# ATUALIZA registros
def atualizar_registros(conexao,cursor):
    comandos_sql = "UPDATE clientes SET nome = ?, email = ?" \
                "WHERE id = ?"
    valores = ("Beltrana", "beltrana@servidor_de_email.com.br",2)
    cursor.execute(comandos_sql, valores)
    conexao.commit()

# REMOVER registros
def remover_registros(conexao,cursor):
    comandos_sql = "DELETE FROM clientes WHERE id = ?"
    valores = (3,) #tuplas com um único valor precisam ter uma virgula
    cursor.execute(comandos_sql, valores)
    conexao.commit()

def inserir_muitos_registros(conexao,cursor,dados):
    # dados deve ser uma lista de tuplas com dois dados
    comandos_sql = "INSERT INTO clientes(nome, email) VALUES (?,?)"
    try:
        cursor.executemany(comandos_sql, dados) #executemany permite que um comando possa ser utilizado várias vezes
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu um erro {e}")
        conexao.rollback() # desfaz o que havia sido feito no try
    finally:
        conexao.commit()

def recuperar_cliente(cursor,identif):
    comandos_sql = "SELECT * FROM clientes WHERE id=?"
    cursor.execute(comandos_sql,(identif,))
    return cursor.fetchone()

def listar_clientes(cursor):
    comandos_sql = "SELECT nome,email,id FROM clientes ORDER BY nome"
    return cursor.execute(comandos_sql)
    

# FIM DA BIBLIOTECA DE FUNCOES

# criando conexão com o banco
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
# criando o objeto cursor, que será utilizado para executar comandos no banco
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row  # visualizar as saídas como dicionario

#criar_banco(conexao,cursor)
#inserir_registro(conexao,cursor)
#atualizar_registros(conexao,cursor)
#remover_registros(conexao,cursor)

registros = [("Sicrana", "sicrana@servidor_de_email.com.br"),
             ("Beltrana", "beltrana@servidor_de_email.com.br"),
             ("José", "ze@servidor_de_email.com.br")
            ]
inserir_muitos_registros(conexao, cursor, registros)    

# mostra valor de consulta
#print(dict(recuperar_cliente(cursor, 1)),"\n") 

# mostra registros da lista de consultas
# for registro in listar_clientes(cursor):
#     print(dict(registro))
