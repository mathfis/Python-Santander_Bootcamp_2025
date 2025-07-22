from sistema_bancario_v2 import (
    deposito, saque, imprime_extrato,
    criar_usuario, criar_conta, listar_contas
)

def menu_inicial():
    while True:
        print("""
======== MENU INICIAL ========
[g] Gerente
[c] Correntista
[q] Sair
=============================
""")
        opcao = input("Escolha o perfil de acesso: ").strip().lower()
        if opcao == "g":
            menu_gerente()
        elif opcao == "u":
            menu_correntista()
        elif opcao == "q":
            print("Saindo do sistema de testes.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_gerente():
    while True:
        print("""
======== MENU GERENTE ========
[1] Criar usuário
[2] Criar conta
[3] Listar contas de usuário
[4] Depositar em conta
[5] Sacar de conta
[6] Extrato de conta
[0] Voltar ao menu inicial
=============================
""")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cpf = input("CPF do novo usuário: ").strip()
            nome = input("Nome: ").strip()
            nascimento = input("Data de nascimento: ").strip()
            endereco = input("Endereço: ").strip()
            dados_pessoais = {
                "nome": nome,
                "nascimento": nascimento,
                "endereco": endereco
            }
            usuarios[cpf] = criar_usuario(cpf, dados_pessoais, {})
            print("Usuário criado.")
        elif opcao == "2":
            cpf = input("CPF do usuário para nova conta: ").strip()
            if cpf not in usuarios:
                print("Usuário não encontrado.")
                continue
            agencia = input("Agência: ").strip() or "001"
            saldo = float(input("Saldo inicial: ") or 0)
            limite = float(input("Limite: ") or 500)
            extrato = ""
            numero_saques = 0
            LIMITE_SAQUES = int(input("Limite de saques: ") or 3)
            nova_conta = {
                "agencia": agencia,
                "saldo": saldo,
                "limite": limite,
                "extrato": extrato,
                "numero_saques": numero_saques,
                "LIMITE_SAQUES": LIMITE_SAQUES
            }
            contas_usuario = usuarios[cpf].get("contas", {})
            contas_usuario = criar_conta(contas_usuario, nova_conta)
            usuarios[cpf]["contas"] = contas_usuario
            print("Conta criada.")
        elif opcao == "3":
            cpf = input("CPF do usuário: ").strip()
            listar_contas(cpf, usuarios)
        elif opcao == "4":
            cpf = input("CPF do usuário: ").strip()
            conta_num = input("Número da conta: ").strip()
            valor = float(input("Valor do depósito: "))
            conta = usuarios[cpf]["contas"][conta_num]
            saldo, extrato = deposito(conta["saldo"], valor, conta["extrato"])
            conta["saldo"] = saldo
            conta["extrato"] = extrato
            print("Depósito realizado.")
        elif opcao == "5":
            cpf = input("CPF do usuário: ").strip()
            conta_num = input("Número da conta: ").strip()
            valor = float(input("Valor do saque: "))
            conta = usuarios[cpf]["contas"][conta_num]
            kwargs = {
                "saldo": conta["saldo"],
                "valor": valor,
                "extrato": conta["extrato"],
                "LIMITE": conta["limite"],
                "numero_saques": conta["numero_saques"],
                "LIMITE_SAQUES": conta["LIMITE_SAQUES"]
            }
            saldo, extrato, numero_saques = saque(**kwargs)
            conta["saldo"] = saldo
            conta["extrato"] = extrato
            conta["numero_saques"] = numero_saques
            print("Saque realizado.")
        elif opcao == "6":
            cpf = input("CPF do usuário: ").strip()
            conta_num = input("Número da conta: ").strip()
            conta = usuarios[cpf]["contas"][conta_num]
            imprime_extrato(conta["saldo"], conta["extrato"])
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_correntista():
    cpf = input("Informe seu CPF: ").strip()
    if cpf not in usuarios:
        print("Usuário não encontrado.")
        return
    while True:
        print("""
====== MENU CORRENTISTA ======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Listar minhas contas
[0] Voltar ao menu inicial
=============================
""")
        opcao = input("Escolha uma opção: ").strip()
        contas_usuario = usuarios[cpf].get("contas", {})
        if not contas_usuario:
            print("Você não possui contas cadastradas.")
            if opcao == "0":
                break
            continue
        if opcao == "1":
            conta_num = input("Número da conta: ").strip()
            valor = float(input("Valor do depósito: "))
            conta = contas_usuario[conta_num]
            saldo, extrato = deposito(conta["saldo"], valor, conta["extrato"])
            conta["saldo"] = saldo
            conta["extrato"] = extrato
            print("Depósito realizado.")
        elif opcao == "2":
            conta_num = input("Número da conta: ").strip()
            valor = float(input("Valor do saque: "))
            conta = contas_usuario[conta_num]
            kwargs = {
                "saldo": conta["saldo"],
                "valor": valor,
                "extrato": conta["extrato"],
                "LIMITE": conta["limite"],
                "numero_saques": conta["numero_saques"],
                "LIMITE_SAQUES": conta["LIMITE_SAQUES"]
            }
            saldo, extrato, numero_saques = saque(**kwargs)
            conta["saldo"] = saldo
            conta["extrato"] = extrato
            conta["numero_saques"] = numero_saques
            print("Saque realizado.")
        elif opcao == "3":
            conta_num = input("Número da conta: ").strip()
            conta = contas_usuario[conta_num]
            imprime_extrato(conta["saldo"], conta["extrato"])
        elif opcao == "4":
            listar_contas(cpf, usuarios)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    
    usuarios = {}
    contas = {}
    menu_inicial()  