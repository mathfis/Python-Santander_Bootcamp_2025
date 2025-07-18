"""
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário
previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar
a estrutura e a eficiência do sistema, implementando as operações de 
depósito, saque e extrato em funções específicas.
Você terá a chance de refatorar o código existente, dividindo-o em
funções reutilizáveis, facilitando a manutenção e o entendimento do sistema
como um todo. Prepare-se para aplicar conceitos avançados de programação e 
demonstrar sua habilidade em criar soluções mais elegantes e eficientes 
utilizando Python.

Descrição completa em: https://web.dio.me/project/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba

"""

#
# criar funções para todas as operações do sistema (elas terão regras de passagem diferentes)
#
#TODO 1- função saque deve receber os argumentos apenas por nome (keyword only) 
        # argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques;
        # retorno: saldo e extrato
#TODO 2- função deposito deve receber os argumentos apenas por posição (positional only) 
        # argumentos: saldo, valor, extrato;
        # retorno: saldo e extrato
#TODO 3- função extrato deve receber os argumentos por posição e nome (positional online e keyword only) 
        # argumentos: saldo (posicional), extrato(nomeado);
        # retorno: None. Ela imprime o extrato.
#
# Novos comportamentos
#
#TODO 4- função criar_usuario que cria usuario. Um usuário é composto por nome, data de nascimento, cpf e
    # endereço. O endereço é uma string com o formato "logradouro, nro - bairro - cidade/sigla_estado". O cpf
    # deve conter apenas números 2 usuários não podem ter o mesmo cpf.
        # argumentos: 
        # retorno: 
#TODO 5- função criar_conta que cria conta. O programa deve armazenar contas em uma lista, onde cada conta é
    # composta por agência, número e usuário. O número da conta é sequencial, começando em 1. O número da
    # agência é fixo ("0001"). O usuário pode ter mais de uma conta, mas uma conta deve pertencer a somente
    # um usuário.
    #       Dica: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado
    #       para cada usuário da lista.
        # argumentos:
        # retorno: 
#TODO 6 - função listar_contas 
        # argumentos:
        # retorno: 

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")