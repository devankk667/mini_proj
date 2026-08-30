from pydantic import BaseModel, Field
from typing import Optional, List
from backend.app.schemas.enums import TransactionType, UserRole

class FinancialTransactionCreate(BaseModel):
    type: TransactionType
    category: str
    amount: float = Field(gt=0)
    description: str
    reference_id: Optional[str] = None

class FinancialSummaryResponse(BaseModel):
    total_revenue: float
    total_expenses: float
    gross_profit: float
    net_profit: float
    profit_margin_percent: float
    total_receivables: float
    total_payables: float

class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: UserRole
    department: str
    salary: float = Field(gt=0)

class EmployeeResponse(BaseModel):
    id: str
    name: str
    role: UserRole
    department: str
    salary: float
    is_active: bool

class DashboardSummaryResponse(BaseModel):
    todays_sales: float
    monthly_revenue: float
    monthly_expenses: float
    gross_profit: float
    profit_margin: float
    total_products: int
    low_stock_count: int
    top_products: List[dict]
    top_customers: List[dict]
