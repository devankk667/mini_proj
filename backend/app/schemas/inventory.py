from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from backend.app.schemas.enums import StockMovementType

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class ProductCreate(BaseModel):
    name: str
    sku: str
    category_id: str
    cost_price: float = Field(gt=0)
    selling_price: float = Field(gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    min_stock_level: int = Field(default=5, ge=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category_id: Optional[str] = None
    cost_price: Optional[float] = None
    selling_price: Optional[float] = None
    min_stock_level: Optional[int] = None

class StockAdjustmentRequest(BaseModel):
    quantity_change: int
    type: StockMovementType
    reason: str

class ProductResponse(BaseModel):
    id: str
    name: str
    sku: str
    category_id: str
    cost_price: float
    selling_price: float
    stock_quantity: int
    min_stock_level: int
    stock_status: str
    is_active: bool

class StockMovementResponse(BaseModel):
    id: str
    product_id: str
    movement_type: StockMovementType
    quantity: int
    previous_stock: int
    new_stock: int
    reason: str
    timestamp: str
