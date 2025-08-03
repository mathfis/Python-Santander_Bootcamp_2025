from SistemaBancario_POO_v1 import (PessoaFisica,ContaCorrente)

def listar_contas(contas):
    for conta in contas:
        print(f"Conta Corrente:agencia {conta.agencia}, número {conta.numero}")

def imprime_extrato(conta):
    print(f"Extrato da conta {conta.numero}")
    print(conta.historico)
    print(f"saldo: {conta.saldo}")


def menu_inicial():
    while True:
        print("""
======== MENU INICIAL ========
[g] Gerente
[c] Correntista
[s] Sair
=============================
""")
        opcao = input("Escolha o perfil de acesso: ").strip().lower()
        if opcao == "g":
            menu_gerente()
        elif opcao == "c":
            menu_correntista()
        elif opcao == "s":
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
        if opcao == "1": #Criar Usuário
            # entrada dos dados
            cpf = input("CPF do novo usuário: ").strip()
            nome = input("Nome: ").strip()
            nascimento = input("Data de nascimento: ").strip()
            endereco = input("Endereço: ").strip()
            #criação do usuario
            usuarios[cpf] = PessoaFisica(endereco, cpf, nome, nascimento)
            print("Usuário criado.")
        
        elif opcao == "2": # Criar Conta
            cpf = input("CPF do usuário para nova conta: ").strip()
            if cpf not in usuarios:
                print("Usuário não encontrado.")
                continue
            agencia = input("Agência: ").strip() or "001"
            saldo = float(input("Saldo inicial: ") or 0)
            limite = float(input("Limite: ") or 500)
            LIMITE_SAQUES = int(input("Limite de saques: ") or 3)

            #cria conta
            conta = ContaCorrente(numero=len(usuarios[cpf].contas)+1,
                                  n_saques=0,
                                  cliente=usuarios[cpf],
                                  limite=limite,
                                  limite_saques=LIMITE_SAQUES,
                                  agencia= agencia)
            conta.saldo = saldo
            #adiciona nova conta à lista de contas do usuario
            usuarios[cpf].contas = conta
            print("Conta criada.")

        elif opcao == "3": # listar contas de usuário
            cpf = input("CPF do usuário: ").strip()
            print(f"usuario: {usuarios[cpf].cpf}")
            print("Contas...")
            listar_contas(usuarios[cpf].contas)
        
        elif opcao == "0": # voltar
            break

        else:            
            cpf = input("CPF do usuário: ").strip()
            if cpf not in usuarios:
                print("Usuário não encontrado.")
                continue
                
            #conta a ser operada
            try: #conta é um inteiro
                conta_num = int(input("Número da conta: ").strip())
                contas = usuarios[cpf].contas
            except: # inseriu valor inválido 
                print("Número de conta inválido.")
                continue
                    
            # Encontrar a conta com o número correspondente
            conta = None
            for c in contas:
                if c.numero == conta_num:
                    conta = c
                    break
                    
            if not conta:
                print("Conta não encontrada.")
                continue
                    
            if opcao == "6": #extrato
                imprime_extrato(conta)
                    
            elif opcao == "4": # depósito    
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
                print("Depósito realizado.")
                        
            elif opcao == "5":  # saque
                valor = float(input("Valor do saque: "))
                sucesso = conta.sacar(valor)
                if sucesso:
                    print("Saque realizado.")
                else:
                    print("Saque não realizado. Verifique saldo ou limite de saques.")
                        
            else: # digitou errado
                print("Opção inválida. Tente novamente.")


def menu_correntista():
    cpf = input("Informe seu CPF: ").strip()

    if cpf not in usuarios:
        print("Usuário não encontrado.")
        return
    usuario = usuarios[cpf]

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
        
        if not usuario.contas:
            print("Você não possui contas cadastradas.")
            continue

        if opcao == "0":
            break
        elif opcao == "4":
            listar_contas(usuario.contas)
            continue
            
        # Para outras opções (1, 2, 3), pedimos o número da conta
        try:
            conta_num = int(input("Número da conta: ").strip())
            conta = None
            for c in usuario.contas:
                if c.numero == conta_num:
                    conta = c
                    break
                    
            if not conta:
                print("Conta não encontrada.")
                continue
                
            if opcao == "1":
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
                print("Depósito realizado.")
            elif opcao == "2":
                valor = float(input("Valor do saque: "))
                sucesso = conta.sacar(valor)
                if sucesso:
                    print("Saque realizado.")
                else:
                    print("Saque não realizado. Verifique saldo ou limite de saques.")
            elif opcao == "3":
                imprime_extrato(conta)
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Número de conta inválido.")


if __name__ == "__main__":
    
    usuarios = {}
    contas = {}
    menu_inicial()  