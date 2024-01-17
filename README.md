# condo_conta_api

Este repositório contém uma API simples de um Banco Digital, desenvolvida em Python 3.10. Siga os passos abaixo para configurar e executar a aplicação.

Pré-requisitos
Certifique-se de ter o Python 3.6 ou superior instalado. Recomendamos o uso do Python 3.10.

Passos para configuração
Clone o repositório:

bash
Copy code
git clone https://github.com/seu-usuario/banco-digital-api.git
cd banco-digital-api
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute a aplicação:

bash
Copy code
python3 manage.py runserver 8080
Importe as collections no Postman:

As coleções estão na pasta 'collections'. Importe-as para o Postman.
Execute as operações no Postman:

Rode as operações na seguinte ordem:
POST current-account
POST savings-account
GET Saldo de conta bancária e Saldo de conta bancária - FAIL
POST Extrato bancário e Extrato bancário - FAIL
Certifique-se de enviar os parâmetros corretos para o POST do Extrato bancário.
Parâmetros necessários para o POST do Extrato bancário:

owner_id: 1

transfer_type: 'investment' ou 'savings'

O POST realiza a soma ou subtração na conta corrente ou poupança. Você pode consultar novamente o saldo em GET Saldo de conta bancária.

Observação: Alguns detalhes no POST do Extrato bancário estão incompletos. A funcionalidade para pegar somente ocorrências mensais ainda precisa ser implementada.
