from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    database_url: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # API
    api_v1_str: str = "/api/v1"
    project_name: str = "FastAPI Lio Backend"

    # Evolution
    EVOLUTION_API_KEY: Optional[str] = None
    EVOLUTION_API_URL: Optional[str] = None

    # Debug
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()