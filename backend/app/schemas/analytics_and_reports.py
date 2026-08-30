from pydantic import BaseModel
from typing import List, Optional
from backend.app.schemas.enums import AlertSeverity, AlertType

class AlertItem(BaseModel):
    id: str
    type: AlertType
    severity: AlertSeverity
    title: str
    message: str
    is_read: bool
    created_at: str

class SalesAnalyticsResponse(BaseModel):
    daily_sales: List[dict]
    total_sales_volume: float
    total_sales_count: int
    top_selling_products: List[dict]

class InventoryAnalyticsResponse(BaseModel):
    stock_turnover_rate: float
    low_stock_frequency: int
    out_of_stock_count: int
    category_distribution: List[dict]

class ReportFilterRequest(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    category_id: Optional[str] = None

class ReportResponse(BaseModel):
    title: str
    generated_at: str
    filters: dict
    summary: dict
    rows: List[dict]
