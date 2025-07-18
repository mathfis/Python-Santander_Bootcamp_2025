# Otimizando o Sistema Bancário com Funções Python

Este projeto tem como objetivo refatorar e otimizar um sistema bancário simples, utilizando funções Python para organizar e facilitar a manutenção do código. O desafio propõe a implementação das operações de depósito, saque, extrato, criação de usuários e contas, além da listagem de contas, cada uma com regras específicas de passagem de argumentos.

## Funcionalidades

- **Depósito**: Função recebe argumentos apenas por posição (positional only).
- **Saque**: Função recebe argumentos apenas por nome (keyword only).
- **Extrato**: Função recebe argumentos por posição e nome (positional only e keyword only).
- **Criar Usuário**: Cadastro de usuários únicos pelo CPF.
- **Criar Conta**: Criação de contas vinculadas a usuários existentes.
- **Listar Contas**: Exibição das contas cadastradas.

## Regras de Implementação

- **Função de Saque**: Recebe saldo, valor, extrato, limite, número de saques e limite de saques apenas por nome. Retorna saldo e extrato atualizados.
- **Função de Depósito**: Recebe saldo, valor e extrato apenas por posição. Retorna saldo e extrato atualizados.
- **Função de Extrato**: Recebe saldo por posição e extrato por nome. Apenas imprime o extrato.
- **Função Criar Usuário**: Cadastro com nome, data de nascimento, CPF (apenas números) e endereço. Não permite CPFs duplicados.
- **Função Criar Conta**: Vincula conta a usuário existente pelo CPF. Número da conta é sequencial e agência fixa ("0001").
- **Função Listar Contas**: Exibe todas as contas cadastradas.

## Como Utilizar

1. Clone o repositório.
2. Execute o arquivo principal em Python.
3. Utilize o menu interativo para realizar operações bancárias.

## Exemplo de Menu

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> 
```

## Referência

Veja a descrição completa do desafio em: [DIO - Otimizando o Sistema Bancário com Funções Python](https://web.dio.me/project/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba)

---

Desenvolvido para o Santander Bootcamp 2025.

##
##
<h1>
    <a href="https://www.dio.me/users/matfis">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> MATHEUS LARA</span>
</h1>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/laramatheus/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mathfis)