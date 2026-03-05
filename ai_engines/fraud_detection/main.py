#!/usr/bin/env python3
"""
Fraud Detection Engine
Evaluates vendors for potential fraud based on various signals
"""

import re
from sqlalchemy.orm import sessionmaker
from ..backend.models.database import engine
from ..backend.models.models import Vendor

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def check_gst_verification(gst_number):
    """Check if GST number format is valid"""
    if not gst_number:
        return False
    # Basic GST format check (22AAAAA0000A1Z5)
    pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}[A-Z\d]{1}$'
    return bool(re.match(pattern, gst_number))

def check_website_presence(website):
    """Check if website is accessible"""
    if not website:
        return False
    try:
        response = requests.head(website, timeout=5)
        return response.status_code == 200
    except:
        return False

def check_domain_email(email, website):
    """Check if email domain matches website"""
    if not email or not website:
        return False
    try:
        email_domain = email.split('@')[1]
        website_domain = website.replace('www.', '').split('/')[0]
        return email_domain == website_domain
    except:
        return False

def calculate_fraud_score(vendor):
    """Calculate fraud score based on signals"""
    score = 0.0

    # GST verification (weight: 0.3)
    if check_gst_verification(vendor.gst_number):
        score += 0.3
    else:
        score += 0.1  # Partial credit for having GST

    # Website presence (weight: 0.2)
    if check_website_presence(vendor.website):
        score += 0.2

    # Domain email match (weight: 0.2)
    if check_domain_email(vendor.email, vendor.website):
        score += 0.2

    # Phone number presence (weight: 0.1)
    if vendor.phone:
        score += 0.1

    # Location specificity (weight: 0.1)
    if vendor.city and vendor.area:
        score += 0.1

    # Brand specificity (weight: 0.1)
    if vendor.brands and len(vendor.brands) > 0:
        score += 0.1

    return min(score, 1.0)  # Cap at 1.0

def update_fraud_scores():
    """Update fraud scores for all vendors"""
    db = SessionLocal()
    try:
        vendors = db.query(Vendor).all()
        for vendor in vendors:
            fraud_score = calculate_fraud_score(vendor)
            vendor.fraud_score = fraud_score
            print(f"Updated {vendor.name}: fraud_score = {fraud_score}")

        db.commit()
        print(f"Updated fraud scores for {len(vendors)} vendors")
    except Exception as e:
        print(f"Error updating fraud scores: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    print("Running fraud detection engine...")
    update_fraud_scores()
    print("Fraud detection completed.")

if __name__ == "__main__":
    main()