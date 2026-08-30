from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class CustomerCreate(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class CustomerResponse(BaseModel):
    id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    total_spent: float
    is_active: bool

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: Optional[float] = None

class OrderItemResponse(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float

class PurchaseCreate(BaseModel):
    supplier_name: str
    items: List[OrderItemCreate]
    tax_rate: float = Field(default=0.0, ge=0)
    discount: float = Field(default=0.0, ge=0)

class PurchaseResponse(BaseModel):
    id: str
    supplier_name: str
    items: List[OrderItemResponse]
    subtotal: float
    tax: float
    discount: float
    total: float
    status: str
    created_at: str

class SaleCreate(BaseModel):
    customer_id: Optional[str] = None
    items: List[OrderItemCreate]
    tax_rate: float = Field(default=0.0, ge=0)
    discount: float = Field(default=0.0, ge=0)

class SaleResponse(BaseModel):
    id: str
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    items: List[OrderItemResponse]
    subtotal: float
    tax: float
    discount: float
    total: float
    status: str
    created_at: str
