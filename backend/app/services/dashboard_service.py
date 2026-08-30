from backend.app.repositories.in_memory import db
from backend.app.services.finance_service import FinanceService
from backend.app.services.inventory_service import InventoryService
from backend.app.schemas.finance_and_mgmt import DashboardSummaryResponse

class DashboardService:
    @classmethod
    def get_dashboard_summary(cls) -> DashboardSummaryResponse:
        fin = FinanceService.get_summary()
        products = InventoryService.list_products()
        low_stock_count = sum(1 for p in products if p["stock_status"] in ["LOW_STOCK", "OUT_OF_STOCK"])

        top_prods = [
            {"id": p["id"], "name": p["name"], "stock_quantity": p["stock_quantity"]}
            for p in sorted(products, key=lambda x: x["stock_quantity"])[:5]
        ]

        top_custs = [
            {"id": c["id"], "name": c["name"], "total_spent": c["total_spent"]}
            for c in sorted(db.customers, key=lambda x: x["total_spent"], reverse=True)[:5]
        ]

        today_sales = sum(s["total"] for s in db.sales if s["status"] == "COMPLETED")

        return DashboardSummaryResponse(
            todays_sales=round(today_sales, 2),
            monthly_revenue=fin.total_revenue,
            monthly_expenses=fin.total_expenses,
            gross_profit=fin.gross_profit,
            profit_margin=fin.profit_margin_percent,
            total_products=len(products),
            low_stock_count=low_stock_count,
            top_products=top_prods,
            top_customers=top_custs
        )
