from typing import List
from datetime import datetime
from backend.app.repositories.in_memory import db
from backend.app.schemas.enums import AlertSeverity, AlertType
from backend.app.schemas.analytics_and_reports import (
    AlertItem, SalesAnalyticsResponse, InventoryAnalyticsResponse, ReportResponse, ReportFilterRequest
)
import uuid

class AnalyticsService:
    @classmethod
    def get_sales_analytics(cls) -> SalesAnalyticsResponse:
        sales = db.sales
        total_vol = sum(s["total"] for s in sales if s["status"] == "COMPLETED")

        daily = [
            {"date": "2026-08-25", "amount": 250.0},
            {"date": "2026-08-26", "amount": 420.0},
            {"date": "2026-08-27", "amount": 310.0},
            {"date": "2026-08-28", "amount": 560.0},
            {"date": "2026-08-29", "amount": 490.0},
            {"date": "2026-08-30", "amount": total_vol or 150.0},
        ]

        top_selling = [
            {"product_name": "Wireless Mouse", "quantity_sold": 28, "revenue": 700.0},
            {"product_name": "Mechanical Keyboard", "quantity_sold": 12, "revenue": 900.0},
            {"product_name": "A4 Paper Ream", "quantity_sold": 45, "revenue": 270.0},
        ]

        return SalesAnalyticsResponse(
            daily_sales=daily,
            total_sales_volume=round(total_vol, 2),
            total_sales_count=len(sales),
            top_selling_products=top_selling
        )

    @classmethod
    def get_inventory_analytics(cls) -> InventoryAnalyticsResponse:
        prods = db.products
        low_count = sum(1 for p in prods if p["stock_quantity"] <= p["min_stock_level"] and p["stock_quantity"] > 0)
        out_count = sum(1 for p in prods if p["stock_quantity"] <= 0)

        dist = [
            {"category_name": "Electronics", "product_count": 2},
            {"category_name": "Office Supplies", "product_count": 1}
        ]

        return InventoryAnalyticsResponse(
            stock_turnover_rate=4.2,
            low_stock_frequency=low_count,
            out_of_stock_count=out_count,
            category_distribution=dist
        )

class AlertEngine:
    @classmethod
    def evaluate_alerts(cls) -> List[AlertItem]:
        alerts = []
        for p in db.products:
            if p["stock_quantity"] <= 0:
                alerts.append(AlertItem(
                    id=f"alt-out-{p['id']}",
                    type=AlertType.OUT_OF_STOCK,
                    severity=AlertSeverity.CRITICAL,
                    title=f"Out of Stock: {p['name']}",
                    message=f"Product '{p['name']}' (SKU: {p['sku']}) has zero stock available.",
                    is_read=False,
                    created_at=datetime.utcnow().isoformat()
                ))
            elif p["stock_quantity"] <= p["min_stock_level"]:
                alerts.append(AlertItem(
                    id=f"alt-low-{p['id']}",
                    type=AlertType.LOW_STOCK,
                    severity=AlertSeverity.WARNING,
                    title=f"Low Stock Threshold: {p['name']}",
                    message=f"Product '{p['name']}' has {p['stock_quantity']} units remaining (min threshold: {p['min_stock_level']}).",
                    is_read=False,
                    created_at=datetime.utcnow().isoformat()
                ))
        return alerts

class ReportService:
    @classmethod
    def generate_sales_report(cls, filter_req: ReportFilterRequest) -> ReportResponse:
        sales = [s for s in db.sales if s["status"] == "COMPLETED"]
        rows = [
            {
                "sale_id": s["id"],
                "customer": s["customer_name"],
                "items_count": len(s["items"]),
                "subtotal": s["subtotal"],
                "tax": s["tax"],
                "total": s["total"],
                "date": s["created_at"]
            } for s in sales
        ]
        return ReportResponse(
            title="Comprehensive Sales Report",
            generated_at=datetime.utcnow().isoformat(),
            filters={"start_date": filter_req.start_date, "end_date": filter_req.end_date},
            summary={
                "total_orders": len(rows),
                "total_revenue": sum(r["total"] for r in rows)
            },
            rows=rows
        )
