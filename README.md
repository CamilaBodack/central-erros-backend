# API Centralizadora de Erros

Projeto final da Aceleração de Python

# Objeto

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.

A arquitetura do projeto é formada por:

## Backend

- Criar endpoints para serem usados pelo frontend da aplicação;
- Criar um endpoint que será usado para gravar os logs de erro em um banco de dados relacional;
- A API deve ser segura, permitindo acesso apenas com um token de autenticação válido;

## Frontend

- Deve implementar as funcionalidades apresentadas nos wireframes
- Deve ser acessada adequadamente tanto por navegadores desktop quanto mobile
- Deve consumir a API do produto
- Desenvolvida na forma de uma Single Page Application

## Observações

- Se a aceleração tiver ênfase no backend (Java, Python, C#, Go, PHP, etc) a equipe deve obrigatoriamente    implementar a API. A implementação do frontend não é necessária
- Se a aceleração tiver ênfase em frontend (React, Vue, Angular, etc) a equipe deve obrigatoriamente        implementar o frontend da aplicação e o backend pode ser substituido por uma aplicação mock. A implementação da API não é necessária, caso o time deseje podem ser utilizados mocks.

## Wireframes

Os wireframes servem para ilustrar as funcionalidades básicas que a aplicação deverá ter, porém o time terá total liberdade para definir os detalhes de implementação e estratégia a ser utilizada no desenvolvimento.

**São fornecidos modelos de wireframes no documento de referência.**


## Execução do projeto

- Docker no linux

Abrir o terminal na raiz do projeto e executar:

```
docker-compose build
docker-compose run web python manage.py createsuperuser
docker-compose up

```


- Ficará disponível em localhost:8000/admin
- Logar com o usuário criado
- Documentação:
- Swagger: http://127.0.0.1:8000/doc
- Redoc: http://127.0.0.1:8000/redoc


## Demo da aplicação:

-  Demo disponível em:

https://obscure-sands-75237.herokuapp.com/

**OBS**
- A interface do django não renderiza corretamente após o deploy no Heroku,
o que prejudicou a visualização da documentação e interface de admin, desta forma,
irei verificar o que causou esse conflito, farei a correção e novo deploy

- Usuário para testes: u32048/senha: 12345678
