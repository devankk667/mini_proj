from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.repositories.in_memory import db

client = TestClient(app)

def get_auth_headers():
    login_res = client.post("/api/auth/login", json={"username": "owner", "password": "admin123"})
    token = login_res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_sales_and_purchase_workflow():
    headers = get_auth_headers()

    prod_before = client.get("/api/inventory/products/prod-1", headers=headers).json()
    assert prod_before["stock_quantity"] == 40

    pur_payload = {
        "supplier_name": "Tech Suppliers Inc",
        "items": [{"product_id": "prod-1", "quantity": 10, "unit_price": 14.0}],
        "tax_rate": 5.0,
        "discount": 0.0
    }
    pur_res = client.post("/api/purchases", json=pur_payload, headers=headers)
    assert pur_res.status_code == 201
    pur_data = pur_res.json()
    assert pur_data["status"] == "COMPLETED"

    prod_after_pur = client.get("/api/inventory/products/prod-1", headers=headers).json()
    assert prod_after_pur["stock_quantity"] == 50

    sale_payload = {
        "customer_id": "cust-1",
        "items": [{"product_id": "prod-1", "quantity": 5}],
        "tax_rate": 0.0,
        "discount": 5.0
    }
    sale_res = client.post("/api/sales", json=sale_payload, headers=headers)
    assert sale_res.status_code == 201
    sale_data = sale_res.json()
    assert sale_data["status"] == "COMPLETED"

    prod_after_sale = client.get("/api/inventory/products/prod-1", headers=headers).json()
    assert prod_after_sale["stock_quantity"] == 45

    fail_sale_res = client.post("/api/sales", json={
        "customer_id": "cust-1",
        "items": [{"product_id": "prod-1", "quantity": 100}]
    }, headers=headers)
    assert fail_sale_res.status_code == 400
    assert "INSUFFICIENT_STOCK" in fail_sale_res.json()["errors"][0]["code"]
