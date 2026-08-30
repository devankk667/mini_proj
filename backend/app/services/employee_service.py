from typing import List
from backend.app.repositories.in_memory import db
from backend.app.schemas.finance_and_mgmt import EmployeeCreate
from backend.app.exceptions import AppException
import uuid

class EmployeeService:
    @classmethod
    def list_employees(cls) -> List[dict]:
        return [e for e in db.employees if e.get("is_active", True)]

    @classmethod
    def create_employee(cls, data: EmployeeCreate) -> dict:
        emp = {
            "id": f"emp-{uuid.uuid4().hex[:6]}",
            "name": data.name,
            "role": data.role.value if hasattr(data.role, 'value') else str(data.role),
            "department": data.department,
            "salary": data.salary,
            "is_active": True
        }
        db.employees.append(emp)
        return emp
