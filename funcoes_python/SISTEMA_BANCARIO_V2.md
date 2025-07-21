# Sistema Bancário v2 - Projeto Python

Este projeto é uma solução completa para um sistema bancário simples, desenvolvido em Python, com foco em organização, clareza e boas práticas de funções. Ele permite a criação e gerenciamento de usuários e contas, além de operações financeiras como depósito, saque e extrato, com menus separados para gerente e correntista.

## Funcionalidades

- **Depósito**: Realize depósitos em contas, com validação de valores.
- **Saque**: Realize saques respeitando limite de valor e quantidade de saques.
- **Extrato**: Visualize todas as movimentações e o saldo da conta.
- **Criar Usuário**: Cadastro de usuários únicos pelo CPF.
- **Criar Conta**: Criação de contas vinculadas a usuários existentes.
- **Listar Contas**: Exibição das contas cadastradas de cada usuário.
- **Menus separados**: Menu inicial para escolha de perfil (gerente ou correntista), com permissões distintas.

## Regras de Implementação

- **Função de Saque**: Recebe argumentos apenas por nome (keyword only).
- **Função de Depósito**: Recebe argumentos apenas por posição (positional only).
- **Função de Extrato**: Recebe saldo por posição e extrato por nome.
- **Função Criar Usuário**: Cadastro com nome, data de nascimento, CPF (apenas números) e endereço. Não permite CPFs duplicados.
- **Função Criar Conta**: Vincula conta a usuário existente pelo CPF. Número da conta é sequencial e agência padrão ("001").
- **Função Listar Contas**: Exibe todas as contas cadastradas de um usuário.

## Como Utilizar

1. Clone ou baixe este repositório.
2. Execute o arquivo `teste_sistema_bancario_v2.py` em Python 3.
3. Utilize o menu interativo para realizar operações bancárias como gerente ou correntista.

## Exemplo de Menu

```
======== MENU INICIAL ========
[g] Gerente
[c] Correntista
[q] Sair
=============================
```

Cada perfil possui menus próprios, com permissões adequadas.

## Testagem

Um roteiro detalhado de testagem está disponível no arquivo `roteiro_de_testagem_sistema_bancario_v2.md`, permitindo que qualquer pessoa valide todas as funcionalidades do sistema, mesmo sem conhecimento prévio do código.

## Referência do Desafio

Desafio original disponível em:  
[DIO - Otimizando o Sistema Bancário com Funções Python](https://web.dio.me/project/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba)

---

Desenvolvido para o Santander Bootcamp 2025 por Matheus Lara.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/laramatheus/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mathfis)