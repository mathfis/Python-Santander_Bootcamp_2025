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
def inserir_parametros_de_conta(parametros_conta = {}):
    #verifica se os parâmetros já foram informados
    if parametros_conta != {}:
        print("Parâmetros da conta já informados.")
        return parametros_conta
    
    # Deseja criar conta padrão?
    if input("Deseja criar conta padrão? (s/n): ").strip().lower() == "s":
        parametros_conta = {
            "agencia":"001", "saldo": 0, "limite": 500, "extrato": "", 
            "numero_saques": 0, "LIMITE_SAQUES": 3
        }
    else: # se não, solicita os parâmetros
        print("Informe os parâmetros da conta:")
        entrada = input("Informe saldo, limite e limite de saques (separados por vírgula):\n")
        saldo, limite, LIMITE_SAQUES = [item.strip() for item in entrada.split(',')]
        agencia, extrato, numero_saques = "0001", "", 0
        parametros_conta = {
            "agência":agencia, "saldo": float(saldo), "limite": float(limite), "extrato": extrato,
            "numero_saques": int(numero_saques), "LIMITE_SAQUES": int(LIMITE_SAQUES)
        }

    
    return parametros_conta


def criar_conta(contas= {},nova_conta = {}):
    ultimo_numero = max([int(k) for k in contas.keys()]) if contas else 0
    novo_numero = str(ultimo_numero + 1)
    nova_conta_vazia = nova_conta == {}
    
    nova_conta = inserir_parametros_de_conta() if nova_conta_vazia else nova_conta
    contas[novo_numero] = nova_conta 

    print("Criando uma nova conta...")

    return contas


def criar_usuario(cpf_usuario, dados_pessoais = {}, contas = {}, primeira_conta = {}):
    """Cria um usuário com os dados fornecidos.
    Args:
        cpf_usuario (str): CPF do usuário, deve conter apenas números.
        dados_pessoais (dict): Dicionário com os dados pessoais do usuário, incluindo nome, data de nascimento e endereço.  
    Returns:
        dict: Dicionário com os dados do usuário, incluindo CPF, dados pessoais e contas.
    """
    usuario = {}
    usuario["cpf"] = cpf_usuario.strip()

    msg_dados_pessoais = """Informe os dados pessoais do usuário:
        Exemplo: nome, data de nascimento, endereço (logradouro, nro - bairro - cidade/sigla_estado)"""

    if not dados_pessoais:
        print(msg_dados_pessoais)
        entrada = input("Informe nome; data de nascimento; endereço (logradouro, nro - bairro - cidade/sigla_estado):\n")
        nome, nascimento, endereco = [item.strip() for item in entrada.split(';')]
        dados_pessoais = {
            "nome": nome, "nascimento": nascimento, "endereco": endereco
        }
    
    usuario["dados"] = dados_pessoais
    
    criar_uma_conta = "s" == input("Deseja criar uma conta? (s/n): ").strip().lower()
    if criar_uma_conta:
        contas = criar_conta(contas, primeira_conta)

    usuario["contas"] = contas
    
    return usuario

def listar_contas(cpf_usuario, usuarios):
    """Lista as contas do usuário.
    
    Args:
        contas (dict): Dicionário com as contas do usuário, onde a chave é o número da conta e o valor é um dicionário com os dados da conta.
    
    Returns:
        None
    """
    if cpf_usuario not in usuarios:
        print("Usuário não encontrado.")
        return
    
    usuario = usuarios[cpf_usuario]
    contas = usuario["contas"]
    
    if not contas:
        print("Nenhuma conta encontrada para o usuário.")
        return
    
    print(f"\nContas do usuário {usuario['dados']['nome']} (CPF: {usuario['cpf']}):")
    for numero_conta, dados_conta in contas.items():
        print(f"Conta número: {numero_conta}, Dados da conta: {dados_conta}")


def saque(*, saldo, valor, extrato, LIMITE, numero_saques, LIMITE_SAQUES):
    """ Função para realizar o saque de um valor da conta do cliente.

    Args:
        saldo (_float_): _Valor na conta do cliente_
        valor (_float_):  _Valor a ser sacado_
        extrato (_String_): _Extrato da conta do cliente_
        LIMITE (_float_): _Valor máximo que pode ser sacado_
        numero_saques (_int_): _ Número de saques realizados_
        LIMITE_SAQUES (_int_): _Número máximo de saques permitidos_

    Returns:
        _float_: _saldo após a transação_
        _String_: _extrato com a transação_
        _int_: _numero de saques realizados após a transação_
    """
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > LIMITE

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


    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato,/):
    """ Função para realizar o depósito de um valor na conta do cliente.

    Args:
        saldo (_float_): _Valor na conta do cliente_
        valor (_float_):  _Valor a ser depositado_
        extrato (_String_): _Extrato da conta do cliente_

    Returns:
        _float_ : _saldo após a transação_
        _String_: _extrato com a transação_ 
    """

    if  valor > 0:        
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def imprime_extrato(saldo, extrato):
    """ Função para exibir o extrato da conta do cliente.

    Args:
        saldo (_float_): _Valor na conta do cliente_
        extrato (_String_): _Extrato da conta do cliente_

    Returns:
        None
    """
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=========================================\n")


def operacoes_conta( saldo = 0, limite = 500, extrato = "",
                        numero_saques = 0, LIMITE_SAQUES = 3):
    
    menu_conta = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:

        opcao = input(menu_conta)

        if opcao == "d": # depósito 
            valor = float(input("Informe o valor do depósito: ").strip())
            # Aqui, estamos criando uma lista os argumentos necessários para a função deposito
            # Os argumentos são passados como posição, ou seja, na ordem em que foram definidos na função.
            # Isso permite que a função deposito receba os argumentos por posição, conforme solicitado.
            # args é uma lista que contém os argumentos para a função deposito
            args = [saldo, valor, extrato]    
            # Chamada da função deposito com os argumentos por posição
            # Aqui, estamos passando os argumentos necessários para a função deposito   
            # A função deposito recebe os argumentos por posição e retorna o saldo e o extrato atualizados
            saldo, extrato = deposito(*args)

        elif opcao == "s": # saque 
            valor = float(input("Informe o valor do saque: ").strip())
            # Aqui, estamos criando um dicionário com os argumentos necessários para a função saque
            # Os argumentos são passados como pares chave-valor, onde a chave é o nome do argumento
            # e o valor é a variável correspondente.
            # Isso permite que a função saque receba os argumentos por nome, conforme solicitado.
            # kwargs é um dicionário que contém os argumentos nomeados para a função saque
            
            kwargs = {
                "saldo": saldo,  "valor": valor, "extrato": extrato,
                "LIMITE": limite, "numero_saques": numero_saques, "LIMITE_SAQUES": LIMITE_SAQUES
            }
            # Chamada da função saque com os argumentos nomeados
            # Aqui, estamos passando os argumentos necessários para a função saque

            saldo, extrato, numero_saques = saque(**kwargs)

        elif opcao == "e": # extrato
            imprime_extrato(saldo,extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    return saldo, extrato