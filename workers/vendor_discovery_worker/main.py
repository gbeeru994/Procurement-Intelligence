#!/usr/bin/env python3
"""
Vendor Discovery Worker
Scrapes vendor data from various sources and stores in database
"""

import time
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from ..backend.models.database import engine, Base
from ..backend.models.models import Vendor

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def scrape_indiamart():
    """Scrape vendors from IndiaMART"""
    # This is a simplified example - in production, use proper scraping libraries
    url = "https://www.indiamart.com/search.mp?ss=network+equipment+mumbai"
    # Note: Actual scraping would require proper headers, rate limiting, etc.
    print("Scraping IndiaMART...")

    # Mock data for demonstration
    vendors = [
        {
            "name": "Tech Solutions Mumbai",
            "city": "Mumbai",
            "area": "Lamington Road",
            "category": "Networking",
            "brands": ["Cisco", "HP"],
            "product_condition": "new",
            "email": "contact@techsolutions.in",
            "phone": "+91-9876543210"
        }
    ]
    return vendors

def scrape_google_maps():
    """Scrape vendors from Google Maps"""
    print("Scraping Google Maps...")
    # Mock data
    vendors = [
        {
            "name": "ServerHub Delhi",
            "city": "Delhi",
            "category": "Servers",
            "brands": ["Dell", "Lenovo"],
            "product_condition": "new"
        }
    ]
    return vendors

def deduplicate_vendors(vendors):
    """Remove duplicate vendors based on name and email"""
    seen = set()
    unique_vendors = []
    for vendor in vendors:
        key = (vendor.get('name'), vendor.get('email'))
        if key not in seen:
            seen.add(key)
            unique_vendors.append(vendor)
    return unique_vendors

def store_vendors(vendors):
    """Store vendors in database"""
    db = SessionLocal()
    try:
        for vendor_data in vendors:
            # Check if vendor already exists
            existing = db.query(Vendor).filter(
                Vendor.name == vendor_data['name'],
                Vendor.email == vendor_data.get('email')
            ).first()

            if not existing:
                vendor = Vendor(**vendor_data)
                db.add(vendor)
                print(f"Added vendor: {vendor.name}")

        db.commit()
    except Exception as e:
        print(f"Error storing vendors: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    print("Starting vendor discovery worker...")

    all_vendors = []

    # Scrape from different sources
    all_vendors.extend(scrape_indiamart())
    all_vendors.extend(scrape_google_maps())

    # Deduplicate
    unique_vendors = deduplicate_vendors(all_vendors)
    print(f"Found {len(unique_vendors)} unique vendors")

    # Store in database
    store_vendors(unique_vendors)

    print("Vendor discovery completed.")

if __name__ == "__main__":
    main()