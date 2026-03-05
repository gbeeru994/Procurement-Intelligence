from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from models.database import get_db
from models.models import Quote
from routes.auth import get_current_user

router = APIRouter()

class QuoteCreate(BaseModel):
    vendor_id: int
    order_id: int
    quoted_price: float
    quantity_available: Optional[int] = None
    delivery_time: Optional[int] = None

class QuoteResponse(BaseModel):
    id: int
    vendor_id: int
    order_id: int
    quoted_price: float
    quantity_available: Optional[int]
    delivery_time: Optional[int]

@router.post("/", response_model=QuoteResponse)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_quote = Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

@router.get("/", response_model=List[QuoteResponse])
def read_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quotes = db.query(Quote).offset(skip).limit(limit).all()
    return quotes

@router.put("/{quote_id}", response_model=QuoteResponse)
def update_quote(quote_id: int, quote_update: QuoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    for key, value in quote_update.dict(exclude_unset=True).items():
        setattr(quote, key, value)
    db.commit()
    db.refresh(quote)
    return quote