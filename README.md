# README - Banco Digital API

Este repositório contém uma API simples de um Banco Digital, desenvolvida em Python 3.10. Siga os passos abaixo para configurar e executar a aplicação.

## Pré-requisitos

Certifique-se de ter o Python 3.6 ou superior instalado. Recomendamos o uso do Python 3.10.

## Passos para configuração

1. Instale o Python 3.6 ou superior (utilizado 3.10)
2. Clone o repositório
3. Instale um ambiente virtual (opcional, mas recomendado)
4. Instale as dependências: **pip install -r requirements.txt**
5. Execute a aplicação: **python3 manage.py runserver 8080**
6. Abra o Postman e importe as collections: **As coleções estão no arquivo 'Account.postman_collection.json'. Importe-as para o Postman.**
7. Execute as operações no Postman:
   * POST current-account
   * POST savings-account
   * GET Saldo de conta bancária e Saldo de conta bancária - FAIL
   * POST Extrato bancário e Extrato bancário - FAIL
   * Certifique-se de enviar os parâmetros corretos para o POST do Extrato bancário. Parâmetros necessários para o POST do Extrato bancário:
       * owner_id: 1
       * transfer_type: 'investment' ou 'savings'
   * O POST realiza a soma ou subtração na conta corrente ou poupança. Você pode consultar novamente o saldo em GET Saldo de conta bancária.

**Observação: Alguns detalhes no POST do Extrato bancário estão incompletos. A funcionalidade para pegar somente ocorrências mensais ainda precisa ser implementada.**
   
     





