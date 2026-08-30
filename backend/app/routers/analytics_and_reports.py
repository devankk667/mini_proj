from typing import List
from fastapi import APIRouter, Depends
from backend.app.schemas.analytics_and_reports import (
    SalesAnalyticsResponse, InventoryAnalyticsResponse, AlertItem, ReportResponse, ReportFilterRequest
)
from backend.app.services.analytics_and_reports_service import AnalyticsService, AlertEngine, ReportService
from backend.app.services.auth_service import get_current_user_from_token

router = APIRouter(prefix="/api", tags=["Analytics, Alerts & Reports"])

@router.get("/analytics/sales", response_model=SalesAnalyticsResponse)
def get_sales_analytics(current_user: dict = Depends(get_current_user_from_token)):
    return AnalyticsService.get_sales_analytics()

@router.get("/analytics/inventory", response_model=InventoryAnalyticsResponse)
def get_inventory_analytics(current_user: dict = Depends(get_current_user_from_token)):
    return AnalyticsService.get_inventory_analytics()

@router.get("/alerts", response_model=List[AlertItem])
def get_alerts(current_user: dict = Depends(get_current_user_from_token)):
    return AlertEngine.evaluate_alerts()

@router.post("/reports/sales", response_model=ReportResponse)
def generate_sales_report(filter_req: ReportFilterRequest, current_user: dict = Depends(get_current_user_from_token)):
    return ReportService.generate_sales_report(filter_req)
