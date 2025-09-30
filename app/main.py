from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import create_db_and_tables
from .api.routes import users, credits, investments, antifraud

# Criar instância do FastAPI
app = FastAPI(
    title=settings.project_name,
    version="1.0.0",
    description="API Backend com FastAPI e SQLModel + PostgreSQL",
    openapi_url=f"{settings.api_v1_str}/openapi.json"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # URLs do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Evento de startup para criar tabelas
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Incluir rotas
app.include_router(
    users.router,
    prefix=f"{settings.api_v1_str}/users",
    tags=["users"]
)

app.include_router(
    credits.router,
    prefix=f"{settings.api_v1_str}/credits",
    tags=["credits"]
)

app.include_router(
    investments.router,
    prefix=f"{settings.api_v1_str}/investments",
    tags=["investments"]
)

app.include_router(
    antifraud.router,
    prefix=f"{settings.api_v1_str}/antifraud",
    tags=["antifraud"]
)

# Rota de health check
@app.get("/")
def read_root():
    return {
        "message": "API está funcionando!",
        "project": settings.project_name,
        "version": "1.0.0",
        "orm": "SQLModel"
    }

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API está saudável", "orm": "SQLModel"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)