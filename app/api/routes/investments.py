from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ...database import get_session
from ..deps import get_current_active_user
from ...config import settings


router = APIRouter()

@router.post("/offer")
def offer_investment():
    """Oferecer investimento"""
    return {"message": "Investimento oferecido com sucesso!"}

@router.get("/offers")
def list_investments():
    """Listar ofertas de investimento disponíveis"""
    return [
        {"id": 1, "amount": 5000, "currency": "BRL", "status": "Aberto"},
        {"id": 2, "amount": 10000, "currency": "BRL", "status": "Em análise"},
    ]

@router.get("/status/{id}")
def investment_details(id: int):
    """Detalhes de uma oferta específica"""
    if id == 1:
        return {"id": 1, "amount": 5000, "currency": "BRL", "status": "Aberto", "details": "Oferta em análise"}
    elif id == 2:
        return {"id": 2, "amount": 10000, "currency": "BRL", "status": "Em análise", "details": "Oferta em análise"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Oferta não encontrada")

