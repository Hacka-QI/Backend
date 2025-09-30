from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ...database import get_session
from ..deps import get_current_active_user
from ...config import settings


router = APIRouter()

@router.post("/request")
def request_credit():
    """Solicitar crédito"""
    return {"message": "Crédito solicitado com sucesso!"}

@router.get("/list")
def list_credits():
    """Listar propostas de crédito abertas do tomador"""
    return [
        {"id": 1, "amount": 1000, "currency": "BRL", "status": "Aberto"},
        {"id": 2, "amount": 2000, "currency": "BRL", "status": "Em análise"},
    ]

@router.get("/status/{id}")
def credit_details(id: int):
    """Detalhes de uma proposta específica"""
    if id == 1:
        return {"id": 1, "amount": 1000, "currency": "BRL", "status": "Aberto", "details": "Proposta em análise"}
    elif id == 2:
        return {"id": 2, "amount": 2000, "currency": "BRL", "status": "Em análise", "details": "Proposta em análise"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proposta não encontrada")