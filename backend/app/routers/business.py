from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from backend.app.schemas.business import (
    CustomerCreate, CustomerUpdate, CustomerResponse,
    PurchaseCreate, PurchaseResponse,
    SaleCreate, SaleResponse
)
from backend.app.services.customer_service import CustomerService
from backend.app.services.purchase_service import PurchaseService
from backend.app.services.sale_service import SaleService
from backend.app.services.auth_service import require_roles, get_current_user_from_token

router = APIRouter(prefix="/api", tags=["Business Operations"])

@router.get("/customers", response_model=List[CustomerResponse])
def list_customers(search: Optional[str] = Query(None), current_user: dict = Depends(get_current_user_from_token)):
    return CustomerService.list_customers(search)

@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: str, current_user: dict = Depends(get_current_user_from_token)):
    return CustomerService.get_customer(customer_id)

@router.post("/customers", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(data: CustomerCreate, current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER", "STAFF"]))):
    return CustomerService.create_customer(data)

@router.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: str, data: CustomerUpdate, current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER"]))):
    return CustomerService.update_customer(customer_id, data)

@router.get("/purchases", response_model=List[PurchaseResponse])
def list_purchases(current_user: dict = Depends(get_current_user_from_token)):
    return PurchaseService.list_purchases()

@router.post("/purchases", response_model=PurchaseResponse, status_code=status.HTTP_201_CREATED)
def create_purchase(data: PurchaseCreate, current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER"]))):
    return PurchaseService.create_purchase(data)

@router.post("/purchases/{purchase_id}/cancel", response_model=PurchaseResponse)
def cancel_purchase(purchase_id: str, current_user: dict = Depends(require_roles(["ADMIN", "OWNER"]))):
    return PurchaseService.cancel_purchase(purchase_id)

@router.get("/sales", response_model=List[SaleResponse])
def list_sales(current_user: dict = Depends(get_current_user_from_token)):
    return SaleService.list_sales()

@router.get("/sales/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: str, current_user: dict = Depends(get_current_user_from_token)):
    return SaleService.get_sale(sale_id)

@router.post("/sales", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
def create_sale(data: SaleCreate, current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER", "STAFF"]))):
    return SaleService.create_sale(data)

@router.post("/sales/{sale_id}/cancel", response_model=SaleResponse)
def cancel_sale(sale_id: str, current_user: dict = Depends(require_roles(["ADMIN", "OWNER", "MANAGER"]))):
    return SaleService.cancel_sale(sale_id)
