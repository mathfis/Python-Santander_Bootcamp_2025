# Roteiro de Testagem do Sistema Bancário v2

Este roteiro orienta o testador a verificar todas as funcionalidades do sistema bancário, mesmo sem conhecimento prévio do código. Siga cada passo, observando as mensagens e resultados esperados.

---

## 1. Iniciar o Sistema

- Execute o arquivo principal de testes (`teste_sistema_bancario_v2.py`).
- O menu inicial será exibido.

---

## 2. Testar como GERENTE

### 2.1. Criar Usuário

1. No menu inicial, digite `g` para acessar como gerente.
2. No menu gerente, escolha a opção `1` para criar usuário.
3. Informe:
   - CPF: `12345678900`
   - Nome: `Maria Silva`
   - Data de nascimento: `01/01/1990`
   - Endereço: `Rua A, 123 - Centro - Cidade/UF`
4. Quando perguntado se deseja criar conta, digite: `n`
4. Verifique a mensagem de sucesso.

### 2.2. Criar Conta

1. Escolha a opção `2` no menu gerente.
2. Informe o CPF do usuário criado (`12345678900`).
3. Informe:
   - Agência: pressione Enter para usar o padrão ou digite `001`
   - Saldo inicial: `0`
   - Limite: `500`
   - Limite de saques: `3`
4. Verifique a mensagem de sucesso.

### 2.3. Listar Contas de Usuário

1. Escolha a opção `3`.
2. Informe o CPF do usuário.
3. Verifique se a conta criada aparece listada.

### 2.4. Depositar em Conta

1. Escolha a opção `4`.
2. Informe o CPF e o número da conta (`1`).
3. Informe o valor do depósito, por exemplo, `200`.
4. Verifique a mensagem de sucesso.

### 2.5. Sacar de Conta

1. Escolha a opção `5`.
2. Informe o CPF e o número da conta (`1`).
3. Informe o valor do saque, por exemplo, `100`.
4. Verifique a mensagem de sucesso.

### 2.6. Extrato de Conta

1. Escolha a opção `6`.
2. Informe o CPF e o número da conta (`1`).
3. Verifique se o extrato mostra o depósito e o saque realizados.

### 2.7. Voltar ao Menu Inicial

1. Escolha a opção `0`.

---

## 3. Testar como CORRENTISTA

### 3.1. Acessar como correntista

1. No menu inicial, digite `c`.
2. Informe o CPF do usuário criado (`12345678900`).

### 3.2. Depositar em Conta

1. Escolha a opção `1`.
2. Informe o número da conta (`1`).
3. Informe o valor do depósito, por exemplo, `50`.
4. Verifique a mensagem de sucesso.

### 3.3. Sacar de Conta

1. Escolha a opção `2`.
2. Informe o número da conta (`1`).
3. Informe o valor do saque, por exemplo, `20`.
4. Verifique a mensagem de sucesso.

### 3.4. Ver Extrato

1. Escolha a opção `3`.
2. Informe o número da conta (`1`).
3. Verifique se o extrato mostra as operações realizadas.

### 3.5. Listar Minhas Contas

1. Escolha a opção `4`.
2. Verifique se a conta aparece listada.

### 3.6. Voltar ao Menu Inicial

1. Escolha a opção `0`.

---

## 4. Sair do Sistema

1. No menu inicial, digite `q`.

---

## 5. Testes de Restrições

- Tente criar conta para um CPF inexistente (deve mostrar erro).
- Tente sacar valor maior que o saldo ou limite (deve mostrar erro).
- Tente exceder o número de saques permitidos (deve mostrar erro).
- Tente acessar como correntista com CPF não cadastrado (deve mostrar erro).

---

## 6. Observações

- Sempre confira se as mensagens exibidas correspondem ao esperado.
- Anote qualquer comportamento inesperado ou erro para relatar ao desenvolvedor.

---

**Fim do roteiro de testagem**