"""
Descrição
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

📌 Regras para um e-mail válido:

Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
Não pode começar ou terminar com "@".
Não pode conter espaços.
Entrada
Uma string contendo o e-mail a ser validado.
Saída
"E-mail válido" se o e-mail estiver no formato correto.
"E-mail inválido" caso contrário.
"""
# Entrada do usuário
email = input().strip()

# Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
teste = "@" in email
# Não pode começar ou terminar com "@".
teste = teste and ( not email.startswith("@") ) and (not email.endswith("@") )
# Não pode conter espaços.
teste = teste and (" " not in email)

# verifica se termina com ".com"
teste = teste and (email.endswith(".com"))    
""" implementação aceita, porém não admite  '.com.br'
    e outros domínios
"""
# TODO: implementar permitindo outros domínios


# atribui (ou não) o 'in' na mensagem
prefixo = '' if teste == True else "in"

#imprime a mensagem
print(f"E-mail {prefixo}válido")