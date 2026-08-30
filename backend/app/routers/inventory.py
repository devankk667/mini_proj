from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from backend.app.schemas.inventory import (
    ProductCreate, ProductUpdate, ProductResponse, StockAdjustmentRequest, StockMovementResponse, CategoryResponse
)
from backend.app.services.inventory_service import InventoryService
from backend.app.services.auth_service import require_roles, get_current_user_from_token
from backend.app.repositories.in_memory import db

router = APIRouter(prefix="/api/inventory", tags=["Inventory"])

@router.get("/categories", response_model=List[CategoryResponse])
def get_categories(current_user: dict = Depends(get_current_user_from_token)):
    return db.categories

@router.get("/products", response_model=List[ProductResponse])
def list_products(
    search: Optional[str] = Query(None),
    category_id: Optional[str] = Query(None),
    current_user: dict = Depends(get_current_user_from_token)
):
    return InventoryService.list_products(search=search, category_id=category_id)

@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: str, current_user: dict = Depends(get_current_user_from_token)):
    return InventoryService.get_product(product_id)

@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    data: ProductCreate,
    current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER"]))
):
    return InventoryService.create_product(data)

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: str,
    data: ProductUpdate,
    current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER"]))
):
    return InventoryService.update_product(product_id, data)

@router.post("/products/{product_id}/adjust-stock", response_model=ProductResponse)
def adjust_stock(
    product_id: str,
    data: StockAdjustmentRequest,
    current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER", "STAFF"]))
):
    return InventoryService.adjust_stock(product_id, data)

@router.get("/movements", response_model=List[StockMovementResponse])
def list_movements(current_user: dict = Depends(get_current_user_from_token)):
    return db.stock_movements
