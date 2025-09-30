from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class UserBase(SQLModel):
    """Campos base compartilhados"""
    email: str = Field(index=True, unique=True)
    nome: str

class User(UserBase, table=True):
    """Modelo de tabela do banco de dados"""
    __tablename__ = "users"
    
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)

class UserCreate(UserBase):
    """Schema para criação de usuário"""
    password: str

class UserRead(UserBase):
    """Schema para leitura de usuário (resposta da API)"""
    id: uuid.UUID
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

class UserUpdate(SQLModel):
    """Schema para atualização de usuário"""
    email: Optional[str] = None
    nome: Optional[str] = None
    password: Optional[str] = None

class UserLogin(SQLModel):
    """Schema para login"""
    email: str
    password: str

class Token(SQLModel):
    """Schema para token de acesso"""
    access_token: str
    token_type: str

class TokenData(SQLModel):
    """Schema para dados do token"""
    username: Optional[str] = None