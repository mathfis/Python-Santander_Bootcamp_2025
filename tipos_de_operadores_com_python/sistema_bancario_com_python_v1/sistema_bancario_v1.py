# Sistema Bancário com Python - versão 1
"""
    Programa que realiza transações financeiras de
    depósito, saque e extrato 
"""

# Condições pemanentes
LIMITE_DE_SAQUES = 3
SAQUE_MAXIMO = 500.00

# Mensagens permanentes
MENU = f"""
-------------- Bem-vindo ao Banco Matheus Lara! --------------

Escolha a operação que deseja realizar, pressionando as teclas
a seguir:

[d] Depósito

[s] Saque (máximo de {LIMITE_DE_SAQUES} saques diários)

[e] Extrato

[x] Encerrar

"""
ENCERRAMENTO = """
                   Transação Encerrada
              
              O Banco Matheus Lara agradece
                    a sua preferência.
              """ 
MSG_CONTINUA = f"{8*'-'} Digite X (para sair) ou ENTER (para continuar) {8*'-'}\n"

# Variáveis de estado do cliente
saldo = 4000.00
msg_saldo = "Não é possível efetuar o saque por falta de saldo"
extrato = ''
saques_disponiveis = LIMITE_DE_SAQUES

while(True):
    # seleciona a operação
    operacao = input(MENU).lower()
    
    #deposito
    if(operacao == 'd'):
        # solicita o depósito
        deposito = float( input(" Digite o valor que deseja depositar: R$ ") )
        
        # o valor deve ser positivo
        if(deposito > 0):
            saldo += deposito
            extrato += f"> Depósito: +{deposito:.2f}\n"

            msg = f"""
                    Depósito realizado com sucesso!
                    Saldo atual: {saldo:.2f}    
                """
        else:
            msg = f"""
                         Operação não realizada!
                    O valor de depósito digitado é inválido.
                """
        
        print(msg)
        operacao = input(MSG_CONTINUA)
        if(operacao == 'x'):
            break

    #saque
    if(operacao == 's'):
        #imprime o saldo atual e pede o saque
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
        saque = float( input(" Digite o valor que deseja sacar: R$ ") )
          
        # o valor do saque deve ser positivo        
        if(saque <= 0.0):
            msg = f"""
                         Operação não realizada!
                    O valor de saque digitado é inválido.
                """
        
        # saque deve ser menor que o SAQUE_MAXIMO
        elif saque > SAQUE_MAXIMO :
            msg = f"""
                         Operação não realizada!
                    Seu saque máximo é de R$ {SAQUE_MAXIMO}.
                """
        
        # devem haver saques disponiveis
        elif saques_disponiveis <= 0 :
            msg ="""
                        Operação não realizada!
                    Número de saques diário excedido.
                """
        
        # saque deve ser menor ou igual a saldo
        elif saque > saldo :
            msg = f"""
                    Operação não realizada por falta de saldo!
                    Saldo atual: {saldo}
                """
        
        # não ocorreram problemas
        else:
            saques_disponiveis -= 1
            saldo -= saque
            msg = f"""
                    Saque realizado com sucesso!
                    Saldo atual: {saldo:.2f}    
                """
            extrato += f"> Saque: -{saque:.2f}\n"
        
        print(msg)
        operacao = input(MSG_CONTINUA)
        if(operacao == 'x'):
            break

    #extrato
    if(operacao == 'e'):
        # impressão do extrato se não estiver vazio, caso contrário, mensagem de erro
        print(extrato if extrato != '' else f"\n{14*'-'} Não foram realizadas movimentações {14*'-'}\n")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        # proxima ação
        operacao = input(MSG_CONTINUA)
        if(operacao == 'x'):
            break
    
    # Encerrar a transação
    elif(operacao == "x"):
        break
    
    # Operação Inválida
    else:
        print("""
              Operação Inválida
              """)
        

print(ENCERRAMENTO)