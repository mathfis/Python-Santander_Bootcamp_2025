"""
Descrição
Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

📌 Regras de desconto:

"DESCONTO10": 10% de desconto.
"DESCONTO20": 20% de desconto.
"SEM_DESCONTO": Sem desconto.
Entrada
Preço original do produto.
Código do cupom digitado.
Saída
Preço final após aplicar o desconto. Com duas casas decimais.
"""
# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()

# Verifica se o cupom está no dicionário
desconto = descontos[cupom] if cupom in descontos.keys() else 0

preco *= (1-desconto)
print(f"{preco:.2f}")