saldo = 500

# Acrescenta 100 a saldo
saldo +=100 
print(saldo)


# Deduz 50 de saldo
saldo -= 50
print(saldo)


# Multiplica saldo por 2
saldo *= 2
print(saldo)


# Divide saldo por 4
saldo /= 4
print(saldo)


# Atribui a saldo a parte inteira de sua divisão por 2
saldo //= 15 # retornará tipo inteiro apenas se saldo for inteiro
print(saldo)  # caso contrário, deve retornar um float com parte decimal nula

# Atribui a saldo o resto da divisão inteira de saldo por 10
saldo %= 10
print(saldo)

# eleva saldo ao quadrado
saldo**=2
print(saldo)
