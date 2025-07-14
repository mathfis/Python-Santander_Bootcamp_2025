saldo = 1000
saque = 250
limite = 200
conta_especial = True

#expressão de difícil leitura
exp_1 = saldo >= saque  and saque <= limite or conta_especial and saldo >= saque
print(exp_1)
#expressão de leitura mais fácil
exp_2 = (saldo >= saque  and saque <= limite) or (conta_especial and (saldo >= saque)) 
print( exp_2)
# divisão de contas
conta_normal_com_saldo_suficiente = (saldo >= saque) and (saque <= limite)
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_3)