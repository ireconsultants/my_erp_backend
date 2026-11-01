# my_erp_backend

A professional Python backend architecture designed for modern ERP (Enterprise Resource Planning) and accounting applications.

## 🏗️ Architecture
This project is built using modern Python tools for scalability, safety, and speed:
- **Package Manager:** `uv` (Extreme fast Python package manager)
- **Database ORM:** SQLAlchemy
- **Testing:** Pytest (100% unit test coverage for accounting logic)
- **Validation:** (Upcoming) Pydantic / FastAPI

## 📂 Project Structure
- `models.py`: Database schema definitions (SQLAlchemy).
- `accounting.py`: Core financial math and VAT logic.
- `test_accounting.py`: Unit tests to ensure accounting logic is bulletproof.
- `create_account.py`: Example script to interact with the database.

## 🚀 How to run
1. Install dependencies:
   ```bash
   uv sync
