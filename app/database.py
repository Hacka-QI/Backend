from sqlmodel import create_engine, Session, SQLModel
from .config import settings

# Criar engine do SQLModel/SQLAlchemy
engine = create_engine(settings.database_url, echo=True)

# Função para criar todas as tabelas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency para obter sessão do banco
def get_session():
    with Session(engine) as session:
        yield session