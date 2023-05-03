# MVP 01 - API - WineStore

Projeto de uma aplicação de venda de vinhos com endpoints que permitem o registro de usuários, listagem de produtos, adição de produtos ao carrinho, exclusão de itens do carrinho e finalização do pedido.

---
## Pre requisitos: 

### 1: Possuir as seguintes depdencencias instaladas:
 + Python 3.10
 + PostgreSQL

### 2: Clonar o reposiório do GitHub
    https://github.com/cvgazeredo/winestore_API

### 3: Criar um banco de dados com o nome
    winestore

## Execução

> todos os comandos devem ser executados dentro do diretório do projeto utilizando o terminal

### 1: Utilizar ambientes virtuais 

> não se aplica para usuários do PyCharm

Execute o seguinte comando:
    
    [virtualenv](https://virtualenpython -m venv .v.pypa.io/en/latest/)

### 2: Instalar dependencias listadas em 'requirements.txt'
    
    pip install -r requirements.txt

### 3: Configurar conexao com o banco de dados

altere o valor das variaveis **username** e **password** definindo as credenciais do banco criado

no arquivo **/model/\_\_init__.py**
    
    url = URL.create(
        drivername="postgresql",
        username="",
        password="",
        host="localhost",
        database="winestore",
        port=5432
    )

Caso a porta do banco de dados criado seja diferente de 5432, defina o valor da sua porta 

### 4: Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API e das rotas.
