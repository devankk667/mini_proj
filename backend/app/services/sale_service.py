import uuid
from datetime import datetime
from typing import List, Optional
from backend.app.repositories.in_memory import db
from backend.app.schemas.business import SaleCreate
from backend.app.schemas.enums import StockMovementType, TransactionType
from backend.app.services.inventory_service import InventoryService
from backend.app.services.customer_service import CustomerService
from backend.app.schemas.inventory import StockAdjustmentRequest
from backend.app.exceptions import AppException

class SaleService:
    @classmethod
    def list_sales(cls) -> List[dict]:
        return db.sales

    @classmethod
    def get_sale(cls, sale_id: str) -> dict:
        s = next((sale for sale in db.sales if sale["id"] == sale_id), None)
        if not s:
            raise AppException("Sale not found", status_code=404, code="SALE_NOT_FOUND")
        return s

    @classmethod
    def create_sale(cls, data: SaleCreate) -> dict:
        if not data.items:
            raise AppException("Sale must contain at least one item", status_code=400, code="EMPTY_ITEMS")

        customer = None
        if data.customer_id:
            customer = CustomerService.get_customer(data.customer_id)

        for item in data.items:
            prod = InventoryService.get_product(item.product_id)
            if prod["stock_quantity"] < item.quantity:
                raise AppException(
                    f"Insufficient stock for product '{prod['name']}'. Available: {prod['stock_quantity']}, Requested: {item.quantity}",
                    status_code=400,
                    code="INSUFFICIENT_STOCK",
                    field="quantity"
                )

        processed_items = []
        subtotal = 0.0

        for item in data.items:
            prod = InventoryService.get_product(item.product_id)
            unit_price = item.unit_price if item.unit_price is not None else prod["selling_price"]
            item_subtotal = round(unit_price * item.quantity, 2)
            subtotal += item_subtotal

            processed_items.append({
                "product_id": prod["id"],
                "product_name": prod["name"],
                "quantity": item.quantity,
                "unit_price": unit_price,
                "subtotal": item_subtotal
            })

        tax = round(subtotal * (data.tax_rate / 100.0), 2)
        total = round(subtotal + tax - data.discount, 2)

        sale = {
            "id": f"sale-{uuid.uuid4().hex[:6]}",
            "customer_id": customer["id"] if customer else None,
            "customer_name": customer["name"] if customer else "Guest Customer",
            "items": processed_items,
            "subtotal": subtotal,
            "tax": tax,
            "discount": data.discount,
            "total": max(0.0, total),
            "status": "COMPLETED",
            "created_at": datetime.utcnow().isoformat()
        }
        db.sales.append(sale)

        for item in processed_items:
            InventoryService.adjust_stock(
                item["product_id"],
                StockAdjustmentRequest(
                    quantity_change=-item["quantity"],
                    type=StockMovementType.SALE,
                    reason=f"Sale receipt {sale['id']}"
                )
            )

        db.financial_transactions.append({
            "id": f"txn-{uuid.uuid4().hex[:6]}",
            "type": TransactionType.INCOME.value,
            "category": "SALES",
            "amount": sale["total"],
            "reference_id": sale["id"],
            "description": f"Sale to {sale['customer_name']}",
            "created_at": sale["created_at"]
        })

        if customer:
            customer["total_spent"] = round(customer.get("total_spent", 0.0) + sale["total"], 2)

        return sale

    @classmethod
    def cancel_sale(cls, sale_id: str) -> dict:
        s = cls.get_sale(sale_id)
        if s["status"] == "CANCELLED":
            raise AppException("Sale is already cancelled", status_code=400, code="ALREADY_CANCELLED")

        s["status"] = "CANCELLED"
        for item in s["items"]:
            InventoryService.adjust_stock(
                item["product_id"],
                StockAdjustmentRequest(
                    quantity_change=item["quantity"],
                    type=StockMovementType.RETURN,
                    reason=f"Cancelled sale receipt {s['id']}"
                )
            )

        if s.get("customer_id"):
            c = next((cust for cust in db.customers if cust["id"] == s["customer_id"]), None)
            if c:
                c["total_spent"] = max(0.0, round(c.get("total_spent", 0.0) - s["total"], 2))

        return s
