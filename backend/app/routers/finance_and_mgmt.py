from typing import List
from fastapi import APIRouter, Depends, status
from backend.app.schemas.finance_and_mgmt import (
    FinancialSummaryResponse, EmployeeCreate, EmployeeResponse, DashboardSummaryResponse
)
from backend.app.services.finance_service import FinanceService
from backend.app.services.employee_service import EmployeeService
from backend.app.services.dashboard_service import DashboardService
from backend.app.services.auth_service import require_roles, get_current_user_from_token

router = APIRouter(prefix="/api", tags=["Management & Dashboard"])

@router.get("/dashboard/summary", response_model=DashboardSummaryResponse)
def get_dashboard_summary(current_user: dict = Depends(get_current_user_from_token)):
    return DashboardService.get_dashboard_summary()

@router.get("/finance/summary", response_model=FinancialSummaryResponse)
def get_finance_summary(current_user: dict = Depends(require_roles(["ADMIN", "OWNER"]))):
    return FinanceService.get_summary()

@router.get("/finance/transactions")
def list_transactions(current_user: dict = Depends(require_roles(["ADMIN", "OWNER"]))):
    return FinanceService.list_transactions()

@router.get("/employees", response_model=List[EmployeeResponse])
def list_employees(current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER"]))):
    return EmployeeService.list_employees()

@router.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(data: EmployeeCreate, current_user: dict = Depends(require_roles(["ADMIN", "OWNER"]))):
    return EmployeeService.create_employee(data)
