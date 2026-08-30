import uuid
from datetime import datetime
from typing import List, Optional
from backend.app.repositories.in_memory import db
from backend.app.schemas.business import CustomerCreate, CustomerUpdate
from backend.app.exceptions import AppException

class CustomerService:
    @classmethod
    def list_customers(cls, search: Optional[str] = None) -> List[dict]:
        custs = [c for c in db.customers if c.get("is_active", True)]
        if search:
            s = search.lower()
            custs = [c for c in custs if s in c["name"].lower() or (c.get("email") and s in c["email"].lower())]
        return custs

    @classmethod
    def get_customer(cls, customer_id: str) -> dict:
        c = next((cust for cust in db.customers if cust["id"] == customer_id and cust.get("is_active", True)), None)
        if not c:
            raise AppException("Customer not found", status_code=404, code="CUSTOMER_NOT_FOUND")
        return c

    @classmethod
    def create_customer(cls, data: CustomerCreate) -> dict:
        customer = {
            "id": f"cust-{uuid.uuid4().hex[:6]}",
            "name": data.name,
            "email": str(data.email) if data.email else None,
            "phone": data.phone,
            "total_spent": 0.0,
            "is_active": True
        }
        db.customers.append(customer)
        return customer

    @classmethod
    def update_customer(cls, customer_id: str, data: CustomerUpdate) -> dict:
        c = cls.get_customer(customer_id)
        if data.name is not None:
            c["name"] = data.name
        if data.email is not None:
            c["email"] = str(data.email)
        if data.phone is not None:
            c["phone"] = data.phone
        return c
