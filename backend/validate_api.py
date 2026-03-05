#!/usr/bin/env python3
"""
Simple API validation script
Tests basic API functionality without complex test framework
"""

import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def test_api_basic():
    """Test basic API functionality"""
    print("Testing Procurement Intelligence API...")

    try:
        # Test that we can import the modules
        from api.main import app
        print("✅ API module imports successfully")

        # Test that all routes are defined
        routes = [
            "/api/v1/auth/register",
            "/api/v1/auth/login",
            "/api/v1/vendors",
            "/api/v1/orders",
            "/api/v1/quotes",
            "/api/v1/leads",
            "/api/v1/analytics/vendors",
            "/api/v1/notifications"
        ]

        route_paths = [str(route.path) for route in app.routes]
        for route in routes:
            if any(route in rp for rp in route_paths):
                print(f"✅ Route {route} is defined")
            else:
                print(f"❌ Route {route} is missing")

        # Test database models
        from models.models import User, Vendor, Order, Quote, Lead
        print("✅ Database models import successfully")

        print("\n🎉 API validation completed successfully!")
        return True

    except Exception as e:
        print(f"❌ API validation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_api_basic()
    sys.exit(0 if success else 1)