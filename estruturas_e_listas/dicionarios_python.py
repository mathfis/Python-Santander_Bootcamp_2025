# dicionarios com python
pessoa = {"nome":"Guilherme","idade":28}
mesma_pessoa = dict(nome="Guilherme",idade=28)
pessoa["telefone"] = "3333-1234"

print(pessoa, mesma_pessoa, pessoa==mesma_pessoa)

print(pessoa["nome"],pessoa["idade"],pessoa["telefone"])

#print(mesma_pessoa["nome"],mesma_pessoa["idade"],mesma_pessoa["telefone"])
print(mesma_pessoa.get("nome"),mesma_pessoa["idade"],mesma_pessoa.get("telefone"))

for chave, valor in pessoa.items():
    print(chave,": ",valor)

# Métodos class dict

mesma_pessoa = pessoa.copy()
print(mesma_pessoa)
mesma_pessoa.clear()
print(mesma_pessoa.fromkeys(["nome","idade","telefone"]))
print(mesma_pessoa) 
mesma_pessoa = mesma_pessoa.fromkeys(["nome","idade","telefone"])
print(mesma_pessoa) 
mesma_pessoa = mesma_pessoa.fromkeys(["nome","idade","telefone"], "vazio")
print(mesma_pessoa) 
