# FastAPI + SQLModel + PostgreSQL Backend

Este é um projeto backend usando FastAPI com SQLModel (ORM moderno) e PostgreSQL.

## Estrutura do Projeto

```
fastapi_sqlmodel_backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── credits.py
│   │       ├── antifraud.py
│   │       └── investments.py
│   │
│   └── core/
│       ├── __init__.py
│       └── security.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .env
├── .gitignore
└── README.md
```

## Como Executar

### Opção 1: Com Docker Compose (Recomendado)

1. Clone o repositório
2. Configure as variáveis no arquivo `.env` se necessário
3. Execute:
```bash
docker-compose up --build
```

### Opção 2: Desenvolvimento Local

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Certifique-se de que o PostgreSQL está rodando
4. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```

## Acessar a API

- **API Base**: http://localhost:8000
- **Documentação Interativa (Swagger)**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Endpoints de usuário

- `POST /api/users/register` - Registrar usuário
- `POST /api/users/login` - Login
- `GET /api/users/me` - Perfil do usuário autenticado
- `PUT /api/users/me` - Atualizar perfil

## Endpoints acessíveis para os tomadores de crédito

- `POST /api/credits/request` - Tomador solicita crédito
- 
- `GET /api/credits/list` - Lista propostas de crédito abertas do tomador
- `GET /api/credits/status/{id}` - Detalhes de uma proposta específica

## Endpoints acessíveis para os investidores

- `POST /api/investments/offer` - Investidor oferece investimento na proposta
- `GET /api/investments/offers` - Investidor acessa a lista de ofertas em aberto
- `GET /api/investments/status/{id}` - Investidor verifica detalhes da oferta 

## Endpoints de antifraude

- `POST /api/antifraud/check` - Valida informações detalhadas do usuário
- `POST /api/antifraud/blockchain/register` - Simulação de Hash de transação


## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno para Python
- **SQLModel**: ORM moderno que unifica SQLAlchemy + Pydantic
- **PostgreSQL**: Banco de dados relacional
- **Docker**: Containerização
- **JWT**: Autenticação baseada em tokens
- **bcrypt**: Hash seguro de senhas

## Recursos Implementados

✅ Conexão com PostgreSQL via SQLModel  
✅ Autenticação JWT  
✅ Hash de senhas com bcrypt  
✅ Validação de dados com Pydantic/SQLModel  
✅ CORS configurado para frontend  
✅ Documentação automática (Swagger/OpenAPI)  
✅ Estrutura modular e escalável  
✅ Tratamento de erros  
✅ Docker e Docker Compose  
✅ Health checks