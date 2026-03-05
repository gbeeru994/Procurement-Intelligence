from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.database import get_db
from models.models import Vendor, Order, Quote, Lead
from routes.auth import get_current_user

router = APIRouter()

@router.get("/vendors")
def get_vendor_analytics(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total_vendors = db.query(func.count(Vendor.id)).scalar()
    verified_vendors = db.query(func.count(Vendor.id)).filter(Vendor.verification_status == True).scalar()
    avg_fraud_score = db.query(func.avg(Vendor.fraud_score)).scalar()
    return {
        "total_vendors": total_vendors,
        "verified_vendors": verified_vendors,
        "avg_fraud_score": float(avg_fraud_score) if avg_fraud_score else 0.0
    }

@router.get("/deals")
def get_deal_analytics(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total_orders = db.query(func.count(Order.id)).scalar()
    open_orders = db.query(func.count(Order.id)).filter(Order.status == "open").scalar()
    closed_deals = db.query(func.count(Order.id)).filter(Order.status == "deal_closed").scalar()
    return {
        "total_orders": total_orders,
        "open_orders": open_orders,
        "closed_deals": closed_deals
    }

@router.get("/prices")
def get_price_analytics(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Basic price analytics - in real implementation, would be more complex
    avg_quote_price = db.query(func.avg(Quote.quoted_price)).scalar()
    return {
        "avg_quote_price": float(avg_quote_price) if avg_quote_price else 0.0
    }

@router.get("/leads")
def get_lead_analytics(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total_leads = db.query(func.count(Lead.id)).scalar()
    new_leads = db.query(func.count(Lead.id)).filter(Lead.status == "new").scalar()
    converted_leads = db.query(func.count(Lead.id)).filter(Lead.status == "converted").scalar()
    return {
        "total_leads": total_leads,
        "new_leads": new_leads,
        "converted_leads": converted_leads
    }