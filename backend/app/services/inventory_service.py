import uuid
from datetime import datetime
from typing import List, Optional
from backend.app.repositories.in_memory import db
from backend.app.schemas.inventory import ProductCreate, ProductUpdate, StockAdjustmentRequest
from backend.app.schemas.enums import StockMovementType
from backend.app.exceptions import AppException

class InventoryService:
    @staticmethod
    def _compute_stock_status(stock_quantity: int, min_stock_level: int) -> str:
        if stock_quantity <= 0:
            return "OUT_OF_STOCK"
        elif stock_quantity <= min_stock_level:
            return "LOW_STOCK"
        return "IN_STOCK"

    @classmethod
    def list_products(cls, search: Optional[str] = None, category_id: Optional[str] = None) -> List[dict]:
        products = [p for p in db.products if p.get("is_active", True)]
        if search:
            s = search.lower()
            products = [p for p in products if s in p["name"].lower() or s in p["sku"].lower()]
        if category_id:
            products = [p for p in products if p["category_id"] == category_id]

        res = []
        for p in products:
            item = p.copy()
            item["stock_status"] = cls._compute_stock_status(p["stock_quantity"], p["min_stock_level"])
            res.append(item)
        return res

    @classmethod
    def get_product(cls, product_id: str) -> dict:
        p = next((prod for prod in db.products if prod["id"] == product_id and prod.get("is_active", True)), None)
        if not p:
            raise AppException("Product not found", status_code=404, code="PRODUCT_NOT_FOUND")
        res = p.copy()
        res["stock_status"] = cls._compute_stock_status(p["stock_quantity"], p["min_stock_level"])
        return res

    @classmethod
    def create_product(cls, data: ProductCreate) -> dict:
        if any(p["sku"].upper() == data.sku.upper() for p in db.products):
            raise AppException(f"Product with SKU '{data.sku}' already exists", status_code=400, code="DUPLICATE_SKU")

        product = {
            "id": f"prod-{uuid.uuid4().hex[:6]}",
            "name": data.name,
            "sku": data.sku.upper(),
            "category_id": data.category_id,
            "cost_price": data.cost_price,
            "selling_price": data.selling_price,
            "stock_quantity": data.stock_quantity,
            "min_stock_level": data.min_stock_level,
            "is_active": True
        }
        db.products.append(product)

        if data.stock_quantity > 0:
            cls.record_movement(product["id"], StockMovementType.ADJUSTMENT, data.stock_quantity, 0, data.stock_quantity, "Initial stock deposit")

        res = product.copy()
        res["stock_status"] = cls._compute_stock_status(product["stock_quantity"], product["min_stock_level"])
        return res

    @classmethod
    def update_product(cls, product_id: str, data: ProductUpdate) -> dict:
        product = next((p for p in db.products if p["id"] == product_id and p.get("is_active", True)), None)
        if not product:
            raise AppException("Product not found", status_code=404, code="PRODUCT_NOT_FOUND")

        if data.name is not None:
            product["name"] = data.name
        if data.category_id is not None:
            product["category_id"] = data.category_id
        if data.cost_price is not None:
            product["cost_price"] = data.cost_price
        if data.selling_price is not None:
            product["selling_price"] = data.selling_price
        if data.min_stock_level is not None:
            product["min_stock_level"] = data.min_stock_level

        res = product.copy()
        res["stock_status"] = cls._compute_stock_status(product["stock_quantity"], product["min_stock_level"])
        return res

    @classmethod
    def adjust_stock(cls, product_id: str, data: StockAdjustmentRequest) -> dict:
        product = next((p for p in db.products if p["id"] == product_id and p.get("is_active", True)), None)
        if not product:
            raise AppException("Product not found", status_code=404, code="PRODUCT_NOT_FOUND")

        prev_stock = product["stock_quantity"]
        new_stock = prev_stock + data.quantity_change
        if new_stock < 0:
            raise AppException("Stock quantity cannot be negative", status_code=400, code="INSUFFICIENT_STOCK")

        product["stock_quantity"] = new_stock
        cls.record_movement(product_id, data.type, data.quantity_change, prev_stock, new_stock, data.reason)

        res = product.copy()
        res["stock_status"] = cls._compute_stock_status(new_stock, product["min_stock_level"])
        return res

    @classmethod
    def record_movement(cls, product_id: str, m_type: StockMovementType, qty: int, prev: int, new: int, reason: str):
        movement = {
            "id": f"mov-{uuid.uuid4().hex[:6]}",
            "product_id": product_id,
            "movement_type": m_type.value if hasattr(m_type, 'value') else str(m_type),
            "quantity": qty,
            "previous_stock": prev,
            "new_stock": new,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat()
        }
        db.stock_movements.append(movement)
        return movement
