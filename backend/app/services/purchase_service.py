import uuid
from datetime import datetime
from typing import List, Optional
from backend.app.repositories.in_memory import db
from backend.app.schemas.business import PurchaseCreate
from backend.app.schemas.enums import StockMovementType, TransactionType
from backend.app.services.inventory_service import InventoryService
from backend.app.exceptions import AppException
from backend.app.schemas.inventory import StockAdjustmentRequest

class PurchaseService:
    @classmethod
    def list_purchases(cls) -> List[dict]:
        return db.purchases

    @classmethod
    def create_purchase(cls, data: PurchaseCreate) -> dict:
        if not data.items:
            raise AppException("Purchase must contain at least one item", status_code=400, code="EMPTY_ITEMS")

        processed_items = []
        subtotal = 0.0

        for item in data.items:
            prod = InventoryService.get_product(item.product_id)
            unit_price = item.unit_price if item.unit_price is not None else prod["cost_price"]
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

        purchase = {
            "id": f"pur-{uuid.uuid4().hex[:6]}",
            "supplier_name": data.supplier_name,
            "items": processed_items,
            "subtotal": subtotal,
            "tax": tax,
            "discount": data.discount,
            "total": max(0.0, total),
            "status": "COMPLETED",
            "created_at": datetime.utcnow().isoformat()
        }
        db.purchases.append(purchase)

        for item in processed_items:
            InventoryService.adjust_stock(
                item["product_id"],
                StockAdjustmentRequest(
                    quantity_change=item["quantity"],
                    type=StockMovementType.PURCHASE,
                    reason=f"Purchase order {purchase['id']}"
                )
            )

        db.financial_transactions.append({
            "id": f"txn-{uuid.uuid4().hex[:6]}",
            "type": TransactionType.EXPENSE.value,
            "category": "PURCHASES",
            "amount": purchase["total"],
            "reference_id": purchase["id"],
            "description": f"Purchase from {data.supplier_name}",
            "created_at": purchase["created_at"]
        })

        return purchase

    @classmethod
    def cancel_purchase(cls, purchase_id: str) -> dict:
        p = next((pur for pur in db.purchases if pur["id"] == purchase_id), None)
        if not p:
            raise AppException("Purchase not found", status_code=404, code="PURCHASE_NOT_FOUND")
        if p["status"] == "CANCELLED":
            raise AppException("Purchase is already cancelled", status_code=400, code="ALREADY_CANCELLED")

        p["status"] = "CANCELLED"
        for item in p["items"]:
            InventoryService.adjust_stock(
                item["product_id"],
                StockAdjustmentRequest(
                    quantity_change=-item["quantity"],
                    type=StockMovementType.ADJUSTMENT,
                    reason=f"Cancelled purchase order {p['id']}"
                )
            )

        return p
