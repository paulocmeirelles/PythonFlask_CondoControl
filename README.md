# Português

## SOBRE

- Este projeto é sobre alguns endpoints desenvolvido em python usando flask e possui finalidade de mostrar exemplos de como prosseguir com flask.

## REQUISITOS

- python 3.10
- pip instalado

## ENDPOINTS

- Tabela Lotes (
  id: primary key; autoincrement; not null
  nome: varchar(100)
  ativo: boolean; default (true)
  criado_em timestamp; default (current_timestamp)
  )
- get - /lote (pega todos os valores da tabela)
- get - /lote/:id (pega uma linha específica relacionada ao id)
- post - /lote (passando json com o campo nome cria um registro)
- put - /lote (passando json com o id que deseja alterar os campos em questão)
- delete - /lote/:id (deleta o registro que foi passado o id)

- Tabela Boletos (
  id: primary key; autoincrement; not null
  nome_sacado: varchar(255)
  id_lote: int; foreignKey(lote - id)
  valor: numeric(10,2)
  linha_digitavel: varchar(255)
  ativo: boolean; default (true)
  criado_em timestamp; default (current_timestamp)
  )
- get - /boleto (pega todos os valores da tabela)
- get - /boleto/:id (pega uma linha específica relacionada ao id)
- post - /boleto (passando json com o campo nome_sacado, id_lote, valor e linha_digitavel
- cria um registro - Não precisa conter tudo isso, mas é bom criar o registro completo)
- put - /boleto (passando json com o id que deseja alterar os campos em questão)
- delete - /boleto/:id (deleta o registro que foi passado o id)

- Relatorio
  /relatorio - gera relatório em pdf de todos os registros em formato de tabela retornando um json em formato base64.

- Filtros
  /boletos?nome=JOSE&valor_inicial=100&valor_final=200&id_lote=2 - Pode ser alterado os valores dos filtros assim também como deletados. Vai buscar exatamente os campos em questão podendo alterar os valores. (ainda em trabalho)

## Passos

Primeiro, após extrair o projeto do git, execute os comandos abaixo dentro da pasta do projeto.

Crie um arquivo .env e nele coloque as credenciais para a conexão com o banco de dados postgresql. Utilize o arquivo setting.env como base.

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

Para inserir algumas linhas no DB (rode este código somente uma vez)

```
from app.extensions import db
db.create_all()
lotes = [
Lote(name='0011'),
Lote(name='0015'),
Lote(name='0017'),
Lote(name='0012'),
Lote(name='0013'),
Lote(name='0018'),
Lote(name='0019'),
Lote(name='0014')
]

db.session.bulk_save_objects(lotes)
db.session.commit()
```

```
flask run
```

Este projeto contem a coleção dos endpoints no postman para os endpoints.

### P.S.

Os arquivos na pasta raiz (lotes.csv e boletos.pdf) são importantes para resolver os exercícios.

# English

## ABOUT

- This project is about some endpoints developed in python using flask. The reason to this project is to show examples of "how to proceed with flask" in backend.

## REQUISITES

- python 3.10
- pip installed

## ENDPOINTS

- Table Lotes (
  id: primary key; autoincrement; not null
  nome: varchar(100)
  ativo: boolean; default (true)
  criado_em timestamp; default (current_timestamp)
  )
- get - /lote (get all values from the table)
- get - /lote/:id (get a specific value from the table)
- post - /lote (if you send a json with nome field it creates a row)
- put - /lote (if you send a json with id it changes the fields that you send with json)
- delete - /lote/:id (delete the row that belongs to id)

- Table Boletos (
  id: primary key; autoincrement; not null
  nome_sacado: varchar(255)
  id_lote: int; foreignKey(lote - id)
  valor: numeric(10,2)
  linha_digitavel: varchar(255)
  ativo: boolean; default (true)
  criado_em timestamp; default (current_timestamp)
  )

- get - /boleto (get all values from the table)
- get - /boleto/:id (get a specific value from the table)
- post - /boleto (if you send a json with nome_sacado, id_lote, valor e linha_digitavel field it creates a row - don't need to contain all these fields, but it's good to create it complete)
- put - /boleto (if you send a json with id it changes the fields that you send with json)
- delete - /boleto/:id (delete the row that belongs to id)

- Report
  /relatorio - generate a report in pdf with all rows in tabular format returning a json in base64 format.

- Filters
  /boletos?nome=JOSE&valor_inicial=100&valor_final=200&id_lote=2 - You can change the values from the filters (only these filters) or take it out. It'll search exactly the fields that you choose. (developing)

## How to setup

First, after extract the project from git, run the commands below inside of the folder.

Make a .env file and inside of it put all credentials to connect to postgresql database. Take setting.env as an example.

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

To insert few rows into DB (run this one time just to fill the rows)

```
from app.extensions import db
db.create_all()
lotes = [
Lote(name='0011'),
Lote(name='0015'),
Lote(name='0017'),
Lote(name='0012'),
Lote(name='0013'),
Lote(name='0018'),
Lote(name='0019'),
Lote(name='0014')
]

db.session.bulk_save_objects(lotes)
db.session.commit()
```

```
flask run
```

This project contains a collection in postman to endpoints.

### P.S.

The files in the root directory (lotes.csv and boletos.pdf) are important to resolve the exercises.
