#!/usr/bin/env python3
"""
Phase 3 Setup Helper
Initializes Phase 3 (Frontend Dashboard) development
"""

import os
import json
import subprocess
from pathlib import Path

def setup_frontend():
    """Setup frontend development environment"""
    print("=" * 80)
    print("PHASE 3: FRONTEND DASHBOARD SETUP")
    print("=" * 80)

    frontend_dir = Path(__file__).parent.parent / "frontend"

    print("\n📁 Checking Frontend Directory...")
    if frontend_dir.exists():
        print(f"✅ Frontend directory exists: {frontend_dir}")
    else:
        print(f"❌ Frontend directory not found: {frontend_dir}")
        return False

    # Check package.json
    package_json = frontend_dir / "package.json"
    if package_json.exists():
        print("✅ package.json found")
    else:
        print("❌ package.json not found")
        return False

    print("\n📦 Frontend Dependencies to Install:")
    with open(package_json, 'r') as f:
        pkg = json.load(f)
        deps = pkg.get("dependencies", {})
        dev_deps = pkg.get("devDependencies", {})

        print("  Production Dependencies:")
        for name, version in deps.items():
            print(f"    • {name}: {version}")

        print("\n  Development Dependencies:")
        for name, version in dev_deps.items():
            print(f"    • {name}: {version}")

    print("\n🔧 To install dependencies, run:")
    print(f"   cd {frontend_dir}")
    print("   npm install")

    print("\n✨ Next Steps:")
    print("1. Install dependencies (npm install)")
    print("2. Create .env.local with API URL")
    print("3. Start development server (npm run dev)")
    print("4. Open http://localhost:3000")

    print("\n📋 Phase 3 Tasks to Complete:")
    tasks = [
        ("auth_ui", "Authentication UI (login/register pages)"),
        ("dashboard_ui", "Main dashboard with metrics"),
        ("vendor_management_ui", "Vendor management interface"),
        ("order_ui", "Order creation interface"),
        ("quote_ui", "Quote comparison interface"),
        ("analytics_ui", "Analytics dashboard"),
        ("responsive_design", "Responsive design implementation"),
    ]

    for task_id, task_name in tasks:
        print(f"   ⏳ {task_name}")

    print("\n💡 Useful Commands:")
    print("   # Check backend status")
    print("   cd ../backend && python validate_api.py")
    print()
    print("   # Track progress")
    print("   cd ../project-management && python progress_tracker.py report")
    print()
    print("   # Start development")
    print("   npm run dev")
    print()
    print("   # Build for production")
    print("   npm run build")

    print("\n" + "=" * 80)
    print("Phase 3 Setup Complete!")
    print("Ready to start frontend development")
    print("=" * 80)

    return True

def check_backend():
    """Verify backend is ready for Phase 3"""
    print("\n🔍 Checking Backend Status...")

    backend_dir = Path(__file__).parent.parent.parent / "backend"

    if not backend_dir.exists():
        print("❌ Backend directory not found")
        return False

    # Check if API can be imported
    try:
        os.chdir(backend_dir)
        result = subprocess.run(
            ["python", "validate_api.py"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print("✅ Backend API is ready for integration")
            print("\n📊 Backend Summary:")
            print("   • API Base URL: http://localhost:8000")
            print("   • API Docs: http://localhost:8000/docs")
            print("   • Total Endpoints: 22")
            return True
        else:
            print("❌ Backend validation failed")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"⚠️  Could not verify backend: {e}")
        return False

def create_env_file():
    """Create .env.local template"""
    frontend_dir = Path(__file__).parent.parent / "frontend"
    env_file = frontend_dir / ".env.local"

    if env_file.exists():
        print("\n⚠️  .env.local already exists")
    else:
        env_content = """# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1

# Optional: Add other environment variables
# NEXT_PUBLIC_APP_NAME=Procurement Intelligence
# NEXT_PUBLIC_APP_VERSION=1.0.0
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ Created .env.local template")

def main():
    """Main setup function"""
    print("\n🚀 Initializing Phase 3: Frontend Dashboard Development\n")

    # Check backend
    backend_ready = check_backend()

    # Setup frontend
    frontend_ready = setup_frontend()

    # Create environment file
    create_env_file()

    print("\n" + "=" * 80)
    if backend_ready and frontend_ready:
        print("✅ ALL SYSTEMS READY FOR PHASE 3!")
        print("\nYou may now start development:")
        print("   cd frontend")
        print("   npm install")
        print("   npm run dev")
    else:
        print("⚠️  Some setup steps need attention")
        print("Please review the errors above")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()