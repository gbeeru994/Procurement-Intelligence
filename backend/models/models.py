from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, DECIMAL, ARRAY, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default="operator")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    city = Column(String(100))
    area = Column(String(100))
    category = Column(String(100))
    brands = Column(ARRAY(String))  # Array of brands
    product_condition = Column(String(50))  # new, used, both
    email = Column(String(255))
    phone = Column(String(20))
    website = Column(String(255))
    gst_number = Column(String(50))
    verification_status = Column(Boolean, default=False)
    fraud_score = Column(DECIMAL(3,2), default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    brand = Column(String(100))
    category = Column(String(100))
    quantity = Column(Integer, nullable=False)
    target_price = Column(DECIMAL(10,2))
    condition = Column(String(50))
    location = Column(String(255))
    deadline = Column(Date)
    status = Column(String(50), default="open")
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    quoted_price = Column(DECIMAL(10,2), nullable=False)
    quantity_available = Column(Integer)
    delivery_time = Column(Integer)  # days
    created_at = Column(DateTime, default=datetime.utcnow)

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False)
    contact_person = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    interest_category = Column(String(100))
    source = Column(String(100))
    status = Column(String(50), default="new")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255))
    brand = Column(String(100))
    category = Column(String(100))
    price = Column(DECIMAL(10,2))
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    recorded_at = Column(DateTime, default=datetime.utcnow)