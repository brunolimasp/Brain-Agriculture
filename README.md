# Teste - Brain-Agriculture


Este projeto é uma aplicação desenvolvida em FastAPI + SQLModel para gerenciar o cadastro de produtores rurais, suas propriedades e safras. Foi criado como parte de um desafio técnico da Brain Agriculture, com foco em boas práticas de desenvolvimento, organização do código e confiabilidade na manipulação de dados.


## Instruções e Requisitos


- Certifique-se de ter o Docker instalado em seu ambiente. Se ainda não o tiver, você pode baixá-lo e instalá-lo a partir do site oficial: Docker.

- Após instalar o Docker, abra um terminal ou prompt de comando.

- Navegue até o diretório raiz do projeto onde está localizado o arquivo docker-compose.yml.

- Execute o seguinte comando:


```cmd
docker-compose up -d
```

- Aguarde até que o Docker baixe as imagens, construa os contêineres e inicie o serviço.

- Uma vez que o serviço esteja em execução, você poderá acessar a documentação das API´s pelo Swagger ou Redoc através das rotas: http://127.0.0.1:8000/redoc  ou http://127.0.0.1:8000/docs

- As credenciais para acesso ao banco estão no arquivo `.env`

## Tecnologias Utilizadas

- **Python 3.12+**  
- **FastAPI**  
- **SQLModel** (ORM baseado em SQLAlchemy + Pydantic)  
- **Uvicorn**  
- **pytest** (para testes)  
- **validate-docbr** (validação de CPF/CNPJ)  

## Visão Geral

Descreva em poucas linhas o objetivo do projeto, por que foi criado e quais problemas resolve.

> *Exemplo*: *Este desafio foi proposto pela Brain Agriculture para avaliar habilidades em **FastAPI** e **SQLModel**, cobrindo CRUDs, validações de dados e testes de unidade.*

---

## Recursos

### Cadastro de produtores
- Suporte a CPF e/ou CNPJ, com validações de documentos (opcionais).
- Permite criar, listar e realizar **soft delete** de produtores.

### Cadastro de propriedades rurais
- Informa **área total**, **área agricultável** e **área de vegetação**.
- Garante que a soma das áreas agricultável e de vegetação não exceda a área total da fazenda.

### Cadastro de culturas (safras)
- Relaciona culturas específicas (Soja, Milho etc.) a cada propriedade.

### Validações
- Regra de “somente um documento” (opcional): CPF ou CNPJ, mas não ambos.
- Validação real de CPF/CNPJ via biblioteca `validate_docbr`.
- Áreas de vegetação e cultivo não podem exceder a área total.

### Testes
- Inclui testes unitários e de integração para garantir confiabilidade das rotas e validações.


Testes
Para executar todos os testes:

```cmd
pytest tests/
```
- Testes Unitários: Validam regras de negócio e lógica de validação em nível de função/classe.
